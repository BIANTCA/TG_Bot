# 🤖 TG_Bot (v1.0.0)

**Bot Telegram Pribadi**  
Hanya untuk penggunaan pribadi dengan fitur utama menerima dan mengelola **video** dan **foto** dari pengguna. Bot ini juga dapat melakukan perintah khusus oleh pemilik (owner).

---

## 🧩 Fitur Utama

- ✅ Menerima dan menyimpan **video** dari pengguna
- ✅ Menerima dan menyimpan **foto**
- ✅ Memungkinkan owner mengendalikan bot via command
- ✅ Dukungan sistem post otomatis ke channel
- ✅ Logging aktivitas dan perintah

---

## 🔐 File Konfigurasi
Semua konfigurasi disimpan di `setting.json`  
Contoh:
```json
{
 "version": "1.0.0",
 "bot": {
  "api": "TOKEN_BOT_ANDA",
  "code" : "0"
 },
 "channel": {
  "id": "@channel_username"
 },
 "owner": [111111111]
}


---

📜 Perintah (Command)

/start

Memulai interaksi dengan bot.

Jika terdapat parameter, akan digunakan untuk mengambil video terkait.

Digunakan untuk mendownload video via link dari channel.


/stopbot (Hanya untuk owner)

Menghentikan bot secara langsung dan keluar dari polling.

Berguna untuk mematikan bot secara manual.


/send_message <chat_id> <pesan> (Hanya untuk owner)

Mengirim pesan manual dari bot ke chat_id tertentu.

Contoh: /send_message 123456789 Halo ini pesan dari bot


/post (Hanya untuk owner)

Melakukan post otomatis video+thumbnail ke channel yang telah diatur.

Video, thumbnail dan caption diambil secara acak dari daftar file.



---

🛠 Struktur Direktori

.
├── main.py
├── setting.json
├── function/
│   ├── tools.py
│   └── video.py
├── documents/
│   ├── video.json
│   ├── videoList.json
│   ├── thumbnail.json
│   ├── tittle.json
│   └── logging/
│       └── *.log


---

🚀 Jalankan Bot

python main.py

Pastikan sudah:

Menginstall dependensi pyTelegramBotAPI

Memasukkan token bot dan owner ID di setting.json



---

📌 Catatan

Bot ini masih dalam pengembangan awal (v1.0.0). Fitur keamanan dan validasi akan ditambahkan di versi selanjutnya.

---

Kalau kamu butuh versi markdown

