from patient import Patient
from prescription import Prescription
from medical_history import MedicalHistory
from appointment import Appointment
from abc import ABC, abstractmethod
from typing import List, Optional


# Patient

class PatientDAO(ABC):
    @abstractmethod
    def get_patient(self, patient_id: int) -> None:
        pass

    @abstractmethod
    def get_all_patients(self) -> None:
        pass

    @abstractmethod
    def save_patient(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def update_patient(self, patient_id: int) -> None:
        pass

    @abstractmethod
    def delete_patient(self, patient_id: int) -> None:
        pass

class PatientDAOMemoryImpl(PatientDAO):
    def __init__(self):
        self.patients = {}

    def get_patient(self, patient_id: int) -> Optional[Patient]:
        return self.patients.get(patient_id)
    
    def get_all_patients(self) -> List[Patient]:
        return list(self.patients.values())
    
    def save_patient(self, patient: Patient) -> None:
        self.patients[patient.patient_id] = patient

    def update_patient(self, patient: Patient) -> None:
        self.patients[patient.patient_id] = patient

    def delete_patient(self, patient_id) -> None:
        self.patients.pop(patient_id)


# Medical Hisory

class MedicalHistoryDAO(ABC):
    @abstractmethod
    def get_medical_history(self):
        pass

    @abstractmethod
    def get_all_medical_histories(self):
        pass

    @abstractmethod
    def save_medical_history(self):
        pass

    @abstractmethod
    def update_medical_history(self):
        pass

    @abstractmethod
    def delete_medical_history(self):
        pass

class MedicalHistoryDAOMemoryImpl(MedicalHistoryDAO):
    def __init__(self):
        self.medical_histories = {}

    def get_medical_history(self, patient_id: int) -> Optional[MedicalHistory]:
        return self.medical_histories.get(patient_id)
    
    def get_all_medical_histories(self) -> List[MedicalHistory]:
        return list(self.medical_histories.values())
    
    def save_medical_history(self, medical_history: MedicalHistory) -> None:
        self.medical_histories[medical_history.patiend_id] = medical_history

    def update_medical_history(self, medical_history: MedicalHistory) -> None:
        self.medical_histories[medical_history.patiend_id] = medical_history

    def delete_medical_history(self, patient_id: int) -> None:
        self.medical_histories.pop(patient_id)

# Prescription

class PrescriptionDAO(ABC):
    @abstractmethod
    def get_prescription(self):
        pass
    
    @abstractmethod
    def get_all_prescriptions(self):
        pass

    @abstractmethod
    def save_prescription(self):
        pass

    @abstractmethod
    def update_prescription(self):
        pass

    @abstractmethod
    def delete_prescription(self):
        pass

class PrescriptionDAOMemoryImpl(PrescriptionDAO):
    def __init__(self):
        self.prescriptions = {}

    def get_prescription(self, prescription_id: int) -> Optional[Prescription]:
        return self.prescriptions[prescription_id]
    
    def get_all_prescriptions(self) -> List[Prescription]:
        return list(self.prescriptions.values())
    
    def save_prescription(self, prescription: Prescription) -> None:
        self.prescriptions[prescription.prescription_id] = prescription

    def update_prescription(self, prescription: Prescription) -> None:
        self.prescriptions[prescription.prescription_id] = prescription

    def delete_prescription(self, prescription_id: int) -> None:
        self.prescriptions.pop(prescription_id)

# Appointment

class AppointmentDAO(ABC):
    @abstractmethod
    def get_appointment(self):
        pass
    
    @abstractmethod
    def get_all_appointment(self):
        pass

    @abstractmethod
    def save_appointment(self):
        pass

    @abstractmethod
    def update_appointment(self):
        pass

    @abstractmethod
    def delete_appointment(self):
        pass

class AppointmentDAOMemoryImpl(AppointmentDAO):
    def __init__(self):
        self.appointments = {}

    def get_appointment(self, appointment_id: int) -> Optional[Appointment]:
        return self.appointments.get(appointment_id)
    
    def get_all_appointment(self) -> List[Appointment]:
        return list(self.appointments.values())
    
    def save_appointment(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment

    def update_appointment(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment

    def delete_appointment(self, appointment_id: int) -> None:
        self.appointments.pop(appointment_id)