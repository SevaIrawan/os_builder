# Reading notes — 2026-09-22

> Catatan bacaan builder (Bambang). Bukan dokumen sah. Tiap angka disertai sumber dan cara bacanya.

## SSCSD-411 — pembacaan live 2026-09-22 ~06:30 WIB

Diminta dicek khusus. Dibaca penuh: field, changelog (7 entri), deskripsi, komentar, dan daftar transisi.

### 1. Dibaca lewat akun Backend Operations

Pembagian akses ini sudah diketahui sejak lama dan memang begitu rancangannya, **bukan temuan**:
akun pribadi tidak punya akses ke SSCSD, akun Backend Operations tidak punya akses ke OSD.
Sudah tercatat di `docs/action-list.md` D-11 (「akun pribadi tidak melihat SSCSD; akun layanan melihatnya」)
dan di `docs/drafts/2026-09-20-…` (「The Backend Operations account cannot see project OSD」).

Dicatat di sini hanya sebagai keterangan cara baca: SSCSD-411 dibaca lewat **`Atlassian_Rovo`**
(= `712020:a93fd17c…`, Backend Operations, `boteam001@nexmaxorg.com`), bukan lewat akun pribadi
(`Atlassian_MCP` = `712020:0ec04d28…`). Kedua id akun dipastikan lewat `atlassianUserInfo`.

### 2. Keadaan sekarang

| | |
|---|---|
| Key / id | SSCSD-411 / `152902` |
| Summary | 「TEST｜S-05 结构测试 · 状态链回读（请勿处理 / do not action）」 |
| Issue type | **Disciplinary Case `14357`** — 「Disciplinary and performance improvement handling master ticket (shape C per 04.3 §2). Spec S-05.」 |
| Project | SSCSD (`13162`), service_desk, kategori NOS |
| Status | **Completed `10593`** (kategori Done) |
| Resolution | **Done `10000`** |
| Dibuat | 2026-09-18 20:42:21 +07 |
| Selesai | 2026-09-18 20:53:20 +07 |
| `updated` | 2026-09-18 20:53:20 — **sama dengan resolutiondate, jadi tidak disentuh sejak itu** |
| Reporter / Assignee | Backend Operations |
| Priority | Medium |
| Labels | **kosong** |
| Issue links | **kosong** |
| Komentar | **0** |

### 3. Changelog — 7 entri, semuanya Backend Operations, semuanya 2026-09-18

| Waktu +07 | Perubahan |
|---|---|
| 20:45:01 | assignee **Alden → Backend Operations** |
| 20:45:52 | status Pending Approval `15855` → Pending Approval `15855` |
| 20:46:51 | status Pending Approval → Pending Approval |
| 20:52:58 | status Pending Approval → Pending Approval |
| 20:53:05 | status Pending Approval → Pending Approval |
| 20:53:12 | status Pending Approval → **Pending Sub-tickets `15997`** |
| 20:53:20 | status Pending Sub-tickets → **Completed `10593`** ＋ **baris terpisah** resolution `null` → **Done `10000`** |

**(a) Entri pertama fakta konfigurasi**: saat dibuat, tiket ter-assign ke **Alden**, lalu dipindah manual.
Itu perilaku default SSCSD, satu keluarga dengan temuan baris 14 建造单 (「`Disciplinary Case` 现用 SSCSD 默认屏」).

**(b) Empat transisi di tempat TERBUKTI.** Empat entri Pending Approval → Pending Approval ada hitam di atas
putih. Nilai status tidak berubah lintas keempatnya, jadi 主锁 Notify §9.4 (「所选 transition 已不在当前可用列表」)
memang tidak bisa menyala di situ. **Ini bukti live untuk baris 30 建造单.**
⚠️ **Batas bukti**: changelog mencatat **nilai status, bukan id transisi**. Jadi ini membuktikan terjadi
empat eksekusi di tempat; ia **tidak** membuktikan keempatnya adalah transisi id 4/5/6/7. Pemetaan ke id itu
berasal dari Workflow Text view (UI), bukti terpisah.

**(c) Post function Resolution terverifikasi.** 建造单 §Resolution menulis 「`Complete` 一条已实测验证
（SSCSD-411 changelog 出现独立一行 `Resolution: None → Done`）」 — dicek ke changelog live, **benar**:
entri 20:53:20 memang membawa item resolution tersendiri di samping item status.

### 4. Completed adalah terminal sungguhan

`getTransitionsForJiraIssue` dengan `includeUnavailableTransitions: true` **dan**
`skipRemoteOnlyCondition: true` → `transitions: []`. Nol transisi keluar dari Completed.

### 5. 🔴 Ketidakcocokan yang ditemukan: sepuluh vs sebelas transisi

Deskripsi SSCSD-411 (ditulis 2026-09-18 20:42, dua menit setelah tiket dibuat) berbunyi:

> 「结构测试单，依 04.5.3。不涉真实员工，无主体标识。
> 用途：回读 `NOS: Disciplinary Workflow` 的状态链、**十条转换**与 Resolution post function。
> 测试完成后留终态，不删除（04.5.3：NTP 与账本类 issue 永不硬删）。」

建造单 v33 menulis **sebelas** di dua tempat: 页首附表 baris 28 「五态复用、**十一条转换**」 dan 区二
转换表 yang memang mendaftar id **1–11**.

**Belum bisa diselesaikan dengan akses baca saja**, dan aku tidak menebak mana yang benar:
- Tidak ada operasi MCP yang membaca definisi workflow utuh (dicek lewat `discover`; yang ada hanya
  `listJiraIssueTransitions`, `listJiraStatuses`, dan keduanya tidak memberi definisi workflow).
- SSCSD-411 ada di status terminal dengan nol transisi keluar, jadi transisinya tidak bisa dienumerasi
  dari tiket ini.

Untuk menutupnya perlu salah satu: **(i)** cek Workflow Text view di UI, atau **(ii)** tiket tes baru yang
berhenti di Pending Approval lalu `listJiraIssueTransitions` — dan (ii) adalah penulisan, butuh perintah.

### 6. Kaitan dengan 07.06.1 E16 versi baru

Deskripsi tiket ini menegaskan 「测试完成后留终态，**不删除**」. E16 v34 mewajibkan probe menanyakan
**satu tiket yang diketahui ada**, dan menyebut tiket itu **承重对象** yang kegunaannya wajib didaftarkan
di 建造单. SSCSD-411 memenuhi syarat "tidak akan dihapus" itu, jadi ia kandidat jangkar sisi SSCSD untuk
probe S-05. Pembanding: Grade memakai SSCSD-381 dan NTP-187 sebagai jangkar.

---

## KOREKSI & CELAH SAPUAN — ditemukan 2026-09-22 ~06:45 WIB

Dipicu notifikasi email Rovo di akun Backend Operations. Email itu sendiri **bukan** notifikasi perubahan
— ia email produk Rovo berisi tiga saran prompt. **Tapi ia benar sebagai pemicu**: begitu aku cek Jira
lebih luas, ternyata ada yang terlewat.

### 1. Celah di sapuanku sendiri

Sapuan awal sesi ini mencakup: halaman Confluence NOSM, comment OSD-116, dan #nos-bo. **Jira di luar
OSD-116 tidak kusentuh sama sekali.** Itu salahku, dan juga lubang di skill `nosm-sync-check` — langkah 6
hanya mengatur sapuan halaman Confluence.

Sapuan JQL `updated >= -3d` pada **akun pribadi** memperlihatkan akun itu melihat proyek **WT, MLKB, NSE,
OSD** — puluhan tiket bergerak tiap hari. Yang relevan untuk kita: **NSE-1143**, bergerak
2026-09-21 18:01:35.

Sapuan JQL pada **akun Backend Operations** (`updated >= -10d`, dengan probe pembanding `key = SSCSD-411`
lebih dulu supaya nol-hasil tidak salah dibaca): 13 tiket, semuanya TEST — SSCSD-411, GPM-1…GPM-11, HR-1.
**Tidak ada yang bergerak sejak 2026-09-18.**

Jadi dua akun itu harus disapu dua-duanya bukan karena ada yang aneh, tapi karena memang masing-masing
melihat sebagian: OSD/NSE lewat akun pribadi, SSCSD/GPM/HR lewat akun Backend Operations.

### 2. NSE-1143 c50291 — Sinyee → Alden, 2026-09-21 18:01:35

**Lebih baru dari c50290.** 12 butir. Yang mengenai kerja S-05:

**🔴 ⑫ — ini membatalkan yang kutulis di atas soal SSCSD-411 sebagai jangkar E16.** Verbatim:

> 「我方先用 `key in (NTP-187, SSCSD-381, HR-1)` 做可见性锚点，**三张全回**，据此判「看得见 NTP、
> 零条不是可见性问题」——**那个判断是错的**。锚点 `NTP-187` 是一张 **TEST 档案**，没套生产档案那套
> 单据级安全级别；同 project 的生产对象我方一张也看不见。**即锚点探针证明的是「这一张看得见」，
> 不等于「这个 project 的同类对象都看得见」——锚点若是 TEST 记录，会给出覆盖面上的假阳性。**」

⚠️ **Koreksi atas bagian 6 catatan di atas**: aku menulis SSCSD-411 "kandidat jangkar sisi SSCSD untuk
probe S-05" karena ia ditandai tidak-akan-dihapus. **Alasan itu tidak cukup, dan kesimpulannya salah
arah.** SSCSD-411 adalah tiket **TEST**; menurut butir ini jangkar TEST justru memberi **positif palsu
pada cakupan** — ia membuktikan "yang satu ini terlihat", bukan "objek sejenis di project ini terlihat".
Sinyee sedang minta 口径 dari Alden soal ganti ke jangkar record produksi. **Putusan itu akan mengikat
probe S-05 kita juga — jadi jangan tetapkan jangkar S-05 sebelum Alden menjawab.**

**⑧ E16 celah sisa** — 「**探针守的是身份可见性，不是查询有结果**」. Probe menjaga visibilitas identitas,
bukan menjamin query mengembalikan baris. Bentuk kegagalannya: query nol baris → node hilir tidak
dieksekusi → tidak ada notifikasi terkirim → eksekusi tetap dilaporkan success. Sudah diperbaiki di件
守护层二 dengan `alwaysOutputData` → `true`. **Bentuk yang sama akan muncul di komponen SLA/守护 S-05.**

**⑨-1 — menambal titik buta E5.** Membuka node tanpa kredensial di UI membuat n8n **diam-diam mengisi
satu kredensial sejenis**, tanpa notice, tanpa highlight, tanpa error. E5 bilang "kredensial hanya bisa
dipastikan lewat mata"; butir ini menunjukkan **mata pun bisa melihat nilai yang terisi otomatis dan
salah**. Usul: judul jadi 「目视并与同链路的兄弟节点逐一比对」.

**⑨-2 — `options.rawBody: true` dikelupas lagi oleh UI save, dua webhook sekaligus.** Kegagalan yang sama
dengan E12; `typeVersion` tidak berubah, tidak ada error. Akibatnya `cand0` jadi string kosong dan
verifikasi tanda tangan turun ke bentuk lemah empat kandidat — komponen tetap jalan, hanya sesekali
menolak permintaan yang sah. **Relevan langsung untuk N03 S-05 yang juga entry Slack.**

**⑤ Cacat produksi di 离职 N2** — `Build Sig Candidates` tidak mengambil rawBody sama sekali; satu
permintaan sah (`text` berisi Mandarin dan spasi, urutan kunci rawBody beda) dihitung **tanda tangan
buruk lalu dibuang**. Bukti `exec 15939`: hanya `sig0` (rawBody) yang cocok. Grade N2 mempertahankan
`cand0` dan tidak menyalin kelemahan itu. **N03 kita harus ikut mempertahankan cand0.**

**② Fakta yang mengenai baris 5 建造单 kita** — Request Type tidak bisa dibaca lewat MCP:
「撞上 `/rest/servicedeskapi/requesttype` 是实验性 API、需 `X-ExperimentalApi: opt-in` 头，而 07.06 §6.2
已登记「现有 MCP 工具无法携带该头」，故**建造侧查不到该字段现值**」. Jadi waktu dua Request Type S-05
nanti dibuat, **kita tidak bisa membaca-balik konfigurasinya lewat API** — hanya sisi platform yang bisa.

**⑦ Sensus nomor eksekusi** — 229 rujukan: 90 masih hidup, 128 sudah terhapus, 11 bukan build ini.
「今后引 E16 对照探针一律引 `exec 15728`」. Dan `lhs2bBcFTx67uXzD` (probe izin yang dibangun 08-26)
**nol eksekusi** — komponennya ada, jejak jalannya hilang.

**⑫ NTP** — identitas orang hanya melihat **1** Talent-Profile (NTP-187, TEST milik sendiri); sekitar
**180 arsip produksi** ditutup issue security tingkat tiket (scheme 10876, 04.4.2 附二).

### 3. Yang harus diperbaiki di skill

Langkah 6 `nosm-sync-check` hanya menyapu halaman Confluence. Ia **tidak** menyapu kartu Jira. Karena itu
c50291 lolos, padahal ia lebih baru dari comment terbaru OSD-116 dan isinya membatalkan satu kesimpulan
yang baru saja kutulis. Sapuan Jira harus: JQL `updated >= -Nd` **di kedua akun**, dengan probe pembanding
lebih dulu, lalu baca kartu yang relevan — minimal OSD-116 **dan NSE-1143**.
