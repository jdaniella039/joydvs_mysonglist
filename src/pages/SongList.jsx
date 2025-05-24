import { useState, useEffect } from "react";

function SongList() {
  const [songs, setSongs] = useState(() => {
    const saved = localStorage.getItem("songs");
    return saved ? JSON.parse(saved) : [];
  });

  const [title, setTitle] = useState("");
  const [artist, setArtist] = useState("");
  const [editId, setEditId] = useState(null);

  useEffect(() => {
    localStorage.setItem("songs", JSON.stringify(songs));
  }, [songs]);

  const resetForm = () => {
    setTitle("");
    setArtist("");
    setEditId(null);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title || !artist) return;

    if (editId !== null) {
      setSongs(
        songs.map((s) =>
          s.id === editId ? { ...s, title, artist } : s
        )
      );
    } else {
      const newSong = {
        id: Date.now(),
        title,
        artist,
        favorite: false, // tambahan
      };
      setSongs([...songs, newSong]);
    }

    resetForm();
  };

  const handleEdit = (song) => {
    setTitle(song.title);
    setArtist(song.artist);
    setEditId(song.id);
  };

  const handleDelete = (id) => {
    setSongs(songs.filter((s) => s.id !== id));
    if (editId === id) resetForm();
  };

  const toggleFavorite = (id) => {
    setSongs(
      songs.map((s) =>
        s.id === id ? { ...s, favorite: !s.favorite } : s
      )
    );
  };

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold text-purple-700 mb-6">🎶 Daftar Lagu</h1>

      <form onSubmit={handleSubmit} className="mb-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
        <input
          type="text"
          placeholder="Judul Lagu"
          className="p-2 border rounded"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="text"
          placeholder="Nama Artis"
          className="p-2 border rounded"
          value={artist}
          onChange={(e) => setArtist(e.target.value)}
        />
        <button
          type="submit"
          className={`text-white rounded p-2 ${
            editId !== null
              ? "bg-yellow-500 hover:bg-yellow-600"
              : "bg-green-600 hover:bg-green-700"
          }`}
        >
          {editId !== null ? "Update" : "Tambah"}
        </button>
      </form>

      {songs.length === 0 ? (
        <p className="text-center text-gray-500">Belum ada lagu ditambahkan.</p>
      ) : (
        <ul className="space-y-3">
          {songs.map((song) => (
            <li
              key={song.id}
              className="border p-4 rounded flex justify-between items-center"
            >
              <div>
                <h2 className="font-semibold flex items-center gap-2">
                  {song.title}
                  {song.favorite && <span title="Favorit">⭐</span>}
                </h2>
                <p className="text-sm text-gray-600">{song.artist}</p>
              </div>
              <div className="space-x-2 flex">
                <button
                  onClick={() => toggleFavorite(song.id)}
                  className={`px-3 py-1 rounded ${
                    song.favorite
                      ? "bg-yellow-400 text-white hover:bg-yellow-500"
                      : "bg-gray-300 text-gray-800 hover:bg-gray-400"
                  }`}
                >
                  {song.favorite ? "Favorit" : "☆"}
                </button>
                <button
                  onClick={() => handleEdit(song)}
                  className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(song.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                >
                  Hapus
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default SongList;
