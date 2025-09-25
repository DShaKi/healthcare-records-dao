import unittest
from datetime import date, time
from appointment import Appointment

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.appointment = Appointment(
            appointment_id=1,
            patient_id=2,
            doctor_id=3,
            appointment_date=date(2025, 9, 30),
            start_time=time(9, 0),
            end_time=time(9, 30),
            status="scheduled",
            appointment_type="consultation",
            location="Room 101",
            notes="Patient prefers morning appointments",
        )

    def test_attributes(self):
        self.assertEqual(self.appointment.appointment_id, 1)
        self.assertEqual(self.appointment.status, "scheduled")
        self.assertEqual(self.appointment.location, "Room 101")
        self.assertEqual(self.appointment.appointment_type, "consultation")

    def test_repr_contains_appointment_id(self):
        self.assertIn("Appointment(1", repr(self.appointment))

if __name__ == '__main__':
    unittest.main()