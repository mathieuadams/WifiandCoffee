# ☕️ Coffee & Wifi 💻

A Flask web app to collect and display cafes with power sockets, wifi, and good coffee – perfect for remote work!

## 🚀 Features

- Add a new cafe with location, image, amenities, and coffee price
- View all submitted cafes with icons for:
  - Wifi
  - Power sockets
  - Toilets
  - Call-friendly zones
- Delete a cafe from the database
- Fully responsive Bootstrap UI

## 📸 Preview

![image](https://github.com/user-attachments/assets/f7ee1b24-2560-417b-92e2-1d98705a661a)
![image](https://github.com/user-attachments/assets/21b968a1-b223-4b36-8360-e5ffd65aed56)


## 🛠 Tech Stack

- Python
- Flask
- SQLite (via SQLAlchemy)
- Flask-WTF + WTForms
- Bootstrap 5 (via Flask-Bootstrap)
- Jinja2 Templates

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/cafe-wifi-app.git
   cd cafe-wifi-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python main.py
   ```

5. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser

---

## 🗃 File Structure

```
├── main.py               # Main Flask application
├── cafes.db              # SQLite database
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── cafes.html
│   └── add.html
├── static/
│   ├── styles.css
│   ├── wifi.png, nowifi.png, plug.png, etc.
├── requirements.txt
└── README.md
```

---

## ✅ To-Do

- [ ] Add edit cafe feature
- [ ] Search cafes by location
- [ ] Add user authentication

---

## 📄 License

MIT — free to use, modify, and distribute.
