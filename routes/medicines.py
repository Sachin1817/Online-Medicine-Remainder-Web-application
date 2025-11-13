from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from models import Medicine
from datetime import datetime

medicines_bp = Blueprint('medicines', __name__)

@medicines_bp.route('/')
@medicines_bp.route('/dashboard')
@login_required
def dashboard():
    medicines = Medicine.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', medicines=medicines)

@medicines_bp.route('/add_medicine', methods=['GET', 'POST'])
@login_required
def add_medicine():
    if request.method == 'POST':
        name = request.form.get('name')
        dosage = request.form.get('dosage')
        frequency = request.form.get('frequency')
        times_list = request.form.getlist('times')
        times = ', '.join(times_list)
        duration = int(request.form.get('duration'))
        start_date_str = request.form.get('start_date')

        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()

        medicine = Medicine(
            name=name,
            dosage=dosage,
            frequency=frequency,
            times=times,
            duration=duration,
            start_date=start_date,
            user_id=current_user.id
        )

        db.session.add(medicine)
        db.session.commit()

        flash('Medicine added successfully!', 'success')
        return redirect(url_for('medicines.dashboard'))

    return render_template('add_medicine.html')

@medicines_bp.route('/edit_medicine/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_medicine(id):
    medicine = Medicine.query.get_or_404(id)
    if medicine.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('medicines.dashboard'))

    if request.method == 'POST':
        medicine.name = request.form.get('name')
        medicine.dosage = request.form.get('dosage')
        medicine.frequency = request.form.get('frequency')
        times_list = request.form.getlist('times')
        medicine.times = ', '.join(times_list)
        medicine.duration = int(request.form.get('duration'))
        start_date_str = request.form.get('start_date')
        medicine.start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()

        db.session.commit()
        flash('Medicine updated successfully!', 'success')
        return redirect(url_for('medicines.dashboard'))

    return render_template('edit_medicine.html', medicine=medicine)

@medicines_bp.route('/delete_medicine/<int:id>')
@login_required
def delete_medicine(id):
    medicine = Medicine.query.get_or_404(id)
    if medicine.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('medicines.dashboard'))

    db.session.delete(medicine)
    db.session.commit()
    flash('Medicine deleted successfully!', 'success')
    return redirect(url_for('medicines.dashboard'))
