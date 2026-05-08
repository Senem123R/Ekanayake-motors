# 🚗 Ekanayake Motor Industries — Inventory & Order Management System

> A full-stack web application for managing automotive spare parts inventory and customer orders, with mobile app API integration.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

---

## 🌐 Live Demo

| Platform | Link |
|----------|------|
| 🌍 Customer Website | [your-netlify-url.netlify.app](#) |
| 🔒 Admin Panel | [your-netlify-url.netlify.app/admin](#) |
| ⚙️ Backend API | [your-render-url.onrender.com](#) |

---

## ✨ Features

### 🛍️ Customer Website
- Browse spare parts catalog with responsive grid layout
- Filter parts by **brand**, **type**, and **availability**
- Search functionality across all products
- Product cards with photo, part number, price & stock status
- **Order form** — customers submit requests directly from the site

### 🔐 Admin Panel
- Secure **session-based login** (credentials never exposed in frontend)
- **Dashboard** with real-time stats — total products, in stock, manufactured, new orders
- **Full product CRUD** — add, edit, delete with 3 photo upload methods:
  - 📁 File upload from computer/phone
  - ☁️ Google Drive link (auto-converts to preview)
  - 🔗 Direct image URL
- **Order management** with status pipeline: `New → Contacted → Done`
- One-tap **WhatsApp reply** with pre-filled message
- Direct **call button** per order

### 📱 Mobile App Integration
- REST APIs serve both the web platform and a mobile application
- Single backend enabling cross-platform data access

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · Flask |
| Database | Firebase Firestore |
| Frontend | HTML · Tailwind CSS · JavaScript |
| Auth | Flask Session-based |
| REST API | Flask RESTful routes |
| Frontend Hosting | Netlify |
| Backend Hosting | Render |
| Version Control | GitHub |

---

## 📁 Project Structure

```
ekanayake-motors/
│
├── app.py                  ← Flask server (main file)
├── firebase_config.py      ← Firebase connection
├── requirements.txt        ← Python packages
│
├── templates/
│   ├── index.html          ← Customer website
│   ├── admin.html          ← Admin panel
│   └── login.html          ← Admin login page
│
└── static/
    ├── js/
    │   ├── main.js         ← Customer site JS
    │   └── admin.js        ← Admin panel JS
    └── css/
        └── custom.css      ← Extra styles
```

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.8+
- Firebase project with Firestore enabled
- Firebase service account key (`serviceAccountKey.json`)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ekanayake-motors.git
cd ekanayake-motors
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Firebase credentials
- Go to [Firebase Console](https://console.firebase.google.com)
- Project Settings → Service Accounts → Generate new private key
- Save as `serviceAccountKey.json` in the root folder

### 5. Create `.env` file
```env
SECRET_KEY=your-secret-key-here
ADMIN_EMAIL=admin@gmail.com
ADMIN_PASSWORD=yourpassword
```

### 6. Run the app
```bash
python app.py
```

Open browser → `http://localhost:5000` ✅

---

## 🔌 API Endpoints

### Customer APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | Get all products |
| POST | `/api/orders` | Submit a new order |

### Admin APIs (login required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/admin/products` | Get all products |
| POST | `/api/admin/products` | Add new product |
| PUT | `/api/admin/products/<id>` | Update product |
| DELETE | `/api/admin/products/<id>` | Delete product |
| GET | `/api/admin/orders` | Get all orders |
| PUT | `/api/admin/orders/<id>` | Update order status |

---

## ☁️ Deployment

### Frontend → Netlify
1. Push code to GitHub
2. Go to [netlify.app](https://netlify.app) → Import from GitHub
3. Set build settings and deploy

### Backend → Render
1. Go to [render.com](https://render.com) → New Web Service
2. Connect GitHub repo
3. Set environment variables:
   - `SECRET_KEY`
   - `ADMIN_EMAIL`
   - `ADMIN_PASSWORD`
4. Start command: `gunicorn app:app`

---

## 🔒 Security Notes

- Admin credentials stored as **environment variables** — never hardcoded
- Session-based authentication protects all admin routes
- Firebase service account key excluded from version control (`.gitignore`)
- CORS configured for allowed origins only

---

## 📄 License

This project is built for **Ekanayake Motor Industries**. All rights reserved.

---

## 👨‍💻 Developer

**[Risni Maleesha]**
- 💼 LinkedIn: [(https://www.linkedin.com/in/risni-maleesha-3a8524316/)](#)
- 🐙 GitHub: [(https://github.com/Senem123R)](#)

---

> ⭐ If you found this project helpful, give it a star!
