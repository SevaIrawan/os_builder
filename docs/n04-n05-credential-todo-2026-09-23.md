# N04 / N05 / N20 — catatan kerja tertunda (2026-09-23, update 2026-09-24)

> Catatan pribadi Bambang, bukan bagian dari `docs/pending-buildsheet-updates.md` /
> `docs/buildsheet-blocker-status.md` (itu soal halaman 建造单 Confluence). Ini murni
> pengingat teknis n8n, disimpan lokal di repo, tidak ditulis ke Confluence/Jira/Slack.

## N05｜重复案件与历史记录检查 (`LJwiAZFfnuq6tmju`)

**Masalah**: node **"Write Duplicate Marker Comment (internal)"** (`n8n-nodes-base.httpRequest`,
POST ke `/rest/api/3/issue/{issueKey}/comment`) belum punya kredensial terpasang.
`authentication: predefinedCredentialType`, `nodeCredentialType: jiraSoftwareCloudApi`,
tapi field `credentials` di parameter node masih kosong (dicek via `get_workflow_details`
berkali-kali sore ini, terakhir `versionId: 4d30db71-356c-4b33-8026-bd9dce5a60ca`,
`updatedAt: 2026-09-23T10:22:06.898Z` — tidak berubah).

Kredensial yang perlu dipasang: **"Bot_SSC (Jira write)"**.

**Yang sudah dicoba (dari HP, n8n2.ohmediaa.com) dan hasilnya**:
- Buka node, pilih "Bot_SSC (Jira write)" di dropdown Credential → tampil di layar tapi
  **tidak pernah tersimpan ke server** (dicek ulang via API tiap kali, `versionId` tetap sama).
- Panel node di mobile tidak punya tombol Save eksplisit — cuma bisa ditutup (X/back),
  lalu save sesungguhnya ada di level workflow. Tapi di level workflow, bar atas cuma
  menampilkan **"Publish"** dan **"⋮"**, tidak ada tombol "Save" terpisah yang jelas.
- **Jangan tap "Publish"** — itu berisiko langsung mengaktifkan workflow, padahal
  build-sheet description N05 menulis: *"Built inactive, needs dry-run + errorWorkflow +
  Alden approval"*. Belum boleh aktif.
- Sempat ada 1x eksekusi manual gak sengaja (`execution 16341`, status error, durasi
  ~0.2 detik) — gagal di node paling awal ("Confirm Case Visible") karena tidak ada
  `issueKey` input asli. **Tidak ada tulisan ke Jira asli**, tidak ada efek permanen.
  Workflow tetap `active: false` sepanjang sesi ini.
- Struktur workflow (koneksi, logic JQL/code/JSON) tidak berubah — cuma pergeseran posisi
  node beberapa pixel dan penambahan field default kosong (`"options":{}` dll), itu
  kosmetik otomatis dari n8n, bukan kerusakan.

**Rencana lanjut di laptop**:
1. Buka N05 dari browser desktop (bukan mobile) — biasanya tombol Save/Publish
   terpisah lebih jelas di layar lebar.
2. Buka node "Write Duplicate Marker Comment (internal)" → Authentication →
   Predefined Credential Type → Jira SW Cloud API → pilih **Bot_SSC (Jira write)**.
3. **Save workflow** (bukan Publish) — workflow harus tetap inactive.
4. Minta saya cek ulang via `get_workflow_details` — kalau field `credentials` sudah
   muncul di node itu dan `versionId` berubah, berarti benar tersimpan.
5. Ingat: pasang kredensial ini belum berarti N05 boleh diaktifkan/dipublish. Masih
   perlu dry-run, errorWorkflow terpasang, dan approval Alden dulu (sesuai deskripsi
   workflow) sebelum langkah publish/activate.

## N04｜路由分发 (`UBLsvYaSlCI3pLWs`)

Dicek ulang hari ini — **tidak ada masalah ditemukan**. Strukturnya sangat sederhana:
satu trigger + satu node "Call N05" (`executeWorkflow`, memanggil `LJwiAZFfnuq6tmju`
dan menunggu hasilnya). Tidak pakai kredensial sendiri, jadi tidak kena isu yang sama
seperti N05. `active: false`, `versionId: 0aad8ecb-e97e-4297-9908-b6c15559fdca`,
belum berubah sejak dibuat.

Satu-satunya keterkaitan: karena N04 memanggil N05, N04 **tidak bisa dites end-to-end
secara utuh** sampai kredensial N05 di atas terpasang — tapi itu bukan masalah di N04
sendiri, cuma downstream dari poin di atas.

## N20｜解雇自动开单与交接 (`ToIGnEJmksSPhC85`) — dibangun 2026-09-24

**Status**: kerangka (skeleton), `active: false`, **belum disambung penuh** — bukan bug,
memang disengaja per instruksi Bambang. Node "Call Resignation Upstream Trigger Entry"
(`executeWorkflow`) pakai `workflowId` placeholder, bukan ID asli, karena workflow sisi
resign (员工离职「系统触发入口」, per Kent OSD-116 c50381 / balasan Bambang NSE-1137 c50435)
**belum ada di n8n** — dicek via `search_workflows` sebelum bangun, cuma ada 17 workflow
员工离职 lama (N1-N12, channel 2), tidak ada yang baru untuk entry point ini.

**Alur yang sudah jadi**: Trigger (terima caseKey/employeeAccountId/judgmentType/judgmentRef)
→ baca comment case S-05 (cek marker `[[nos-s05-n20-triggered:...]]` biar idempoten, pola
sama kayak N05 tapi versi E11-safe dari awal) → IF sudah pernah trigger → kalau belum, map
judgmentType ke option id (纪律违规→15846, PIP未改善→15847, sesuai kontrak Kent c50381) →
panggil entry Geri (placeholder) → bikin Trigger Link (issueLink type 10075) → tulis comment
marker internal.

**Kredensial — kena masalah yang SAMA PERSIS dengan N05, sudah diduga sebelum bangun**:
- Node "Read S-05 Case Comments" (Jira native, `issueComment.getAll`) — kredensial Bot_SSC
  **otomatis kepasang** oleh n8n waktu create (`autoAssignedCredentials` di response).
- Dua node `httpRequest` ("Create Trigger Link", "Write Triggered Marker Comment") —
  **tidak** kepasang otomatis. Response create eksplisit bilang: *"HTTP Request nodes ...
  were skipped during credential auto-assignment. Their credentials must be configured
  manually."* Ini persis konfirmasi 07.06.1 E5 ("新建 httpRequest 节点仍须 UI 手工挂凭据").
  **Jangan diulang coba pasang lewat API** — sudah dikonfirmasi dua kali (N05, sekarang N20)
  kalau itu ditolak platform, bukan salah eksekusi.

**Rencana lanjut (sama seperti N05, tapi sekarang tahu pola errornya)**:
1. Buka N20 dari **desktop browser** (bukan HP) di n8n2.ohmediaa.com.
2. Node "Create Trigger Link (S-05 to resignation)" → Credential → pilih **Bot_SSC (Jira write)**.
3. Node "Write Triggered Marker Comment (internal)" → sama.
4. **Save** (bukan Publish/Activate) — tetap harus `inactive` sampai dry-run + errorWorkflow
   + approval Alden (sama syarat kayak N05).
5. Begitu Geri kasih tahu workflow id sisi resign-nya, saya ganti placeholder di node
   "Call Resignation Upstream Trigger Entry" dengan ID asli, lalu baru bisa dry-run end-to-end.

**Belum di-set**: `settings.errorWorkflow` (nos-ops alert on failure) — sama seperti N04/N05,
ini menunggu keputusan platform, belum saya paksa set sendiri.

## Menunggu 04.3 selesai revisi — dampak ke N07 / Abort Case (OSD-116 c50442)

**Sumber**: Kayden Lee, OSD-116 comment c50442, 2026-09-24T12:30:26+0700, balasan ke Alden
soal 04.3 §六 (撤回类 vs 失效类 pada 中止/Abort Case). Baris yang menyebut Bambang, dikutip
persis: *"@Bambang 待 04.3 改完，Abort Case 转态权限配给 HR Ops & Data 角色组，N07 确认重复
同口径。"*

**Yang perlu dikerjakan nanti, setelah 04.3 selesai direvisi (Kayden bilang "Kayden 侧已派人"
untuk revisi itu, belum ada versi baru per komentar ini)**:
1. Kasih hak transisi "Abort Case" ke role group **HR Ops & Data**.
2. Pastikan **N07** (pengecekan duplikat) pakai kriteria yang sama dengan 失效类 yang baru
   ditetapkan di 04.3 (khususnya nilai "Duplicate Case" yang menurut Kayden ditandai 失效类
   di tabel A Felix, S-05 sendiri tidak perlu diubah/direview ulang).

**Status**: belum dikerjakan, sengaja ditunda — 04.3 belum selesai direvisi per komentar
ini. Jangan mulai sebelum ada konfirmasi versi baru 04.3.
