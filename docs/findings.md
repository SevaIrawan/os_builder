# Catatan Temuan (Findings Log)

> **Sifat**：catatan internal repo. **Bukan dokumen resmi, bukan standar, tidak punya
> kewenangan apa pun.** Isinya tidak boleh dipakai sebagai dasar konfigurasi atau
> keputusan; dasar kerja tetap halaman Confluence yang berlaku saat itu.
>
> **Aturan pencatatan**：
> 1. Temuan **dicatat di sini saja**. Tidak mengedit halaman Confluence, tidak mengirim
>    ke Slack／Jira／siapa pun, tanpa perintah eksplisit pemilik repo.
> 2. Catatan ini **tidak menentukan** temuan itu urusan siapa, harus naik ke mana, atau
>    perlu ditindak atau tidak. Itu di luar wewenang repo ini.
> 3. Setiap temuan wajib menyebut halaman yang **benar-benar dibuka** (pageId +
>    lastModified saat dibaca), supaya bisa dicek ulang kapan pun.
> 4. Append-only. Entri lama tidak dihapus atau ditulis ulang; kalau keadaan berubah,
>    tambah baris di kolom Status.

---

## F-001 · 2026-09-20 · 04.11 tidak terdaftar di peta subpage halaman 04

**Status**：dicatat. Belum dilaporkan ke siapa pun. Belum ditindak.

**Ditemukan saat**：menjalankan skill `nosm-sync-check` (verifikasi salinan lokal lawan
sumber Confluence). Temuan ini **di luar lingkup skill tersebut** — skill-nya hanya
membandingkan salinan lokal dengan sumbernya, bukan memeriksa kecocokan antar halaman
sumber. Tercatat di sini sebagai arsip, bukan sebagai hasil kerja skill.

**Halaman yang benar-benar dibuka dan dibaca**：

| pageId | Halaman | lastModified saat dibaca |
| --- | --- | --- |
| 1676804100 | 04｜流程建设与执行治理总纲 | Sep 05, 2026 |
| 1730347066 | 07.06｜建设指南 | Sep 15, 2026 |
| 1764524046 | 04.11｜Slack Channel 登记表 | Aug 24, 2026 |
| 1704362028 | 07｜指南 | Sep 14, 2026 |

**Fakta yang tercatat**：

1. 07.06 §三 langkah 3 menyuruh mencocokkan Channel ID ke
   「04.11｜Slack Channel 登记表（pageId 1764524046，按 Channel ID 查对，频道名仅辅助）」.
2. 07.06 §三 归口表 menyebut 04.11 sekali lagi, pada baris
   「登记表某一行错了（04.7／04.8／04.9／04.11）」.
3. Halaman 04 §六「04 子页地图」berakhir di baris 04.10 — **tidak ada baris 04.11**.
   Halaman 04 §五「登记集」juga tidak memuat baris pemicu untuk mapping
   「领域→Slack Channel」.
4. Halaman 04 §九 berbunyi：「子页新增、废弃、改名、权威边界改变或跨页结构重排时，
   必须同步核对本页路由与全部指针」。04.11 menurut halamannya sendiri dibuat 2026-08;
   sampai versi 04 yang dibaca (Sep 05, 2026) belum terlihat di tabel routing.
5. Halaman 04.11 mencatat sendiri：「本页为 2026-08 新设，与旧编号 04.11（今 04.10｜
   Jira 共享配置登记表与变更治理）无关」— nomor 04.11 pernah dipakai halaman lain.

**Kenapa dicatat, bukan ditindak**：

- Baris 04.11 **tidak ditambahkan** ke `docs/04-anchor-navigation.md`. File itu cermin
  tabel halaman 04; menambah baris yang tidak ada di sumber sama dengan mengarang
  standar, dan itu dilarang eksplisit di `CLAUDE.md` §一.
- Halaman Confluence tidak disentuh sama sekali — hanya dibaca.
- Tidak ada yang dikirim ke Slack, Jira, atau pihak mana pun.

**Catatan keadaan saat dicatat**：tidak ada pekerjaan pembangunan yang sedang berjalan,
jadi tidak ada yang terhambat oleh temuan ini.

---

## Riwayat sync-check

| Tanggal | Sumber yang dibandingkan | Hasil |
| --- | --- | --- |
| 2026-09-20 | 07.06 §八 (1730347066, Sep 15 2026) vs `CLAUDE.md` §一 | Sama persis, tidak ada perubahan |
| 2026-09-20 | 04 §一/§五/§六 (1676804100, Sep 05 2026) vs `docs/04-anchor-navigation.md` | 3 frasa hilang saat penyalinan, dikembalikan sesuai sumber (commit `a15c1b3`) |
