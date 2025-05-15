import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="bg-purple-700 text-white px-4 py-3 flex justify-between items-center">
      <h1 className="text-xl font-bold flex items-center gap-2">
        <span role="img" aria-label="music">🎵</span> MySongList
      </h1>
      <ul className="flex gap-4 items-center">
        <li><Link to="/" className="hover:underline">Home</Link></li>
        {user && <li><Link to="/songs" className="hover:underline">Lagu</Link></li>}
        {!user ? (
          <>
            <li><Link to="/login" className="hover:underline">Login</Link></li>
            <li><Link to="/register" className="hover:underline">Register</Link></li>
          </>
        ) : (
          <>
            <li className="text-sm text-white">Hello, {user.username}</li>
            <li>
              <button
                onClick={logout}
                className="bg-red-500 px-3 py-1 rounded hover:bg-red-600"
              >
                Logout
              </button>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
