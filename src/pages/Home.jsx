import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Home() {
  const { user } = useAuth();

  return (
    <div className="p-8 max-w-4xl mx-auto text-center">
      <h1 className="text-4xl sm:text-5xl font-bold text-purple-700 mb-4">
        🎵 Selamat datang di MySongList
      </h1>
      <p className="text-lg text-gray-600 mb-8">
        Aplikasi pribadi untuk menyimpan, mengelola, dan menikmati daftar lagu favoritmu!
      </p>

      {/* Kartu fitur yang bisa diklik */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 text-left text-gray-700 mb-10">
        <Link
          to="/songs"
          className="bg-purple-50 p-4 rounded shadow hover:shadow-md transition block"
        >
          <h2 className="font-semibold text-lg mb-2">🎧 Tambah Lagu</h2>
          <p>Masukkan judul dan artis lagu favoritmu dengan mudah.</p>
        </Link>

        <Link
          to="/songs"
          className="bg-purple-50 p-4 rounded shadow hover:shadow-md transition block"
        >
          <h2 className="font-semibold text-lg mb-2">📝 Edit & Hapus</h2>
          <p>Kelola lagu yang sudah kamu simpan sesuai keinginanmu.</p>
        </Link>

        <div className="bg-purple-50 p-4 rounded shadow hover:shadow-md transition">
          <h2 className="font-semibold text-lg mb-2">💾 Disimpan Lokal</h2>
          <p>Semua data tersimpan aman di browser lewat localStorage.</p>
        </div>
      </div>

      {/* Tombol navigasi bawah */}
      {user ? (
        <Link
          to="/songs"
          className="inline-block bg-purple-700 text-white px-6 py-3 rounded-lg font-semibold hover:bg-purple-800 transition"
        >
          🎶 Buka Daftar Lagu
        </Link>
      ) : (
        <div className="space-x-4">
          <Link
            to="/login"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Login
          </Link>
          <Link
            to="/register"
            className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
          >
            Register
          </Link>
        </div>
      )}
    </div>
  );
}

export default Home;
