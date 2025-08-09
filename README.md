# Proyek: Pengirim Quotes WhatsApp Otomatis
 
> Proyek sederhana untuk mengirimkan quotes kritik pedas ala Timothy Ronald ke WhatsApp secara otomatis menggunakan Gemini API dan Python.
 
---
 
## Fitur
 
* **Quotes Dinamis:** Mengambil quotes yang dibuat secara real-time oleh model AI Google Gemini.
* **Pengiriman Otomatis:** Mengirim pesan WhatsApp ke nomor tujuan pada waktu yang ditentukan.
* **Fleksibel:** Dapat dijalankan di komputer lokal atau VPS (Virtual Private Server) untuk otomatisasi 24/7.
 
---
 
## Persyaratan Sistem
 
Pastikan Anda memiliki hal-hal berikut sebelum memulai:
 
1.  **Python 3.8+** terinstal di sistem Anda.
2.  **Kunci API Gemini** dari [Google AI Studio](https://aistudio.google.com/app/apikey).
3.  **WhatsApp Web** sudah login di browser Anda (jika menggunakan `pywhatkit`).
 
---
 
## Cara Menjalankan
 
Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan proyek.
 
### 1. Kloning Repositori
 
Buka terminal dan kloning repositori ini ke komputer Anda.
 
```bash
git clone https://github.com/irwancious/wa-timothy-quotes-sender.git
cd wa-timothy-quotes-sender
```
### 2. Siapkan Lingkungan Virtual
Disarankan untuk menggunakan virtual environment agar dependensi proyek tidak bercampur dengan pustaka global Anda.

```Bash
# Buat virtual environment
python -m venv venv
 
# Aktifkan virtual environment
# Di macOS/Linux:
source venv/bin/activate
# Di Windows:
venv\Scripts\activate
```
### 3. Konfigurasi Kunci API dan Nomor Tujuan
Buat file baru di dalam folder proyek bernama .env > isi dengan:
```bash
GEMINI_API_KEY="PASTE_KUNCI_API_GEMINI_ANDA_DI_SINI"
NOMOR_TUJUAN = "+6281234561890" # Ganti dengan nomor WhatsApp tujuan kamu
```
> Pastikan format nomor telepon sudah benar, termasuk kode negara. Untuk Indonesia, gunakan +62 di depan.

### 4. Instal Dependensi
Dengan virtual environment yang sudah aktif, instal semua pustaka yang dibutuhkan dari requirements.txt.
```bash
pip install -r requirements.txt
```

### 5. Jalankan Program
Anda dapat menjalankan program secara manual untuk menguji fungsinya.
```bash
python sendquotes_tr.py
```

### Menjadwalkan Pengiriman Otomatis
Untuk menjadwalkan program agar berjalan setiap jam 7 pagi (atau kapan pun), Anda bisa menggunakan cron job di Linux/macOS atau Task Scheduler di Windows/VPS.

Contoh cron job:

```bash
# Buka crontab
crontab -e
 
# Tambahkan baris ini untuk berjalan setiap jam 7 pagi
0 7 * * * /path/ke/virtual-env/bin/python /path/ke/proyek/nama_file_anda.py
```
Pastikan Anda menggunakan path absolut ke interpreter Python di dalam venv dan ke file program Anda.

---

### Kontribusi
Jika Anda memiliki ide untuk perbaikan atau fitur baru, silakan buka issue atau kirim pull request.

---

### Disclaimer
Proyek ini menggunakan pywhatkit yang mengotomatiskan WhatsApp Web menggunakan library pywhatkit (tanpa butuh WhatsApp API). Jadi cara ini lebih aman dari banned dibandingkan menggunakan WhatsApp API yang tidak resmi. Penggunaan API tidak resmi memiliki risiko pemblokiran akun. Gunakan dengan bijak.