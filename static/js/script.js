// Custom JavaScript for Medicine Reminder System

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('a[href*="delete_medicine"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this medicine?')) {
                e.preventDefault();
            }
        });
    });

    // Set default start date to today for add medicine form
    const startDateInput = document.getElementById('start_date');
    if (startDateInput) {
        const today = new Date().toISOString().split('T')[0];
        startDateInput.value = today;
    }

    // Handle dynamic time inputs
    const addTimeBtn = document.getElementById('add-time');
    const timeContainer = document.getElementById('time-container');

    if (addTimeBtn && timeContainer) {
        addTimeBtn.addEventListener('click', function() {
            const timeGroup = document.createElement('div');
            timeGroup.className = 'input-group mb-2';
            timeGroup.innerHTML = `
                <input type="time" class="form-control time-input" name="times" required>
                <button type="button" class="btn btn-outline-secondary remove-time">Remove</button>
            `;
            timeContainer.appendChild(timeGroup);
            updateRemoveButtons();
        });

        timeContainer.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-time')) {
                e.target.closest('.input-group').remove();
                updateRemoveButtons();
            }
        });

        function updateRemoveButtons() {
            const timeGroups = timeContainer.querySelectorAll('.input-group');
            timeGroups.forEach((group, index) => {
                const removeBtn = group.querySelector('.remove-time');
                if (timeGroups.length > 1) {
                    removeBtn.style.display = 'inline-block';
                } else {
                    removeBtn.style.display = 'none';
                }
            });
        }

        // Initialize remove buttons
        updateRemoveButtons();
    }
});
