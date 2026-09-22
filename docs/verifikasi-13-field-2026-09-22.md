# Verifikasi API 13 field S-05 (c50345) — 2026-09-22

Dasar: Kent c50345 (14:24) 「13 fields built and registered in 04.10 §三 (v20) … All fields API-readback
verified (createmeta 2026-09-22)」. Aturan 04.10 §2 / 建造单 butir 14 menuntut **API 回读 sebelum 登记**.
Berikut回读 dari sisi建造侧, lewat konektor Rovo (akun Backend Operations).

## 1 · HR × Sub-ticket 14316 — 13/13 ADA, tipe & nilai cocok

| # | Kent | Jira `fieldId` | Nama di Jira | Tipe live | Nilai option live |
|---|---|---|---|---|---|
| 1 | Show Cause Extension Count | `customfield_18243` | Show Cause Extension Count | number (float) | — |
| 2 | Show Cause Explanation Result | `customfield_18252` | Show Cause Explanation Result | option | **成立**(15918) / **不成立**(15919) |
| 3 | Warning Effective Date | `customfield_18244` | Warning Effective Date | date (datepicker) | — |
| 4 | Check-in Record | `customfield_18256` | Check-in Record | textarea | — |
| 5a | Outstanding Items | `customfield_18248` | **PIP** Outstanding Items | textarea | — |
| 5b | Current Gap | `customfield_18249` | **PIP** Current Gap | textarea | — |
| 5c | Extension Goals | `customfield_18250` | **PIP** Extension Goals | textarea | — |
| 5d | Extension Period | `customfield_18253` | **PIP** Extension Period | option | **15 天**(15920) / **30 天**(15921) / **60 天**(15922) / **90 天**(15923) |
| 5e | New Due Date | `customfield_18245` | **PIP** New Due Date | date | — |
| 5f | Check-in Schedule | `customfield_18251` | **PIP** Check-in Schedule | **textfield (single-line)** | — |
| 6 | PIP Result | `customfield_18254` | PIP Result | option | **Completed**(15924) / **Extension**(15925) / **Failed**(15926) |
| 7 | Assessment Basis Type | `customfield_18255` | Assessment Basis Type | option | **纪律违规**(15927) / **PIP未改善**(15928) |
| 8 | Joint Review Result | `customfield_18257` | Joint Review Result | option | **通过**(15929) / **不通过**(15930) |

Project HR = id **13260** (`HR Execution`). Issue type 14316 `Sub-ticket`, `subtask: false`, hierarchyLevel 0
— konsisten dengan 技术签 c49696 「子单＝Sub-ticket 类型…认 link 不认 subtask」.

**Seluruh nilai option cocok verbatim** dengan yang ditulis Kent dan dengan Spec (#7 逐字对齐离职流 辞退原因).

## 2 · HR × Task 10004 — 13/13 juga ada

`cf18257` Joint Review Result ada dengan 通过／不通过 — sesuai carrier N25 yang disebut Kent.
Ketiga belas field lainnya juga terpasang di 屏 Task ini.

**Catatan konteks yang memperkuat klaim「HR-specific context」**: di Task 10004, `cf18152` Grade Assessment
Result dan `cf18153` New Grade balik `allowedValues: []` (konteks option-nya tidak mencakup Task), sedangkan
kelima field option S-05 tetap membawa nilainya. Jadi konteks S-05 memang mencakup dua issue type ini.

## 3 · Check-in Record (`cf18256`) di 7 department project — 3 terverifikasi, 4 TIDAK BISA dicek

| Project | Hasil |
|---|---|
| **HR** (13260) | ✅ `cf18256` ada, textarea |
| **BO** (13263) | ✅ ada |
| **FIN** (13264) | ✅ ada |
| CRM | ⛔ `You cannot create issues in this project.` |
| FOZ | ⛔ sama |
| WP | ⛔ sama |
| XLP | ⛔ sama |

**Probe pembanding (07.06.1 E16 — wajib, tidak boleh menyimpulkan dari galat tunggal):**
`getVisibleJiraProjects(action=create)` balik **8 project**: BO · FIN · FTL · GPM · HR · NTP · SSCSD · TCL.
**CRM／FOZ／WP／XLP tidak ada di daftar.** Jadi keempat galat itu **izin create di level project**, bukan
bukti field tidak terpasang. `createmeta` memang menuntut izin create.

**Kesimpulan yang boleh ditulis**: klaim Kent「mounted on ALL 7 department Sub-ticket screens」 **terbukti 3
dari 7 dari sisi ini, dan tidak terbantah pada 4 sisanya** — bukan「tidak terpasang」, melainkan **di luar
jangkauan verifikasi akun ini**. Kalau butuh bukti 7/7, harus dari Schema Owner (Kent) atau akun yang punya
izin create di empat project itu.

## 4 · Dua selisih kecil antara c50345 dan Jira (bukan kesalahan, perlu dicatat apa adanya)

1. **Nama**: enam field PIP di Jira berawalan `PIP ` (PIP Outstanding Items / PIP Current Gap / PIP Extension
   Goals / PIP Extension Period / PIP New Due Date / PIP Check-in Schedule). c50345 menulis nama pendeknya.
2. **Carrier #8**: c50345 menulis carrier `cf18257` = HR Task 10004. Live-nya **juga terpasang di
   Sub-ticket 14316**. Lebih luas, bukan bertentangan.
3. **Tipe #5f**: `cf18251` adalah **textfield single-line**, sesuai usulan Bambang c50283
   (「Check-in 安排 (single-line)」), bukan textarea.

## 5 · Status

Syarat 「字段建成＋API 回读」 **terpenuhi untuk 13 field pada carrier HR (Sub-ticket 14316 ＋ Task 10004)**.
Siap ditulis ke 建造单 dalam satu versi begitu diperintahkan, dengan batas verifikasi §3 ditulis apa adanya.
