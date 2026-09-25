# Verifikasi ulang isi empat kiriman — poin 7 audit 2026-09-25

> Atas perintah Bambang 2026-09-25: 「kau selesaikan point 7 dan 8 sekarang」.
> Poin 7 = cek ulang isi W-2026-09-23-05, W-2026-09-23-06, W-2026-09-24-04, W-2026-09-24-05
> terhadap sumber yang dibaca **sampai habis**. Tidak ada yang dikirim atau diubah di luar repo.

## Kenapa perlu

Di keempat kiriman ini, sebagian sumber tidak pernah terbaca sampai habis sebelum dikirim
(temuan 8 audit). Gate lama meloloskannya karena kutipannya memang ada di sumber, tapi
isi di luar kutipan — yang bisa membantah atau mempersempit klaim — tidak dibaca.

## Cara

- Sumber yang dicek adalah **salinan persis yang dipakai saat menulis** (hasil baca yang tersimpan
  di transkrip), bukan versi sekarang. Jadi pertanyaannya: *benarkah kalimat itu terhadap sumbernya
  pada saat dikirim.*
- Salinan yang sama persis tidak dibaca dua kali (dicek per hash / per isi komentar):
  - Spec v67 yang dipakai W-24-04 dan W-24-05 = Spec v67 yang saya baca penuh 2026-09-25
    (hash `3c5b804619` sama) → 4 klaim saya cek sendiri.
  - OSD-116 halaman 1 dipakai ketiga kiriman, isinya identik (hash `d27db367e6`).
  - OSD-116 halaman 2 versi 09-23 (75 komentar) = 75 komentar pertama versi 09-24, isi sama.
  - NSE-1137 halaman 3 versi 13:41 (56 komentar) = 56 komentar pertama versi 14:49, isi sama.
- Tujuh salinan dibaca penuh oleh tujuh agen pembaca, masing-masing melaporkan rentang karakter
  yang dibaca (semuanya 0 sampai akhir, tanpa celah):

| Salinan | Panjang (karakter) | Klaim yang bergantung |
|---|---|---|
| Spec S-05 v62 (09-23 13:37) | 71.353 | 12 (W-23-05, W-23-06) |
| Build sheet v43 (09-24 14:49) | 73.586 | 16 (W-24-05) |
| OSD-116 komentar c48791–c49731 | 169.502 | 11 |
| OSD-116 komentar c49740–c50496 | 90.127 | 11 |
| NSE-1137 komentar c48129–c49112 | 175.300 | 10 |
| NSE-1137 komentar c49118–c49938 | 135.559 | 10 |
| NSE-1137 komentar c49940–c50501 | 78.000 | 10 |

- Setiap temuan agen yang dipakai di bawah **saya cek ulang sendiri** langsung ke teks
  (kutipan dihitung persis ada di sumber). Satu penilaian agen saya koreksi (K4, lihat bawah).

## Hasil per kiriman

### W-2026-09-23-05 dan W-2026-09-23-06 (Slack #nos-bo, Indonesia dan Inggris)

| Klaim | Hasil | Catatan |
|---|---|---|
| K1／EK1 「N03 — submit S-05 sendiri」 | Benar | Baris N03 Spec v62 |
| K2／EK2 「HR masih boleh gantiin kalau atasan absen」 | Benar untuk N03, kurang tepat istilahnya | Spec menyebut **HR Ops & Data**, bukan HR umum: 「缺位由HR Ops & Data代为受理」. Kutipan dasar di pesan yang sama sudah memuat istilah yang benar |
| K3／EK3 kutipan dasar | Benar, kata per kata | Terjemahan Inggris 「receives it on their behalf」 untuk 代为受理 lebih lemah dari maksud Spec (「代为受理提交」, 「代提交」 = mengajukan atas nama) |
| K4／EK4 「Sudah ditanyakan ke Alden di c50279」 | Benar | c50279 menanyakan jalur N03, termasuk 「For the 缺位 path (submitter = HR Ops & Data, not the Direct Supervisor)」 dan 「明确 N03 走身份件还是直调 B6」. Agen pembaca sempat ragu karena c50279 mengecualikan soal kode error B6 mana yang dihitung 缺位 — itu hal lain, bukan yang diklaim |
| K5／EK5 「N16」 | Benar | — |
| **K6／EK6 「N17 turut sama — HR ambil alih penuh pas Check-in PIP」** | **Tidak tepat** | Check-in ada di **N16**, bukan N17. Di N16 HR Ops & Data mengambil alih hanya kalau atasan 缺位 (「Direct Supervisor（缺位→HR Ops & Data承接）」); dalam keadaan normal 「HR不担任本子单Owner，监督经C-10频率提醒及D表知会承担」. Untuk N17 yang dialihkan hanya masukan atasan (「Direct Supervisor（缺位→已承接的HR Ops & Data）提出提前终止建议」); pemilik N17 memang selalu HR Ops & Data, dan notifikasi hasil N17 ke atasan 「缺位不替代发送」. Kutipan dasar di pesan hanya dari baris N16, jadi tidak membuktikan bagian N17 |
| K7／EK7 kutipan dasar baris N16 | Benar, kata per kata | — |

Catatan waktu: aturan pengambilalihan saat atasan 缺位 **dicabut sehari kemudian**
(Kayden c50461, 2026-09-24; Spec v67). Isi kedua pesan ini sekarang menggambarkan aturan yang
sudah tidak berlaku. Apakah sesudahnya ada koreksi di thread Slack itu **belum saya cek**.

### W-2026-09-24-04 (komentar NSE-1137 c50501)

| Klaim | Hasil | Catatan |
|---|---|---|
| K6 `created:false` + `issueKey` = sukses | Benar | Geri c50494: 「that is a success, not a failure; do not retry on it」 |
| K12 cocok dengan NTP fallback yang ditawarkan Geri | Benar, dengan satu hal yang tidak disebut | c50494 menawarkan NTP sebagai cadangan, tapi Geri lebih suka nama dikirim: 「passing it is cheaper and avoids a lookup that can fail」. Pesan kita menjelaskan kenapa tidak (kontrak milik Kent) |
| K10 kontrak Kent 「S-05 triggers resignation」 | Benar | Kent c50381: 「Trigger link 10075, S-05 triggers resignation, main-to-main」 — ini ringkasan Kent di bawah judul kontrak, bukan teks Spec 离职 |
| K11 nama karyawan dari NTP (Spec N20) | Benar | Spec v67 baris N20 |
| **Kalimat di c50501 yang tidak ada sumbernya** | **Asumsi** | 「N20 stops unless the entry returns ok:true with an issueKey」. c50494 dan c50387 tidak menyebut nilai `ok` saat pengaman duplikat kena. Kalau saat itu entry mengembalikan `ok:false`, N20 akan memperlakukan duplikat yang sebenarnya sukses sebagai gagal. Perlu ditanyakan ke Geri (C-16) |

### W-2026-09-24-05 (build sheet v43 → v44)

| Klaim | Hasil | Catatan |
|---|---|---|
| K18, K22, K38, K46, K57, K59 (dari NSE-1137) | Benar | Geri c50494／c50495. Nama baris 「员工离职 Spec 系统触发接收入口」 di K57 memang nama baris di tabel atas build sheet v43 |
| K20, K47 (upstreamSource ditanyakan ke Geri) | Benar | Hanya mencatat bahwa kita bertanya di c50501; belum ada jawaban Geri sampai c50501 |
| K41, K42, K43 (Kayden c50445) | Benar, kata per kata | — |
| K50 「Kent 契约原文」 | Benar, istilahnya agak berlebih | Itu ringkasan Kent di c50381, bukan teks kontrak di Spec 离职 |
| K61 (Kent c50472) | Benar, kata per kata | — |
| K62 (Kayden mencabut satu kalimat) | Benar terhadap c50461, tapi menyempitkan | c50461 mencabut seluruh mekanisme: 「不设代提或承接机制，缺位一律视为档案问题，拦住并告警」, bukan hanya satu kalimat |
| K63 (Felix c50486, Spec v67) | Benar, kata per kata | Kalimat yang sama di c50486 juga menulis 「本轮修订按建设期注记处理，不重走结构审计」 — terkait C-15 |
| **K64 「本页凡引用旧缺位处理逻辑者，以 Spec v67 为准」** | **Tidak ada sumbernya** | Ini aturan buatan kita sendiri. Tidak ada komentar yang menyatakannya, dan status v67 terhadap audit struktur belum dikonfirmasi Kayden (C-15) |
| **K29 status 「已建·inactive」 untuk N20** | **Berlebih terhadap aturan** | N20 memang ada di n8n dan inactive, tapi 04.9 §一: 「三位一体…缺任一项视为未完成」 — N20 belum terdaftar di 04.9, jadi menurut aturan belum 「已建」 |
| K25 「marker 已改为…」 | Isinya benar, sumber di ledger salah tunjuk | Perubahan marker berasal dari update N20 di n8n, bukan dari build sheet |
| K28, K31, K33, K35, K40, K55, K56, K60 | Benar | K60 「已不适用」 didukung Kent c50472 (kalimat berikutnya, K61) |
| K4, K5, K8, K10, K13 | Benar | Tanggal 2026-09-24 adalah tanggal tulis, bukan klaim dari sumber |
| K52, K53, K54 (Spec v67) | Benar | Baris N20 dan tabel A 「离职单关联状态」 |

## Ringkasan

- **Tidak ada klaim yang terbukti salah total.**
- **Tidak tepat:** K6／EK6 di dua pesan Slack (N17 dan Check-in).
- **Tanpa sumber:** K64 di build sheet (「以 Spec v67 为准」), dan satu kalimat di c50501 (nilai `ok`).
- **Berlebih:** K29 (「已建」 padahal belum terdaftar di 04.9), K62 (menyempitkan), K50 (istilah).
- **Kurang tepat istilah／terjemahan:** K2 (HR vs HR Ops & Data), EK3.
- **Sudah tidak berlaku:** isi kedua pesan Slack 09-23, karena aturan 缺位 dicabut 09-24.

Tindak lanjutnya dicatat di `docs/action-list.md` baris **C-16**. Tidak ada yang dikirim.

## Batas verifikasi ini

- Pembacaan penuh ketujuh salinan dikerjakan agen pembaca. Laporan cakupan mereka menyatakan
  0 sampai akhir tanpa celah. Temuan yang dipakai di sini saya cocokkan sendiri ke teks.
- Gate G-01 (C5) menghitung "sudah dibaca" hanya dari cetakan di percakapan utama. Verifikasi
  ini tidak mengubah status gate untuk kiriman lama; tujuannya memeriksa isi.
- Klaim yang sumbernya sejak awal dibaca penuh (bacaan n8n, 07.06.1, Spec 离职) tidak diulang di sini.
