// scripts.js

document.getElementById('date-input').addEventListener('change', function() {
    const date = this.value;
    fetch(`/reservations/?date=${date}`)
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          document.getElementById('booking-list').innerHTML = data.message;
        } else {
          let bookingsHTML = '';
          data.forEach(booking => {
            bookingsHTML += `<li>${booking.first_name} - ${booking.reservation_slot}</li>`;
          });
          document.getElementById('booking-list').innerHTML = bookingsHTML;
        }
      });
  });
  