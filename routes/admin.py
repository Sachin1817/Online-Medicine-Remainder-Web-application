from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from models import User, Medicine

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.before_request
@login_required
def require_admin():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('medicines.dashboard'))

@admin_bp.route('/')
def dashboard():
    users = User.query.all()
    medicines = Medicine.query.all()
    return render_template('admin_dashboard.html', users=users, medicines=medicines)

@admin_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@admin_bp.route('/toggle_admin/<int:user_id>')
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    flash(f'Admin status for {user.username} updated.', 'success')
    return redirect(url_for('admin.users'))
