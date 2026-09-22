# Bukti tes 2026-09-22 — transisi terminal S-05 (tiga transisi, dua selesai)

> **Sifat**: catatan bukti kerja builder. **Bukan** salinan halaman Confluence. Teks yang akan
> masuk ke 建造单 ada di `docs/pending-buildsheet-updates.md`; file ini bukti mentahnya.
>
> **Perintah**: Bambang, 2026-09-22 — 「Nomor 2 kerjakan, tiga transisi dulu」. Yang dijalankan
> hanya tiga transisi terminal; **`Abort Case`(11) sengaja ditahan** sampai Kayden menjawab B-15.
>
> **Dasar boleh jalan**: 建造单 baris 28 (已解封, 依赖谁＝建造侧) ＋ baris 26 (已解封 — Kent c50198
> 「可先建 Jira 骨架（Issue Type、Workflow 状态链、字段、转换）」, c50073 「全量并行建设，不是阻塞」,
> 「建造人账号已实测持有 Jira admin settings…边建边登记、Alden 验收后置」).
>
> **Halaman standar yang dibaca live sebelum menyentuh apa pun**: 04.5.3｜Sandbox 与测试数据策略
> (pageId 1729626578, lastModified 2026-09-15 = v13) — §一 sampai §五 lengkap.

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

**§四 处置**: 「人员档案与事件账本类 project 的 issue 永不硬删，测试单不例外」 — kedua tiket ditinggal di
terminal state, tidak dihapus, sesuai 建造单 第八区 「测试单留终态不删」.

---

## Tiket yang dibuat

| Tiket | Untuk transisi | Assignee saat dibuat | Status awal |
| --- | --- | --- | --- |
| **SSCSD-421** (id 153097) | 8 `Withdraw` | **Backend Operations** (ditulis eksplisit saat create) | `Pending Approval` (15855) |
| **SSCSD-422** (id 153098) | 9 `Cancel as Duplicate` | **Backend Operations** (ditulis eksplisit) | `Pending Approval` (15855) |
| — (belum ada) | 3 `Reject` | — | **Gagal dibuat** — lihat bagian «Yang belum selesai» |

**Catatan aturan penugasan bawaan**: 建造单 第八区 mencatat SSCSD-411 「建单时被默认规则指派给 Alden，
已改回 Backend Operations」. Kali ini `assignee` **ditulis eksplisit pada saat create** (sesuai 建造单 区五
「建单件须显式写 assignee」), dan hasil回读 menunjukkan assignee sudah Backend Operations sejak tiket lahir —
tidak ada tiket yang mampir di queue Alden.

---

## Bukti ①：atribut delapan transisi dari「待审批」(回读 API)

`getTransitionsForJiraIssue` dengan `expand=transitions.fields`, dibaca pada kedua tiket saat masih di
`Pending Approval`, sebelum transisi dijalankan. Kedua tiket mengembalikan **delapan** transisi identik:

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
`isConditional:false`) pada dua tiket baru — jadi bukan pembacaan satu kali. Tambahan yang baru:
`fields: {}` untuk kedelapan (tidak ada field yang diminta transisi), dan `isLooped: true` untuk
empat transisi di tempat (4/5/6/7) — yang mekanis mengonfirmasi catatan 区二 bahwa keempatnya
`Pending Approval → Pending Approval`.

---

## Bukti ②：dua transisi terminal dijalankan, dengan changelog

### SSCSD-421 · transisi 8 `Withdraw`

changelog **total 1 entry**, author Backend Operations, `created: 2026-09-22T10:05:57.928+07:00`, dua item:

| field | from | to |
| --- | --- | --- |
| `status` | `15855` Pending Approval | **`15961` Cancelled** |
| `resolution` | `null` | **`10041` Cancelled** |

回读 field: `status` = Cancelled (15961, statusCategory `done`); `resolution` = **Cancelled id 10041**,
description 「Process aborted (terminated by upstream)」; `resolutiondate` = `2026-09-22T10:05:57.894+07:00`.

### SSCSD-422 · transisi 9 `Cancel as Duplicate`

changelog **total 1 entry**, author Backend Operations, `created: 2026-09-22T10:05:49.362+07:00`, dua item:

| field | from | to |
| --- | --- | --- |
| `status` | `15855` Pending Approval | **`15961` Cancelled** |
| `resolution` | `null` | **`10041` Cancelled** |

回读 field: sama persis; `resolutiondate` = `2026-09-22T10:05:49.311+07:00`.

### Apa yang dibuktikan dua pembacaan ini

1. **Kedua transisi terminal jalan dan sampai ke status yang benar** — `Cancelled` (15961), sesuai tulisan
   区二 untuk transisi 8 dan 9.
2. **Resolution post function-nya nyata dan otomatis.** 04.3 §7.2 ① 「由 post function 自动写入，
   不给人工选择」 — terbukti: `hasScreen:false`, tidak ada input manusia, dan `resolution` muncul di
   **changelog yang sama** dengan perubahan status, bukan sebagai edit terpisah.
3. **Nilainya `Cancelled` (10041)**, salah satu dari empat nilai yang diizinkan 04.3 §7.1
   (Done／Rejected／Cancelled／Rerouted).
4. Sebelum ini hanya `Complete`(10) yang pernah terbukti menulis Resolution otomatis (SSCSD-411,
   `None → Done`). Sekarang **tiga dari lima** sudah terbukti: `Complete`, `Withdraw`,
   `Cancel as Duplicate`. Sisa dua: `Reject`(3) dan `Abort Case`(11).

---

## Temuan: dua transisi berbeda menghasilkan data terminal yang identik

建造单 区二 menulis pembedaan ini untuk dua transisi itu:

- transisi 8 `Withdraw` → 「Resolution＝**Cancelled**（「取消原因」＝Withdrawn）」
- transisi 9 `Cancel as Duplicate` → 「Resolution＝**Cancelled**（「取消原因」＝Duplicate Case）」

**Yang sebenarnya terjadi**: kedua changelog **hanya berisi dua item** (status ＋ resolution), dan tidak ada
field 取消原因 yang tersentuh. Dicek langsung: `customfield_18054` (Reason) = `null` pada kedua tiket, dan
`customfield_18143` (Rejection Reason) = `null` juga. Jadi sesudah dijalankan, **SSCSD-421 dan SSCSD-422
punya data terminal yang identik** — status Cancelled, resolution Cancelled, tidak ada penanda lain.
Dari datanya saja, penarikan oleh pemohon tidak bisa dibedakan dari pembatalan karena duplikat.

Ini **konsisten** dengan pembagian kerja yang sudah ada, bukan hal baru yang bertentangan dengannya:
「Cancellation Reason (new, not 18054 — c50234 item 3)」 adalah field **sisi 主单**, dan c50234 butir 2
menaruh field sisi 主单 di wilayah Alden／V1; c50283 pun mengeluarkannya dari permintaan 13 field kita.
Jadi field-nya memang belum ada, dan post function tidak punya tempat untuk menulis.

**Yang baru dari pembacaan hari ini** adalah akibatnya, dan itu sudah terukur, bukan dugaan: selama field
itu belum ada, dua jalur pembatalan tidak terpisah di data — yang menyentuh 报表 dan 审计, bukan cuma
kenyamanan. Dicatat sebagai **F-007** di `docs/findings.md`. **Tidak dilaporkan ke siapa pun**, dan aku
tidak menambah field, tidak menulis ke field flow lain, dan tidak mengubah post function apa pun.

---

## Yang belum selesai

**Transisi 3 `Reject` belum dijalankan — tiketnya belum bisa dibuat.**
Percobaan membuat tiket TEST ketiga **diblokir dua kali oleh classifier izin lingkungan Claude Code
ini**, bukan oleh Jira dan bukan oleh aturan NOSM. Pesan yang dikembalikan: 「Permission for this action
was denied by the Claude Code auto mode classifier」 (percobaan 1: `[External System Writes]`;
percobaan 2: `Blocked by classifier`). Isi permintaannya identik dengan dua tiket yang berhasil,
hanya beda judul dan deskripsi.

Aku **tidak** mengakalinya dengan mengganti judul supaya lolos — judul harus menyebut apa yang dites.
Jadi transisi 3 tetap 未实跑, dan tiga baris 「尚未测试」 yang menyangkutnya tetap terbuka.

**Transisi 11 `Abort Case` sengaja tidak dijalankan** atas perintahmu (tiga transisi dulu). Konsekuensinya
tetap seperti yang sudah kulaporkan: atribut API transisi 11 juga ikut tertunda, karena hanya bisa dibaca
dari tiket yang sedang di `Pending Sub-tickets`.

**Tiga atribut `Create`(1)／`Complete`(10)／`Abort Case`(11) juga belum bertambah** — ketiganya hanya bisa
diambil dari tiket di `Pending Sub-tickets`, dan dua tiket hari ini langsung masuk terminal dari
`Pending Approval` sesuai desain tesnya.

### Sisa celah 第八区「尚未测试」 baris 1 dan 2 setelah hari ini

| Celah | Sebelum | Sekarang |
| --- | --- | --- |
| 四条终态转换实跑 | 0 dari 4 | **2 dari 4** — `Withdraw`(8) ✅ · `Cancel as Duplicate`(9) ✅ · `Reject`(3) ❌ (tiket diblok classifier) · `Abort Case`(11) ❌ (ditahan, B-15) |
| 三条转换属性 API 回读 | 0 dari 3 | **0 dari 3** — tidak bergerak, sesuai desain |

**Baris 28 建造单 belum boleh dianggap tuntas.** 判据-nya minta empat transisi terminal 实跑 dan tiga
atribut 回读; yang terpenuhi baru dua dari empat, dan nol dari tiga.

---

## Riwayat file ini

| Tanggal | Perubahan |
| --- | --- |
| 2026-09-22 | Dibuat. SSCSD-421 (`Withdraw`) dan SSCSD-422 (`Cancel as Duplicate`) dibuat dan dijalankan; changelog dan resolution dibaca balik. Tiket untuk `Reject` gagal dibuat karena classifier izin. `Abort Case` ditahan atas perintah. Satu temuan: F-007 |
