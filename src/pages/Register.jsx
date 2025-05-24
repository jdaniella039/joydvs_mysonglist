function Register() {
  return (
    <div className="p-6 text-center">
      <h1 className="text-2xl font-bold mb-4">Register</h1>
      <form className="space-y-4 max-w-sm mx-auto">
        <input
          type="text"
          placeholder="Username"
          className="w-full p-2 border rounded"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full p-2 border rounded"
        />
        <button
          type="submit"
          className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
        >
          Daftar
        </button>
      </form>
    </div>
  );
}

export default Register;
