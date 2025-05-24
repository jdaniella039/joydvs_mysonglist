# 📑 MySongList API Documentation

## 🧑‍💻 Auth Endpoints

### 🔐 Register
- `POST /api/register`
- Body:
```json
{
  "username": "yourname",
  "password": "yourpassword"
}
```

### 🔐 Login
- `POST /api/login`
- Body:
```json
{
  "username": "yourname",
  "password": "yourpassword"
}
```
- Response:
```json
{
  "token": "<jwt_token>"
}
```

## 🎵 Songs Endpoints (Protected by JWT)

**Authorization header required:**  
`Authorization: Bearer <token>`

### 📄 Get all songs
- `GET /api/songs`

### ➕ Add song
- `POST /api/songs`
- Body:
```json
{
  "title": "Song Title",
  "artist": "Artist Name",
  "favorite": true
}
```

### ✏️ Update song
- `PUT /api/songs/{id}`
- Body: same as POST

### ❌ Delete song
- `DELETE /api/songs/{id}`
