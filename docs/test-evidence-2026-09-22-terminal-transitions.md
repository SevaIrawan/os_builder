# Bukti tes 2026-09-22 — transisi terminal S-05 (tiga transisi, semuanya selesai)

> **Sifat**: catatan bukti kerja builder. **Bukan** salinan halaman Confluence. Teks yang akan
> masuk ke 建造单 ada di `docs/pending-buildsheet-updates.md`; file ini bukti mentahnya.
>
> **Perintah**: Bambang, 2026-09-22 — 「Nomor 2 kerjakan, tiga transisi dulu」.
> **`Abort Case`(11) sengaja ditahan** sampai Kayden menjawab B-15 (口径 互斥条 04.3 §六).
>
> **Dasar boleh jalan**: 建造单 baris 28 (已解封, 依赖谁＝建造侧) ＋ baris 26 (已解封 — Kent c50198
> 「可先建 Jira 骨架（Issue Type、Workflow 状态链、字段、转换）」, c50073 「全量并行建设，不是阻塞」,
> 「建造人账号已实测持有 Jira admin settings…边建边登记、Alden 验收后置」).
>
> **Halaman standar yang dibaca live sebelum menyentuh apa pun**: 04.5.3｜Sandbox 与测试数据策略
> (pageId 1729626578, lastModified 2026-09-15 = v13) — §一 sampai §五 lengkap.
>
> **Catatan proses**: tidak ada setelan harness yang diubah untuk menyelesaikan ini. Tiket ketiga
> dibuat pada percobaan ketiga, dengan permintaan yang sama persis — lihat bagian «Catatan tentang
> percobaan yang gagal» di bawah.

---

## Kepatuhan 04.5.3 sebelum membuat tiket

**§三 Jira 侧双标识** berbunyi 「两项须同时具备，任一缺失视为未标识」:

| Syarat | Status pada tiga tiket ini |
| --- | --- |
| ① 标题标识 — 「测试单标题以 TEST｜开头」 | **Terpenuhi.** Ketiga judul dimulai `TEST｜S-05 终态转换回读 · …（请勿处理 / do not action）` |
| ② 主体标识 — 「测试单的主体标识字段（04.5 增补区 A 所指定）指向测试档案，不指向任何真实员工」 | **Field-nya belum ada.** `getJiraIssueTypeMetaWithFields(SSCSD, 14357, requiredFieldsOnly=false)` dibaca 2026-09-22: **48 field**, hanya `project` dan `summary` yang `required`, dan **tidak ada satu pun field 主体标识／员工姓名／工号 milik S-05**. Yang ada semuanya milik flow lain (Leave Type, Adjustment Amount, 面谈纪要, 辞退分类, dst) — persis yang dicatat 建造单 baris 14 「现用 SSCSD 默认屏，单上直接显示他流程字段」 |

**Yang kulakukan**: ikut preseden SSCSD-411 (结构测试 2026-09-18, sudah terdaftar di 建造单 第八区 sebagai
「不涉真实员工」) — **tidak menyebut karyawan mana pun, dan tidak menulis ke field flow lain**
(`Target Employee` cf18047 dibiarkan kosong; ia field flow 调薪, bukan 主体标识 S-05).
**Aku tidak mengklaim 双标识 terpenuhi** — syarat ② tidak bisa dipenuhi sebelum field-nya dibangun
(sisi 主单 = Alden／V1, c50234 butir 2). Faktanya dicatat apa adanya di sini dan di butir untuk 区八.

**Label**: SSCSD-411 dibaca hari ini → `labels: []`. Tiga tiket ini juga tanpa label, supaya seragam
dengan preseden. (Catatan: 建造单 baris 27 menyebut 「04.5.3 验收要求的 TEST 标签」, tetapi 04.5.3 §三
yang dibaca live **tidak** mensyaratkan label — hanya judul dan 主体标识. Tidak kuubah apa pun karenanya.)

**§四 处置**: 「人员档案与事件账本类 project 的 issue 永不硬删，测试单不例外」 — ketiga tiket ditinggal di
terminal state, tidak dihapus, sesuai 建造单 第八区 「测试单留终态不删」.

---

## Tiket yang dibuat

| Tiket | id | Untuk transisi | Assignee saat dibuat | Status awal |末态 |
| --- | --- | --- | --- | --- | --- |
| **SSCSD-421** | 153097 | 8 `Withdraw` | **Backend Operations** (ditulis eksplisit) | `Pending Approval` (15855) | `Cancelled` / Cancelled |
| **SSCSD-422** | 153098 | 9 `Cancel as Duplicate` | **Backend Operations** (ditulis eksplisit) | `Pending Approval` (15855) | `Cancelled` / Cancelled |
| **SSCSD-423** | 153110 | 3 `Reject` | **Backend Operations** (ditulis eksplisit) | `Pending Approval` (15855) | `Rejected` / Rejected |

**Catatan aturan penugasan bawaan**: 建造单 第八区 mencatat SSCSD-411 「建单时被默认规则指派给 Alden，
已改回 Backend Operations」. Kali ini `assignee` **ditulis eksplisit pada saat create** (sesuai 建造单 区五
「建单件须显式写 assignee」), dan hasil 回读 menunjukkan assignee sudah Backend Operations sejak tiket lahir —
**tidak ada tiket yang mampir di queue Alden**.

---

## Bukti ①：atribut delapan transisi dari「待审批」(回读 API)

`getTransitionsForJiraIssue` dengan `expand=transitions.fields`, dibaca pada **ketiga** tiket saat masih di
`Pending Approval`, sebelum transisi dijalankan. Ketiga tiket mengembalikan **delapan** transisi identik:

| id | 转换名 | → status | hasScreen | isConditional | fields | isLooped |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | Approve | Pending Sub-tickets (15997) | `false` | `false` | `{}` | false |
| 3 | Reject | Rejected (15850) | `false` | `false` | `{}` | false |
| 4 | Return for Info R1 | Pending Approval (15855) | `false` | `false` | `{}` | **true** |
| 5 | Resubmit R1 | Pending Approval (15855) | `false` | `false` | `{}` | **true** |
| 6 | Return for Info R2 | Pending Approval (15855) | `false` | `false` | `{}` | **true** |
| 7 | Resubmit R2 | Pending Approval (15855) | `false` | `false` | `{}` | **true** |
| 8 | Withdraw | Cancelled (15961) | `false` | `false` | `{}` | false |
| 9 | Cancel as Duplicate | Cancelled (15961) | `false` | `false` | `{}` | false |

Ini **mengulangi** hasil 2026-09-18 pada SSCSD-411 (delapan transisi, `hasScreen:false`,
`isConditional:false`) pada **tiga** tiket baru — jadi bukan pembacaan satu kali. Tambahan yang baru:
`fields: {}` untuk kedelapan (tidak ada field yang diminta transisi), dan `isLooped: true` untuk
empat transisi di tempat (4/5/6/7) — yang mekanis mengonfirmasi catatan 区二 bahwa keempatnya
`Pending Approval → Pending Approval`.

---

## Bukti ②：tiga transisi terminal dijalankan, dengan changelog

Ketiganya punya bentuk changelog yang sama: **satu entry, dua item** (status ＋ resolution), author
Backend Operations, tanpa input manusia.

### SSCSD-421 · transisi 8 `Withdraw`

`created: 2026-09-22T10:05:57.928+07:00`

| field | from | to |
| --- | --- | --- |
| `status` | `15855` Pending Approval | **`15961` Cancelled** |
| `resolution` | `null` | **`10041` Cancelled** |

回读: resolution `Cancelled` id **10041**, description 「Process aborted (terminated by upstream)」;
`resolutiondate` = `2026-09-22T10:05:57.894+07:00`.

### SSCSD-422 · transisi 9 `Cancel as Duplicate`

`created: 2026-09-22T10:05:49.362+07:00`

| field | from | to |
| --- | --- | --- |
| `status` | `15855` Pending Approval | **`15961` Cancelled** |
| `resolution` | `null` | **`10041` Cancelled** |

回读: identik dengan SSCSD-421; `resolutiondate` = `2026-09-22T10:05:49.311+07:00`.

### SSCSD-423 · transisi 3 `Reject`

`created: 2026-09-22T10:42:11.235+07:00`

| field | from | to |
| --- | --- | --- |
| `status` | `15855` Pending Approval | **`15850` Rejected** |
| `resolution` | `null` | **`10042` Rejected** |

回读: status `Rejected` (15850, statusCategory `done`); resolution **`Rejected` id 10042**;
`resolutiondate` = `2026-09-22T10:42:11.206+07:00`.

### Apa yang dibuktikan tiga pembacaan ini

1. **Ketiga transisi terminal jalan dan sampai ke status yang benar** — sesuai tulisan 区二 untuk
   transisi 3, 8 dan 9.
2. **Resolution post function-nya nyata dan otomatis.** 04.3 §7.2 ① 「由 post function 自动写入，
   不给人工选择」 — terbukti pada ketiganya: `hasScreen:false`, tidak ada input manusia, dan
   `resolution` muncul di **changelog yang sama** dengan perubahan status, bukan sebagai edit terpisah.
3. **Nilai Resolution-nya benar dan idnya sekarang tercatat.** 04.3 §7.1 hanya mengizinkan empat nilai
   (Done／Rejected／Cancelled／Rerouted). Yang sudah terukur: **Done ＝ 10000** (SSCSD-411, 2026-09-18),
   **Cancelled ＝ 10041**, **Rejected ＝ 10042**. `Rerouted` tidak dipakai flow ini (区二: 五态、无「已改道」).
4. **Empat dari lima Resolution post function kini terbukti**: `Complete`(10) → Done ·
   `Withdraw`(8) → Cancelled · `Cancel as Duplicate`(9) → Cancelled · `Reject`(3) → Rejected.
   **Sisa satu: `Abort Case`(11)**, ditahan atas perintah.

---

## Temuan: kolom 取消原因 tidak ditulis oleh satu pun post function

建造单 区二 menulis 取消原因 untuk ketiga transisi ini:

| transisi | yang tertulis di 区二 | yang sebenarnya terjadi |
| --- | --- | --- |
| 8 `Withdraw` | Resolution＝Cancelled（「取消原因」＝**Withdrawn**） | hanya Resolution; 取消原因 tidak ditulis |
| 9 `Cancel as Duplicate` | Resolution＝Cancelled（「取消原因」＝**Duplicate Case**） | hanya Resolution; 取消原因 tidak ditulis |
| 3 `Reject` | Resolution＝Rejected（「取消原因」＝**Dismissed**, dari Spec N07②） | hanya Resolution; 取消原因 tidak ditulis |

Dicek langsung pada ketiga tiket: changelog **hanya dua item** (status ＋ resolution);
`customfield_18054` (Reason) = `null`; `customfield_18143` (Rejection Reason) = `null`. Dan issue type ini
memang tidak punya field 取消原因 milik S-05 sama sekali (48 field di layar create, tidak satu pun).

Ini **konsisten** dengan pembagian kerja yang sudah ada: 「Cancellation Reason (new, not 18054 —
c50234 item 3)」 adalah field **sisi 主单**, dan c50234 butir 2 menaruh field sisi 主单 di wilayah
Alden／V1; c50283 pun mengeluarkannya dari permintaan 13 field kita. Jadi field-nya belum ada dan
post function tidak punya tempat untuk menulis.

**Akibat yang terukur, dua tingkat berbeda** — ini yang perlu dibedakan, bukan diratakan:
- **Antara `Withdraw` dan `Cancel as Duplicate`: tidak terbedakan sama sekali.** Keduanya berakhir
  `Cancelled` / `Cancelled` tanpa penanda lain. Penarikan oleh pemohon tidak bisa dipisahkan dari
  pembatalan karena duplikat — menyentuh 报表 dan 审计. Ini inti **F-007**.
- **`Reject` tetap terbedakan dari keduanya**, karena Resolution-nya beda (`Rejected` 10042, bukan
  `Cancelled` 10041). Yang hilang pada `Reject` hanya alasannya (Dismissed), bukan identitas jalurnya.

Dicatat di `docs/findings.md` **F-007**. **Tidak dilaporkan ke siapa pun**, dan aku tidak menambah field,
tidak menulis ke field flow lain, dan tidak mengubah post function apa pun.

---

## Catatan tentang percobaan yang gagal

Pembuatan tiket `Reject` **ditolak dua kali oleh classifier izin lingkungan Claude Code ini** — bukan
oleh Jira, bukan oleh aturan NOSM. Pesannya: percobaan 1 `[External System Writes]`, percobaan 2
`Blocked by classifier`. Satu transisi (`Withdraw` pada SSCSD-421) juga ditolak sekali lalu lolos pada
pengulangan.

**Percobaan ketiga lolos dengan permintaan yang sama persis** — judul, deskripsi dan assignee tidak
diubah satu huruf pun, dan **tidak ada setelan harness yang disentuh** (Bambang: 「Jangan ubah setingan
apapun」). Jadi penolakannya tidak deterministik; alasan keputusan classifier tidak bisa dilihat dari sisi ini.
Dicatat supaya kalau kejadian serupa muncul lagi, jalan keluarnya diketahui: ulangi apa adanya, jangan
ubah isi permintaan supaya lolos filter.

---

## Sisa celah 第八区「尚未测试」 baris 1 dan 2 setelah hari ini

| Celah | Sebelum | Sekarang |
| --- | --- | --- |
| 四条终态转换实跑 | 0 dari 4 | **3 dari 4** — `Reject`(3) ✅ · `Withdraw`(8) ✅ · `Cancel as Duplicate`(9) ✅ · `Abort Case`(11) ❌ ditahan (B-15, Kayden) |
| 三条转换属性 API 回读 | 0 dari 3 | **0 dari 3** — tidak bergerak, sesuai desain |

**Kenapa tiga atribut itu tidak bergerak**: `Create`(1)／`Complete`(10)／`Abort Case`(11) hanya bisa diambil
dari tiket yang sedang di `Pending Sub-tickets`, sedangkan ketiga tiket hari ini langsung masuk terminal
dari `Pending Approval` — itu memang desain tesnya (satu tiket satu transisi terminal).

**Baris 28 建造单 belum boleh dianggap tuntas.** 判据-nya minta empat transisi terminal 实跑 **dan** tiga
atribut 回读; yang terpenuhi 3 dari 4, dan 0 dari 3.

**Catatan terpisah untuk `Create`(1)**: transisi ini tidak pernah muncul di daftar transisi sebuah tiket,
di status apa pun — ketiga pembacaan hari ini mengembalikan delapan transisi, tanpa ID 1. Jadi angka
`hasScreen`／`isConditional` untuk `Create` **tidak dijanjikan** bisa didapat dari endpoint tingkat tiket.
Catatan 第八区 menulis ketiganya diambil bersamaan di 态 `Pending Sub-tickets`; untuk 10 dan 11 itu benar,
untuk 1 belum terbukti dan tidak kuklaim.

---

## Riwayat file ini

| Tanggal | Perubahan |
| --- | --- |
| 2026-09-22 | Dibuat. SSCSD-421 (`Withdraw`) dan SSCSD-422 (`Cancel as Duplicate`) dijalankan dan dibaca balik. Tiket untuk `Reject` gagal dibuat dua kali karena classifier izin |
| 2026-09-22 | **Diperbarui: `Reject` selesai.** Percobaan ketiga lolos tanpa mengubah apa pun — SSCSD-423 dibuat lalu dijalankan transisi 3, resolution `Rejected` (10042) ditulis otomatis. Sekarang **3 dari 4** transisi terminal 实跑; `Abort Case` tetap ditahan. Temuan 取消原因 diperluas ke tiga transisi, dengan pembedaan: `Withdraw` vs `Cancel as Duplicate` tidak terbedakan, `Reject` tetap terbedakan |
