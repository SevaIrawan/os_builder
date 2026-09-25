// G-02 helper: read n8n Workflow SDK code on stdin, print the node configs it declares as JSON.
// The SDK functions are replaced by stubs that only record what they are given, so the code's
// object literals are evaluated (template literals resolve their escapes exactly as n8n will)
// without contacting n8n. Runs in a vm context with a timeout.
'use strict';
const vm = require('vm');
const fs = require('fs');

let src = fs.readFileSync(0, 'utf8');
const imp = src.match(/import\s*\{([^}]*)\}\s*from\s*['"]@n8n\/workflow-sdk['"]\s*;?/);
const names = imp ? imp[1].split(',').map(s => s.trim().split(/\s+as\s+/).pop()).filter(Boolean) : [];
src = src.replace(/^\s*import\b[^;\n]*;?\s*$/mg, '');
src = src.replace(/\bexport\s+default\s+/, '__default = ');
src = src.replace(/^(\s*)export\s+/mg, '$1');

const seen = new Set();
const captured = [];
function scan(v, depth) {
  if (depth > 8 || v === null || typeof v !== 'object' || seen.has(v)) return;
  seen.add(v);
  if (typeof v.type === 'string' && v.config && typeof v.config === 'object') {
    captured.push({ type: v.type, version: v.version, config: v.config });
  }
  for (const k of Object.keys(v)) scan(v[k], depth + 1);
}
function chain() {
  const f = function () {};
  const p = new Proxy(f, {
    get(t, k) {
      if (k === Symbol.toPrimitive) return () => '';
      if (k === 'then') return undefined;
      return (...a) => { a.forEach(x => scan(x, 0)); return p; };
    },
    apply(t, th, a) { a.forEach(x => scan(x, 0)); return p; }
  });
  return p;
}
const ctx = { __default: null, console: { log() {}, warn() {}, error() {} } };
for (const n of names) {
  ctx[n] = (...a) => { a.forEach(x => scan(x, 0)); return n === 'expr' ? String(a[0]) : chain(); };
}
vm.createContext(ctx);
vm.runInContext(src, ctx, { timeout: 3000 });
const out = captured.map(c => ({
  type: c.type,
  name: c.config.name,
  parameters: c.config.parameters || {},
  retryOnFail: c.config.retryOnFail === true,
  settings: c.config.settings || {},
  credentials: c.config.credentials || null
}));
process.stdout.write(JSON.stringify(out));
