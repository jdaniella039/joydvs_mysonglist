# 🎵 MySongList 🎧  
_Aplikasi Web Catatan Lagu Favorit_

![mysonglist-banner](https://img.freepik.com/premium-vector/music-note-icon-flat-vector-illustration_585024-17.jpg?w=996) <!-- Ganti dengan gambar banner sendiri kalau ada -->

---

## 📌 Deskripsi Singkat

**MySongList** adalah aplikasi web sederhana untuk mencatat daftar lagu favorit. Aplikasi ini dirancang menggunakan arsitektur fullstack dengan backend **Python Pyramid + PostgreSQL**, dan frontend **React.js**.

---

## 🚀 Fitur Aplikasi

✅ Autentikasi pengguna (Register & Login dengan JWT)  
✅ Tambah lagu (judul dan artis)  
✅ Lihat daftar lagu milik user  
✅ Hapus lagu dari daftar  

> Semua data bersifat personal per user dan aman karena dilindungi oleh sistem token JWT.

---

## 📦 Dependensi Utama

### 🔧 Backend - Python (Pyramid)
- `pyramid`
- `pyramid_jwt`
- `sqlalchemy`
- `passlib`
- `jwt`
- `waitress`
- `psycopg2-binary`

### 🎨 Frontend - React
- `react`
- `react-router-dom`
- `axios`
- `tailwindcss`

---

## 🧪 Cara Menjalankan Aplikasi

### 🔙 Backend
```bash
cd mysonglist-backend
python -m venv env
source env/bin/activate # atau .\env\Scripts\activate di Windows
pip install -e .
pserve development.ini --reload
