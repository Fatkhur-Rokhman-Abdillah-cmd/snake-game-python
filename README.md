# 🐍 Snake Classic - Pygame

Game klasik **Snake** yang dibuat dengan Python + Pygame.

## 🎮 Kontrol

| Tombol | Aksi |
|--------|------|
| `↑` / `W` | Gerak ke atas |
| `↓` / `S` | Gerak ke bawah |
| `←` / `A` | Gerak ke kiri |
| `→` / `D` | Gerak ke kanan |
| `P` | Pause / Lanjut |
| `R` | Restart |
| `ESC` | Keluar |

## 📦 Instalasi

1. Clone repository:
   ```bash
   git clone <url-repo> pygame-snake
   cd pygame-snake
   ```

2. Buat virtual environment (opsional tapi disarankan):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Menjalankan Game

```bash
python main.py
```

## 🗂️ Struktur Project

```
pygame-snake/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── settings.py
│   ├── game.py
│   ├── snake.py
│   ├── food.py
│   └── utils.py
└── assets/
    ├── sounds/
    └── images/
```

## ✨ Fitur

- Kontrol keyboard (Arrow / WASD)
- Skor bertambah setiap makan
- Kecepatan bertambah seiring skor
- Pause & Restart
- Deteksi tabrakan dinding & badan sendiri
- Grid visual

## 📝 Lisensi

MIT License - bebas digunakan untuk belajar.