
# 📚 Study Materials Sharing Platform

> A full-stack web platform for sharing and discovering study resources — built with Django, MySQL, and JavaScript.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=flat&logo=mysql)
![HTML5](https://img.shields.io/badge/HTML5-CSS3-red?style=flat&logo=html5)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat&logo=javascript)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

---

## 🔗 Live Demo

🌐 **Live Website:**  
https://tomerarvind195-byte.github.io/Resourse-Sharing-Plateform-WebApplication/

> **Note:** This GitHub Pages deployment showcases the frontend only. For the complete Django application with backend functionality, deploy the project on Render, Railway, or PythonAnywhere.

---


# 📸 Application Screenshots

## 🏠 Home Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/901040d7-bb08-4d2e-a53d-5eb18e8c0f07" width="850"/>
</p>

---

## 📚 Resources Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/f2690ec7-5ebb-43fc-9c81-42c569379d12" width="850"/><br><br>
  <img src="https://github.com/user-attachments/assets/6366a46e-3530-4822-ad25-f5b81951f069" width="850"/><br><br>
  <img src="https://github.com/user-attachments/assets/4484a84e-d27e-47a9-9fa8-9ee460fc9275" width="850"/><br><br>
  <img src="https://github.com/user-attachments/assets/86d80c71-40e3-42c5-9b31-be2cffdff8d8" width="850"/>
</p>

---

## 📞 Contact Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/b6269d4f-ee5c-4260-95b4-5fff611b8abe" width="850"/>
</p>

---

## 📋 About The Project

A **full-stack web application** that allows students to upload, browse, and share academic study materials across multiple categories. Built to solve the problem of scattered resources by centralizing them in one easy-to-access platform.

**Key Highlights:**
- 50+ categorized study materials hosted on the platform
- Multi-section navigation: Home, Resources, Contact
- Dynamic content management using Django backend
- Mobile-first responsive design
- Clean, user-friendly interface

---

## ✨ Features

- ✅ Browse and download study materials by category
- ✅ Dynamic content management via Django admin panel
- ✅ Multi-section navigation (Home, Resources, Contact)
- ✅ Responsive design — works on mobile, tablet, and desktop
- ✅ MySQL database for structured data storage
- ✅ Fast and lightweight frontend with vanilla JavaScript

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.x, Django 4.x |
| Frontend | HTML5, CSS3, JavaScript (ES6) |
| Database | MySQL |
| Version Control | Git & GitHub |
| Deployment | _(Add: Render / Railway / PythonAnywhere)_ |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.8+
- MySQL
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/study-platform.git
cd study-platform

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup MySQL database
# Create a database named 'study_platform' in MySQL
# Update DB credentials in settings.py

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create superuser (for admin panel)
python manage.py createsuperuser

# 7. Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure

```
study-platform/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── study_platform/          # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── resources/               # Main app
│   ├── models.py            # Database models
│   ├── views.py             # Business logic
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin panel config
│
├── templates/               # HTML templates
│   ├── home.html
│   ├── resources.html
│   └── contact.html
│   └── search.html
│   └── Login.html
|   └── other etc.
|   
│
└── static/                  # CSS, JS, Images
    ├── css/
    ├── js/
    └── images/
    |__ other /
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar yeh project helpful laga toh **star** zaroor karo!
