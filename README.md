# 🎵 MySongList – Aplikasi Manajemen Daftar Lagu

## 📝 Deskripsi Aplikasi Web
**MySongList** adalah aplikasi web yang memungkinkan pengguna untuk:
- Mendaftarkan akun dan login
- Menambahkan lagu favorit ke daftar pribadi
- Melihat daftar lagu yang telah ditambahkan
- Menghapus lagu dari daftar

Aplikasi ini dibangun sebagai bagian dari Tugas Besar Pemrograman Web dengan arsitektur fullstack: backend menggunakan **Python Pyramid** dan frontend menggunakan **React.js**.

## 📦 Dependensi Paket (Library)
Berikut adalah dependensi utama yang digunakan dalam aplikasi ini:

### Backend (Python + Pyramid)
- `pyramid`
- `pyramid_jwt`
- `passlib`
- `sqlalchemy`
- `psycopg2-binary`
- `waitress`

### Frontend (React)
- `react`
- `react-dom`
- `react-router-dom`
- `axios`
- `tailwindcss`

> Semua dependensi lengkap dapat dilihat di file `requirements.txt` (backend) dan `package.json` (frontend).

## ⚙️ Fitur pada Aplikasi
- 🔐 **Register dan Login User** dengan sistem token JWT
- 📄 **CRUD Lagu**: Tambah, lihat, dan hapus lagu dalam daftar
- ✅ **Proteksi endpoint** (hanya user login yang bisa akses daftar lagu)
- 🔎 **Pencarian Lagu** berdasarkan judul atau artis (opsional jika sudah)
- 🎨 **Tampilan Responsif** dengan React dan Tailwind CSS

## 📚 Referensi
- Dokumentasi Pyramid Framework: https://docs.pylonsproject.org/projects/pyramid/en/latest/
- React Documentation: https://reactjs.org/docs/getting-started.html
- Tailwind CSS: https://tailwindcss.com/docs/installation
- JWT Auth: https://github.com/vallettea/pyramid_jwt
