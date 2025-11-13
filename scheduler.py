from apscheduler.schedulers.background import BackgroundScheduler
from flask import current_app
from flask_mail import Message
from models import Medicine, User, SentReminder, db
from datetime import datetime, date, time
import logging

scheduler = BackgroundScheduler()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_reminder_email(app, user_email, medicine_name, dosage, reminder_time, medicine_id, user_id, reminder_date):
    """Send reminder email for medicine"""
    with app.app_context():
        try:
            msg = Message(
                subject=f'Medicine Reminder: {medicine_name}',
                recipients=[user_email],
                body=f"""
[💊] Medicine Reminder - {medicine_name}

Dear User,

This is your medicine reminder for today.

📋 Medicine Details:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   💊 Medicine Name: {medicine_name}
   📏 Dosage: {dosage}
   ⏰ Scheduled Time: {reminder_time}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Please take your medicine as prescribed.

Best regards,
Medicine Reminder System
"Stay healthy and take your meds on time!"
"""
            )
            app.extensions['mail'].send(msg)

            # Record the sent reminder
            sent_reminder = SentReminder(
                medicine_id=medicine_id,
                user_id=user_id,
                reminder_date=reminder_date,
                reminder_time=datetime.strptime(reminder_time, '%H:%M').time()
            )
            db.session.add(sent_reminder)
            db.session.commit()

            logger.info(f'Reminder email sent to {user_email} for {medicine_name}')
        except Exception as e:
            logger.error(f'Failed to send reminder email: {e}')

def check_reminders(app):
    """Check for medicines that need reminders"""
    with app.app_context():
        today = date.today()
        current_time = datetime.now().time()

        medicines = Medicine.query.all()

        for medicine in medicines:
            # Check if medicine is still active
            start_date = medicine.start_date
            end_date = start_date.replace(day=start_date.day + medicine.duration)
            if not (start_date <= today <= end_date):
                continue

            # Check reminder times
            reminder_times = medicine.times.split(',')
            for reminder_time_str in reminder_times:
                reminder_time = datetime.strptime(reminder_time_str.strip(), '%H:%M').time()

                # Check if reminder has already been sent today
                existing_reminder = SentReminder.query.filter_by(
                    medicine_id=medicine.id,
                    user_id=medicine.user_id,
                    reminder_date=today,
                    reminder_time=reminder_time
                ).first()

                if existing_reminder:
                    continue  # Skip if already sent

                # Check if it's time to send reminder (current time is at or just after reminder time, within 1 minute)
                time_diff = (datetime.combine(today, current_time) - datetime.combine(today, reminder_time)).total_seconds()
                if 0 <= time_diff <= 60:  # Between 0 and 60 seconds after reminder time
                    user = User.query.get(medicine.user_id)
                    if user:
                        send_reminder_email(app, user.email, medicine.name, medicine.dosage, reminder_time_str.strip(), medicine.id, user.id, today)

def start_scheduler(app):
    """Start the background scheduler"""
    if not scheduler.running:
        scheduler.add_job(func=lambda: check_reminders(app), trigger="interval", minutes=1, id='check_reminders')
        scheduler.start()
        logger.info('Scheduler started')

def stop_scheduler():
    """Stop the background scheduler"""
    if scheduler.running:
        scheduler.shutdown()
        logger.info('Scheduler stopped')
