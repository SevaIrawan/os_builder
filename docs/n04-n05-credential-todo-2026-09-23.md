# N04 / N05 — catatan kerja tertunda (2026-09-23)

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
