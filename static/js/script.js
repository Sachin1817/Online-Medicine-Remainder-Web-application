// Premium JavaScript for Medicine Reminder System

document.addEventListener('DOMContentLoaded', function() {
    // Elegant fade out for alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            // Apply nice fadeout class if browser supports transition
            alert.style.transition = 'opacity 0.5s ease, transform 0.5s ease, margin 0.5s ease, padding 0.5s ease, height 0.5s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            
            setTimeout(function() {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 500);
        }, 5000);
    });

    // Confirm delete actions with sweet transition (standard confirm but wrapped cleanly)
    const deleteButtons = document.querySelectorAll('a[href*="delete_medicine"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            const card = button.closest('.card');
            if (confirm('Are you sure you want to delete this medicine?')) {
                if (card) {
                    card.style.transition = 'transform 0.4s ease, opacity 0.4s ease';
                    card.style.transform = 'scale(0.9) translateY(20px)';
                    card.style.opacity = '0';
                }
            } else {
                e.preventDefault();
            }
        });
    });

    // Set default start date to today for add medicine form
    const startDateInput = document.getElementById('start_date');
    if (startDateInput && !startDateInput.value) {
        const today = new Date().toISOString().split('T')[0];
        startDateInput.value = today;
    }

    // Handle dynamic time inputs with fluid animations
    const addTimeBtn = document.getElementById('add-time');
    const timeContainer = document.getElementById('time-container');

    if (addTimeBtn && timeContainer) {
        addTimeBtn.addEventListener('click', function() {
            const timeGroup = document.createElement('div');
            timeGroup.className = 'input-group mb-2 time-entry-row';
            timeGroup.style.opacity = '0';
            timeGroup.style.transform = 'translateY(10px)';
            timeGroup.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
            
            timeGroup.innerHTML = `
                <input type="time" class="form-control time-input" name="times" required>
                <button type="button" class="btn btn-outline-danger remove-time"><i class="fas fa-trash-alt"></i> Remove</button>
            `;
            
            timeContainer.appendChild(timeGroup);
            
            // Force reflow and trigger transition
            setTimeout(() => {
                timeGroup.style.opacity = '1';
                timeGroup.style.transform = 'translateY(0)';
            }, 10);
            
            updateRemoveButtons();
        });

        timeContainer.addEventListener('click', function(e) {
            // Support both clicking button or its icon
            const targetButton = e.target.closest('.remove-time');
            if (targetButton) {
                const row = targetButton.closest('.input-group');
                row.style.opacity = '0';
                row.style.transform = 'translateY(-10px)';
                
                setTimeout(function() {
                    row.remove();
                    updateRemoveButtons();
                }, 300);
            }
        });

        function updateRemoveButtons() {
            const timeGroups = timeContainer.querySelectorAll('.input-group');
            timeGroups.forEach((group) => {
                const removeBtn = group.querySelector('.remove-time');
                if (removeBtn) {
                    if (timeGroups.length > 1) {
                        removeBtn.style.display = 'inline-block';
                    } else {
                        removeBtn.style.display = 'none';
                    }
                }
            });
        }

        // Initialize remove buttons
        updateRemoveButtons();
    }

    // Add staggered delay to medicine cards for page load entrance
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Animate progress bars using data-width to fix CSS parsing errors in HTML files
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach((bar) => {
        const width = bar.getAttribute('data-width');
        if (width) {
            bar.style.transition = 'width 1s cubic-bezier(0.16, 1, 0.3, 1)';
            setTimeout(() => {
                bar.style.width = width + '%';
            }, 200);
        }
    });
});
