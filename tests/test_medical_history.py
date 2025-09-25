import unittest
from medical_history import MedicalHistory

class TestMedicalHistory(unittest.TestCase):
    def setUp(self):
        self.history = MedicalHistory(
            patient_id=1,
            diagnoses=["Hypertension"],
            allergies=["Penicillin"],
            medications=["Lisinopril"],
            surgeries=["Appendectomy"],
            family_history=["Father: Diabetes"],
            immunizations=["Influenza"],
            chronic_conditions=["High blood pressure"],
            lifestyle_factors=["Non-smoker"],
            notes="Regular checkups required."
        )

    def test_attributes(self):
        self.assertEqual(self.history.patient_id, 1)
        self.assertListEqual(self.history.diagnoses, ["Hypertension"])
        self.assertListEqual(self.history.allergies, ["Penicillin"])
        self.assertIn("Lisinopril", self.history.medications)
        self.assertEqual(self.history.notes, "Regular checkups required.")
    
    def test_repr_contains_patient_id(self):
        self.assertIn("patient_id=1", repr(self.history))

if __name__ == '__main__':
    unittest.main()
