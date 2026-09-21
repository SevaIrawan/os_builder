# 建造单 页首附表「建设待办／阻塞表」— status per baris setelah 2026-09-21

> Cermin dari tabel 33 baris di 页首附表 建造单 (pageId 2096463922, **v33**, dibaca live 2026-09-21 ~18:50 WIB).
> Daftar 待办 / 阻塞中 itu disusun oleh Bambang di Confluence; file ini **bukan pengganti**, hanya
> pandangan status yang dipakai untuk menyiapkan update v34. Kalau berbeda, halaman Confluence yang benar.
>
> **Cara menilai**: tiap baris diuji terhadap **解除判据 baris itu sendiri**, bukan terhadap kesan.
> Ini yang diwajibkan CLAUDE.md §一: 「开工前先扫一遍建造单阻塞行，逐条核对「解除判据」是否已成立，
> 已解封的立即恢复推进。」 Kolom "Verdict" hanya boleh berbunyi 判据成立 kalau kalimat 判据-nya
> benar-benar terpenuhi dan sumbernya dibaca hari ini.

## Ringkasan v33 → sekarang

| | v33 | Setelah 2026-09-21 |
| --- | --- | --- |
| 阻塞中 | 5 (baris 1–5) | **5** — tidak ada yang 判据-nya terpenuhi |
| 待办 (semua rasa) | 24 | **23** |
| 已解封 | 4 (baris 24, 26, 27, 28) | **5** — baris 12 menyusul |

**Satu baris benar-benar tutup hari ini: baris 12.** Delapan baris lain bergerak tanpa 判据-nya terpenuhi
(dependensinya berubah, separuh syaratnya jatuh, atau permintaannya sudah dikirim) — itu tetap ditulis,
karena "sudah dikirim" bukan "sudah beres".

## Baris yang bergerak hari ini

| # | 状态 v33 | Verdict hari ini | Apa yang berubah |
| --- | --- | --- | --- |
| **12** | 待办 | ✅ **判据成立 → 已解封 (2026-09-21)** | 判据-nya berbunyi 「确认这两个频道继续用于该团队知会，或统一改发 collab-hr-crm」 — hanya minta konfirmasi bisnis. Felix menjawabnya di **c50261 butir 4**: kedua channel dipakai terus, tidak digabung, dengan dua alasan (kepala INZ9/Marketing tidak ada di collab-hr-crm; collab-hr-crm sudah padat oleh tiga market lead). ⚠️ Kolom 依赖谁 baris ini menulis 「Felix（业务）＋Alden（登记）」, tapi 判据-nya tidak menyebut registrasi. Bagian registrasi 04.11 adalah 判据② **baris 6**, bukan baris ini. Jadi baris ini tutup tanpa menunggu Alden. |
| **5** | 阻塞中 | ❌ 判据 belum terpenuhi — **tapi dependensinya pindah orang** | 判据 minta 04.7 dua baris diisi nama dwibahasa **dan** Spec／04.7／nama tampilan platform tiga-tiganya sama. **04.7 dibaca live hari ini: v46, kedua baris S-05 tidak berubah satu huruf, nama belum diisi.** Yang berubah: Felix sudah **memberi** kedua namanya (c50261 butir 1). Keduanya lolos larangan di 判据 — tidak ada 全角「｜」 di dalamnya, dan formatnya 中文 · English dengan 半角中点 berspasi, sesuai 04.0 §五. Jadi **依赖谁 「Felix（流程 Owner）」 sudah gugur**; sisanya 回填 04.7, dan Owner 04.7 = **Alden** (04 §六, dibaca live v25 hari ini). Catatan yang belum hilang: nama Mandarin dari Felix 「提交纪律处置申请」 ≠ tulisan 04.7 v46 sekarang 「提交纪律与绩效改进处置申请」, jadi syarat "tiga-tiganya sama" belum bisa dinilai sebelum Spec dicek. |
| **1** | 阻塞中 | ❌ 判据 belum terpenuhi | 判据 minta baris 04.1 §一 berubah jadi 「已裁决｜待创建｜{key}」 atau 「运行中」 **dan** Issue Type + visibilitas terdaftar. **04.1 masih v46, tidak bergerak di sapuan mana pun** → baris itu masih 「候选｜待N5」. Yang baru hari ini: Kent **c50255** 「Build the library per N5; the 04.1 / 04.8 rows get formalized by Kayden's side」 dan **c50257** 「已让 Bambang 按 N5 建库…我会盯 N5 建库 ＋ 04.1/04.8 转正式 到闭环」. Jadi pihak yang ditunggu sekarang tegas: **orang yang ditunjuk Kayden**, dengan Kent mengawal. Tetap 阻塞中. |
| **3** | 阻塞中 | ❌ 判据 belum terpenuhi | 判据: 「平台扩展组件能力并更新 04.4.1」. **04.4.1 masih v13**, tidak bergerak. Yang baru: permintaannya sudah dikirim utuh sebagai **c50279** (2026-09-21 15:17). **Alden belum membalas** — dia bahkan belum berkomentar di OSD-116 sejak 2026-09-10. Tetap 阻塞中. |
| **6** | 待办 | ❌ 判据 belum terpenuhi — **dua dari tiga sudah jatuh** | 判据 ① bot masuk tujuh channel + baca balik daftar anggota → **terpenuhi** (pembacaan Slack kita 2026-09-21 + Felix c50261 butir 3). 判据 ③ posisi bot di `sscos-hr` harus dicek oleh yang punya akses, karena 「建造人账号非其成员」 → **premisnya sudah tidak berlaku**: Felix c50261 menulis akun kita sudah ditambahkan ke `#sscos-hr`, dan pembacaan kita menemukan `@sscos-bot` (U0BCPFHGURE) di dalamnya. Sisa: **hanya 判据② registrasi 04.11**, dan **04.11 masih v2 (2026-08-24)**, tidak muncul di sapuan mana pun. Dependensi murni **Alden**. |
| **19** | 待办（双签未表态） | ❌ 判据 belum terpenuhi — **separuhnya beres** | 判据: 「明确执行身份与模式五互斥条在本场景的适用口径」 — dua hal. **执行身份 sudah jelas**: Kayden c50244 → Kent c50257 「N28＝方向 2——转态权限配 HR Ops & Data 角色组＋守护件」. **互斥条口径belum**: c50263 kita menetapkan 04.3 §六 sudah memutuskan kasus Mode-5 secara verbatim, lalu merutekan sisa pertanyaannya ke **Kayden** sebagai Owner 04.3. Belum dijawab. |
| **32** | 待办（双签未表态） | ❌ 判据 belum terpenuhi — **tapi syarat keduanya praktis gugur** | 判据 dua bagian: 「明确 N03 走身份件还是直调 B6」 + 「若走身份件，待其转「可用」后本流程方可建 N03 身份认证段」. Bagian kedua: 身份件 **sudah active·已发布** sejak 2026-09-21 07:52Z (04.9 **v106** baris indeks baru; 04.9.1 **v19**, versionId＝activeVersionId `616bbd91`). 🔴 Tapi **04.4 §十一 masih menulis 「在建（影子·shadow）」 dan 04.4.3 masih v6 「在建·影子·inactive」** (findings F-006) — dan 04.4 §十一 justru rute yang CLAUDE.md suruh pakai untuk 共享组件. Bagian pertama masih terbuka, ditanyakan di **c50279 add-on (c)**, belum dijawab. |
| **25** | 待办（文档订正） | ❌ 判据 belum terpenuhi | 判据: 「订正 Notify 契约 §9.14」. **Notify 契约 masih v13**, tidak bergerak. Sudah disampaikan ke Alden sebagai catatan dokumentasi di badan **c50279 ①**. Menunggu Alden. |
| **29** | 待办（双签未表态） | ❌ 判据 belum terpenuhi | 判据: nilai `flow` didaftarkan ke 分派钩子已知表 lalu dibaca balik. **04.4.1 masih v13**; daftar hook di 04.9 v106 masih tiga nilai saja — offboard-n2 / grade-n2 / align-n10, **`disciplinary-n03` belum ada** (diverifikasi dari diff 04.9 hari ini). Sudah diminta di **c50279 add-on (a)**. Menunggu Alden. |
| **30** | 待办（双签未表态） | ❌ 判据 belum terpenuhi | 判据 minta 回调件 N07 「先认领后动作」 + uji negatif. Komponennya belum ada — terkunci baris 3. Dua hal baru: (i) kalimat terakhir kolom 事项 baris ini **salah kutip** dan sudah masuk daftar v34 sebagai butir 8 (轮次防过期 = 「🔲 待定」, bukan 「未实现」); (ii) **c50279 (b)** meminta Alden menambahkan S-05 ke kolom 「被哪些 workflow 引用」 tabel kartu bersama. |
| **13** | 待办 | ❌ 判据 belum terpenuhi | 判据 minta mode tes mengalihkan kiriman ke whitelist + membawa penanda tes 04.5.3 §三 — **pekerjaan build kita, belum dikerjakan**. Fakta baru: Felix c50261 menulis akun kita sudah ditambahkan ke `#sscos-hr` untuk testing dan minta dikabari agar aksesnya dicabut. Itu **menambah utang kita**, tidak mengurangi 判据. |

## Baris yang TIDAK bergerak hari ini

Dicek, tidak ada perubahan pada 判据 maupun dependensinya:

**2** (NTP 岗位受控清单, 阻塞中 · Alden+Felix) · **4** (邮件收信件, 阻塞中 · Alden) · **7** (N09 附件回贴) ·
**8** (离职 Spec 接收入口 · Kent+Geri) · **9** (S-06/S-15 Spec belum dirancang · Felix) ·
**10** (测试档案 NTP · Kent) · **11** (部门值→Team Project 对照表 · sisi kita) · **14** (主单专属 Screen) ·
**15** (dua 提点 Kayden belum dijawab Felix) · **16** (WFH 规章 · Felix) · **17** (请求级整单时限 · Felix) ·
**18** (形状 C「已改道」出口) · **20** (Resolution 值 · Alden) · **21** (JSM SLA) · **22** (dua scheme id) ·
**23** (主体标识 marker 跨流程) · **31** (belum terdaftar sebagai konsumen B6/NTP · Alden) ·
**33** (nama Issue Type 主单 tidak konsisten).

Catatan baris **14**: Kent c50234 #2 menyatakan 「the Screen (Disciplinary Case inherits the SSCSD default)
→ Alden / V1 domain」 — itu menetapkan **siapa pemiliknya**, bukan menjawab 判据① yang menanyakan
**di mana objek kelas Screen didaftarkan** (07.06.1 §六-4 tidak punya entri untuk itu). Jadi belum bergerak.

Catatan baris **18**: kolom 依赖谁-nya menulis 「Alden（04.3 Owner）」 — **salah**, Owner 04.3 adalah
Kayden Lee. Sudah masuk daftar v34 sebagai butir 5.

## Hubungan dengan daftar v34

`docs/pending-buildsheet-updates.md` **dihapus 2026-09-21** atas permintaan pemilik repo; daftar v34 akan
disusun ulang dari awal. Isi lamanya (16 butir) tetap ada di riwayat git pada commit `24f3013` kalau
sewaktu-waktu perlu dilihat lagi. File ini hanya pandangan status per baris, bukan teks yang akan ditulis
ke Confluence.
