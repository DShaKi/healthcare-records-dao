import unittest
from daos import MedicalHistoryDAOMemoryImpl, AppointmentDAOMemoryImpl, PrescriptionDAOMemoryImpl
from datetime import date, time

class TestGenericDAO(unittest.TestCase):
    def setUp(self):
        self.medical_dao = MedicalHistoryDAOMemoryImpl()
        self.appointment_dao = AppointmentDAOMemoryImpl()
        self.prescription_dao = PrescriptionDAOMemoryImpl()

    def test_medical_history_crud(self):
        history = self.medical_dao.save(
            patient_id=1,
            diagnoses=["Hypertension"],
            allergies=[],
            medications=[]
        )
        self.assertEqual(history.patient_id, 1)

        fetched = self.medical_dao.get(history.patient_id)
        self.assertEqual(fetched.patient_id, 1)

        updated = self.medical_dao.update(history.patient_id, allergies=["Penicillin"])
        self.assertIn("Penicillin", updated.allergies)

        self.medical_dao.delete(history.patient_id)
        self.assertIsNone(self.medical_dao.get(history.patient_id))

    def test_appointment_crud(self):
        appointment = self.appointment_dao.create(
            patient_id=1,
            doctor_id=2,
            appointment_date=date(2025, 10, 1),
            start_time=time(9, 0),
            end_time=time(9, 30),
            status="scheduled"
        )
        self.assertEqual(appointment.status, "scheduled")

        fetched = self.appointment_dao.get(appointment.appointment_id)
        self.assertEqual(fetched.appointment_id, appointment.appointment_id)

        updated = self.appointment_dao.update(appointment.appointment_id, status="completed")
        self.assertEqual(updated.status, "completed")

        self.appointment_dao.delete(appointment.appointment_id)
        self.assertIsNone(self.appointment_dao.get(appointment.appointment_id))

    def test_prescription_crud(self):
        prescription = self.prescription_dao.create(
            patient_id=1,
            doctor_id=2,
            medication_name="Ibuprofen",
            dosage="200mg",
            frequency="Twice daily",
            start_date=date(2025, 10, 1)
        )
        self.assertEqual(prescription.medication_name, "Ibuprofen")

        fetched = self.prescription_dao.get(prescription.prescription_id)
        self.assertEqual(fetched.prescription_id, prescription.prescription_id)

        updated = self.prescription_dao.update(prescription.prescription_id, dosage="400mg")
        self.assertEqual(updated.dosage, "400mg")

        self.prescription_dao.delete(prescription.prescription_id)
        self.assertIsNone(self.prescription_dao.get(prescription.prescription_id))


if __name__ == '__main__':
    unittest.main()
