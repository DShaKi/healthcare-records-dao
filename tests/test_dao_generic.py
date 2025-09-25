import unittest
from datetime import datetime, date, time

from patient import Patient
from appointment import Appointment
from medical_history import MedicalHistory
from prescription import Prescription

from daos import PatientDAOMemoryImpl, PrescriptionDAOMemoryImpl, MedicalHistoryDAOMemoryImpl, AppointmentDAOMemoryImpl

class GenericDAOTest(unittest.TestCase):
    def setUp(self):
        if type(self) is GenericDAOTest:
            self.skipTest("Base class")

    def test_create_and_get(self):
        self.dao.create(self.sample_entity)
        fetched = self.dao.get(self._get_id(self.sample_entity))
        self.assertIsNotNone(fetched)
        self.assertEqual(self._get_id(fetched), self._get_id(self.sample_entity))

    def test_update(self):
        self.dao.create(self.sample_entity)
        self.dao.update(self.updated_entity)
        updated = self.dao.get(self._get_id(self.updated_entity))
        self.assertIsNotNone(updated)
        self.assertEqual(self._get_id(updated), self._get_id(self.updated_entity))

    def test_delete(self):
        self.dao.create(self.sample_entity)
        self.dao.delete(self._get_id(self.sample_entity))
        self.assertIsNone(self.dao.get(self._get_id(self.sample_entity)))

    def test_get_all(self):
        self.dao.create(self.sample_entity)
        all_entities = self.dao.get_all()
        self.assertIsInstance(all_entities, list)
        self.assertGreaterEqual(len(all_entities), 1)

    def _get_id(self, entity):
        for attr in ('patient_id', 'prescription_id', 'appointment_id'):
            if hasattr(entity, attr):
                return getattr(entity, attr)
        return getattr(entity, 'id', None)


class TestPatientDAO(GenericDAOTest):
    def setUp(self):
        self.dao = PatientDAOMemoryImpl()
        self.sample_entity = Patient(patient_id=1, name="Alice", age=30, contact="12345")
        self.updated_entity = Patient(patient_id=1, name="Alice Updated", age=31, contact="67890")


class TestPrescriptionDAO(GenericDAOTest):
    def setUp(self):
        self.dao = PrescriptionDAOMemoryImpl()
        self.sample_entity = Prescription(
            prescription_id=1,
            patient_id=1,
            doctor_id=2,
            medication_name="Aspirin",
            dosage="100mg",
            frequency="Once daily",
            start_date=date(2025, 1, 1)
        )
        self.updated_entity = Prescription(
            prescription_id=1,
            patient_id=1,
            doctor_id=2,
            medication_name="Ibuprofen",
            dosage="200mg",
            frequency="Twice daily",
            start_date=date(2025, 1, 1)
        )


class TestMedicalHistoryDAO(GenericDAOTest):
    def setUp(self):
        self.dao = MedicalHistoryDAOMemoryImpl()
        self.sample_entity = MedicalHistory(
            patient_id=1,
            diagnoses="Hypertension",
            allergies=["Penicillin"],
            medications=["Lisinopril"],
            surgeries=["Appendectomy"],
            family_history=["Father: Diabetes"],
            immunizations=["Flu"],
            chronic_conditions=["Hypertension"],
            lifestyle_factors=["Non-smoker"],
            notes="Checkup annually"
        )
        self.updated_entity = MedicalHistory(
            patient_id=1,
            diagnoses="Hypertension Updated",
            allergies=["Penicillin"],
            medications=["Lisinopril", "Aspirin"],
            surgeries=["Appendectomy"],
            family_history=["Father: Diabetes"],
            immunizations=["Flu"],
            chronic_conditions=["Hypertension"],
            lifestyle_factors=["Non-smoker"],
            notes="Checkup every 6 months"
        )


class TestAppointmentDAO(GenericDAOTest):
    def setUp(self):
        self.dao = AppointmentDAOMemoryImpl()
        self.sample_entity = Appointment(
            appointment_id=1,
            patient_id=1,
            doctor_id=2,
            appointment_date=date(2025, 10, 1),
            start_time=time(9, 0),
            end_time=time(9, 30),
            status="scheduled"
        )
        self.updated_entity = Appointment(
            appointment_id=1,
            patient_id=1,
            doctor_id=2,
            appointment_date=date(2025, 10, 2),
            start_time=time(10, 0),
            end_time=time(10, 30),
            status="rescheduled"
        )


if __name__ == "__main__":
    unittest.main()
