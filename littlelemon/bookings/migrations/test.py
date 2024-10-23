from django.test import TestCase
from .models import Booking

class BookingModelTests(TestCase):
    def test_string_representation(self):
        booking = Booking(first_name="John", last_name="Doe", reservation_date="2024-10-23", reservation_slot="18:00", num_people=2)
        self.assertEqual(str(booking), "John Doe - 2024-10-23 - 18:00")
