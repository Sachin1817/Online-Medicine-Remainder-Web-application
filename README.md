# 💊 Medicine Reminder Web Application

[![Flask Version](https://img.shields.io/badge/Flask-2.3.3-blueviolet?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-emerald?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Database](https://img.shields.io/badge/Database-SQLite%20%2F%20SQLAlchemy-blue?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)
[![UI Style](https://img.shields.io/badge/UI--Style-Glassmorphism%20%26%20Animations-ff69b4?style=for-the-badge&logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)

A premium, modern, and state-of-the-art web application built with Python Flask for scheduling and managing personalized medicine reminders. Featuring a high-end **Glassmorphism & Neon-Accent UI**, smooth micro-animations, automated background email reminders, and a comprehensive admin oversight panel.

---

## ✨ Features

### 👤 User Capabilities
* **Secure Portal**: Encrypted user registration and authentication with session security.
* **Intelligent Scheduler**: Add, edit, and manage medicine timetables with dynamic multi-time additions.
* **Glassmorphic Dashboard**: Review schedules in a premium grid of medicine cards, indicating dosage, frequency, and duration.
* **Automated Dispatch**: Background processor automatically fires email alerts at the exact scheduled time.
* **User Profile**: View account level metadata, role metrics, and creation timestamps.

### 🛡️ Administrator Tools
* **Operational Overview**: Dynamic cards highlighting registered users count, active schedules, and average density.
* **Account Moderation**: Elevate/revoke user administrator capabilities and oversee database tables dynamically.
* **Secure Sign-out**: Full session clearance on exit.

### ⚙️ Technical Highlights
* **Healthcare Tech Palette**: A rich custom CSS theme leveraging Google Fonts `Outfit` and `Inter`.
* **Micro-Animations**: Staggered cards entrance delay, floating capsules, and ringing notification bell interactions.
* **Background Workers**: Integrated `APScheduler` executing minute-by-minute sweeps without blocking user requests.
* **Security Shield**: Password hashing via `Werkzeug` and blueprint-level security filters.

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Description |
| :--- | :--- | :--- | :--- |
| **Backend** | Flask | `2.3.3` | Lightweight Python microframework |
| **Database** | SQLite + SQLAlchemy | `3.0.5` | Standard relational engine & ORM |
| **Authentication**| Flask-Login | `0.6.3` | User session state management |
| **Scheduling** | APScheduler | `3.10.4` | Background threading for periodic sweeps |
| **Email** | Flask-Mail | `0.9.1` | SMTP mailing interface |
| **Frontend** | Bootstrap 5 + FontAwesome 6 | `5.1.3` / `6.4.0` | Layout scaffolding and iconography |
| **Styling** | Custom CSS3 | - | Premium Glassmorphic system |

---

## 📂 Project Structure

```ascii
Online-Medicine-Remainder-Web-application/
│
├── app.py                 # Main entrypoint & Application Factory
├── config.py              # Configuration & Environment loading
├── models.py              # Database Schema Definitions
├── scheduler.py           # Background email task queue
├── requirements.txt       # Core python dependency file
├── .env                   # Local settings configurations
│
├── instance/
│   └── medicine_reminder.db  # Generated SQLite Database
│
├── routes/
│   ├── auth.py            # Login, registration, & user profiles
│   ├── medicines.py       # Dashboard CRUD operations
│   └── admin.py           # Admin dashboards & role management
│
├── static/
│   ├── css/
│   │   └── style.css      # Custom UI theme sheet
│   └── js/
│       └── script.js      # Animations & dynamic time inputs handler
│
└── templates/
    ├── base.html          # Global layout template
    ├── login.html         # Login interface
    ├── register.html      # Registration portal
    ├── dashboard.html     # User grid panel
    ├── add_medicine.html  # Intake scheduler form
    ├── edit_medicine.html # Scheduler editor form
    ├── profile.html       # Profile inspector
    ├── admin_dashboard.html# System metrics page
    └── user_list.html     # User lists sheet
```

---

## 🚀 Installation & Local Launch

### Prerequisites
* **Python 3.8+** installed on your operating system.
* **Git** installed locally.

### Setup Instructions

1. **Clone the codebase:**
   ```bash
   git clone https://github.com/Sachin1817/Online-Medicine-Remainder-Web-application.git
   cd Online-Medicine-Remainder-Web-application
   ```

2. **Establish a virtual environment:**
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and copy the contents from `.env.example` or write:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///medicine_reminder.db

   # Email configurations (Gmail App-Password)
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-16-digit-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   MAIL_ENABLED=False # Set to True to trigger active emails
   ```

   > [!IMPORTANT]
   > For Gmail reminders, enable 2-Factor Authentication on your Google Account and generate a **16-character App Password** under Account Security. Do not use your standard password.

5. **Initialize the SQLite Schema:**
   ```bash
   python -c "from app import db; db.create_all()"
   ```

6. **Start the application:**
   ```bash
   python app.py
   ```
   Open your browser to [http://localhost:5000](http://localhost:5000).

---

## 🧬 Database Architecture

### `User` Table
* `id`: Primary key (Integer)
* `username`: Unique login handle (String)
* `email`: Unique contact point (String)
* `password_hash`: Securely encrypted password (String)
* `is_admin`: Administrative privileges flag (Boolean)

### `Medicine` Table
* `id`: Primary key (Integer)
* `name`: Name of the drug (String)
* `dosage`: Measurement detail (String)
* `frequency`: Timing pattern (String)
* `times`: Comma-separated schedule times (String)
* `duration`: Treatment duration in days (Integer)
* `start_date`: Start timestamp (Date)
* `user_id`: Owning user relation (Foreign Key -> User.id)

---

## 🔒 Security Features
* **Werkzeug Encryption**: Passwords are hashed using the pbkdf2 algorithm before persistence.
* **Blueprint Isolation**: Secure partition between admin utilities and standard scheduler routes.
* **Session Guard**: Flask-Login protects views, preventing unauthenticated routing attempts.

---

## ✉️ Support & Contribution

If you run into any issues or would like to contribute:
* Submit a Pull Request or create an issue report on GitHub.
* Contact the developer directly: **sachindevaraju49@gmail.com**

---
*Created with ❤️ for smart wellness and healthcare.*
