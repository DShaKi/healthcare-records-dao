import unittest
from datetime import date
from prescription import Prescription

class TestPrescription(unittest.TestCase):
    def setUp(self):
        self.prescription = Prescription(
            prescription_id=10,
            patient_id=2,
            doctor_id=5,
            medication_name="Amoxicillin",
            dosage="500mg",
            frequency="3 times a day",
            start_date=date(2025, 9, 20),
            end_date=date(2025, 9, 27),
            instructions="Take after meals",
            notes="Avoid if allergic to penicillin."
        )

    def test_attributes(self):
        self.assertEqual(self.prescription.medication_name, "Amoxicillin")
        self.assertEqual(self.prescription.dosage, "500mg")
        self.assertEqual(self.prescription.frequency, "3 times a day")
        self.assertEqual(self.prescription.instructions, "Take after meals")

    def test_repr_contains_prescription_id(self):
        self.assertIn("Prescription(10", repr(self.prescription))

if __name__ == '__main__':
    unittest.main()