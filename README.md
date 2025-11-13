# Medicine Reminder Web Application

A comprehensive web application built with Flask for managing medicine reminders. Users can register, add medicines with dosages and schedules, and receive automated email reminders. Admins can manage users and view system statistics.

## Features

### User Features
- **User Registration & Authentication**: Secure login and registration system
- **Medicine Management**: Add, edit, and delete medicines with detailed information
- **Automated Reminders**: Email notifications at specified times
- **Dashboard**: View all medicines in a professional, responsive interface
- **Profile Management**: Update user information

### Admin Features
- **Admin Dashboard**: System statistics and user management
- **User Management**: View and manage all registered users
- **System Monitoring**: Track total users and medicines

### Technical Features
- **Responsive Design**: Professional purple-themed UI with animations
- **Email Integration**: SMTP-based email reminders
- **Background Scheduling**: Automated reminder checks every minute
- **Database**: SQLite with SQLAlchemy ORM
- **Security**: Password hashing, session management, CSRF protection

## Technology Stack

- **Backend**: Flask 2.3.3
- **Database**: SQLite with Flask-SQLAlchemy 3.0.5
- **Authentication**: Flask-Login 0.6.3
- **Email**: Flask-Mail 0.9.1
- **Scheduling**: APScheduler 3.10.4
- **Frontend**: Bootstrap 5.1.3, FontAwesome 6.0.0, Custom CSS
- **Environment**: python-dotenv 1.0.0

## Installation

### Prerequisites
- Python 3.8 or higher
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sachin1817/Online-Medicine-Remainder-Web-application.git
   cd Online-Medicine-Remainder-Web-application
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**

   Create a `.env` file in the root directory with the following variables:

   ```env
   # Flask Configuration
   SECRET_KEY=your-secret-key-here
   FLASK_ENV=development

   # Database Configuration
   DATABASE_URL=sqlite:///medicine_reminder.db

   # Email Configuration (Required for reminders)
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com

   # Optional: Custom database path
   # DATABASE_URL=postgresql://user:password@localhost/medicine_reminder
   ```

   **Important Email Setup:**
   - For Gmail: Enable 2-factor authentication and generate an App Password
   - Replace `your-email@gmail.com` with your Gmail address
   - Replace `your-app-password` with the 16-character App Password (not your regular password)
   - For other email providers, adjust MAIL_SERVER and MAIL_PORT accordingly

5. **Initialize the database:**
   ```bash
   python -c "from app import db; db.create_all()"
   ```

6. **Run the application:**
   ```bash
   python app.py
   ```

7. **Access the application:**
   - Open your browser and go to `http://localhost:5000`
   - Register a new account or login
   - Create an admin user by setting `is_admin=True` in the database

## Usage

### For Users
1. **Register**: Create an account with username, email, and password
2. **Login**: Access your dashboard
3. **Add Medicine**: Click "Add New Medicine" and fill in details:
   - Medicine name
   - Dosage (e.g., "500mg")
   - Frequency (e.g., "Twice daily")
   - Times (comma-separated, e.g., "08:00,20:00")
   - Duration in days
   - Start date
4. **Manage Medicines**: Edit or delete medicines as needed
5. **Receive Reminders**: Automated emails at specified times

### For Admins
1. **Admin Dashboard**: View system statistics
2. **User Management**: Access `/admin/users` to view all users
3. **System Monitoring**: Track user and medicine counts

## Email Configuration Details

### Gmail Setup
1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Generate an App Password:
   - Go to Security > App passwords
   - Select "Mail" and "Other"
   - Enter "Medicine Reminder App"
   - Copy the 16-character password
4. Use this App Password in your `.env` file
5. And change the MAIL_ENABLED=False
   to "True" value

### Other Email Providers
- **Outlook/Hotmail**: `MAIL_SERVER=smtp-mail.outlook.com`, `MAIL_PORT=587`
- **Yahoo**: `MAIL_SERVER=smtp.mail.yahoo.com`, `MAIL_PORT=587`
- **Custom SMTP**: Adjust server and port as needed

## Project Structure

```
medicine-reminder/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── scheduler.py          # Background scheduler for reminders
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── instance/
│   └── medicine_reminder.db  # SQLite database
├── routes/
│   ├── auth.py           # Authentication routes
│   ├── medicines.py      # Medicine management routes
│   └── admin.py          # Admin routes
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── script.js     # JavaScript
└── templates/
    ├── base.html         # Base template
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── dashboard.html    # User dashboard
    ├── admin_dashboard.html  # Admin dashboard
    └── ...               # Other templates
```

## API Endpoints

- `GET /` - Home page (redirects to login/dashboard)
- `GET/POST /login` - User login
- `GET/POST /register` - User registration
- `GET /logout` - User logout
- `GET /dashboard` - User dashboard
- `GET/POST /add_medicine` - Add new medicine
- `GET/POST /edit_medicine/<id>` - Edit medicine
- `POST /delete_medicine/<id>` - Delete medicine
- `GET /admin/dashboard` - Admin dashboard
- `GET /admin/users` - User management

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- is_admin (Boolean)

### Medicines Table
- id (Primary Key)
- name
- dosage
- frequency
- times (Comma-separated)
- duration (Days)
- start_date
- user_id (Foreign Key)

### SentReminders Table
- id (Primary Key)
- medicine_id (Foreign Key)
- user_id (Foreign Key)
- reminder_date
- reminder_time

## Security Features

- Password hashing with Werkzeug
- CSRF protection
- Session management
- Admin role-based access
- Input validation

## Development

### Running in Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Database Migrations
If you modify models, recreate the database:
```bash
rm instance/medicine_reminder.db
python -c "from app import db; db.create_all()"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
- Create an issue on GitHub
- Check the configuration and ensure all environment variables are set
- Verify email settings for reminder functionality

## Future Enhancements

- Mobile app version
- Push notifications
- Medicine interaction checker
- Prescription scanning
- Multi-language support
- Advanced reporting and analytics

##for any support contact developer
sachindevaraju49@gmail.com
