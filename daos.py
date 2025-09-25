from patient import Patient
from prescription import Prescription
from medical_history import MedicalHistory
from appointment import Appointment
from abc import ABC, abstractmethod
from typing import List, Optional


# Patient

class PatientDAO(ABC):
    @abstractmethod
    def get(self, patient_id: int) -> None:
        pass

    @abstractmethod
    def get_all(self) -> None:
        pass

    @abstractmethod
    def save(self, patient: Patient) -> None:
        pass

    @abstractmethod
    def update(self, patient_id: int) -> None:
        pass

    @abstractmethod
    def delete(self, patient_id: int) -> None:
        pass

class PatientDAOMemoryImpl(PatientDAO):
    def __init__(self):
        self.patients = {}

    def get(self, patient_id: int) -> Optional[Patient]:
        return self.patients.get(patient_id)
    
    def get_all(self) -> List[Patient]:
        return list(self.patients.values())
    
    def save(self, patient: Patient) -> None:
        self.patients[patient.patient_id] = patient

    def update(self, patient: Patient) -> None:
        self.patients[patient.patient_id] = patient

    def delete(self, patient_id) -> None:
        self.patients.pop(patient_id)


# Medical Hisory

class MedicalHistoryDAO(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class MedicalHistoryDAOMemoryImpl(MedicalHistoryDAO):
    def __init__(self):
        self.medical_histories = {}

    def get(self, patient_id: int) -> Optional[MedicalHistory]:
        return self.medical_histories.get(patient_id)
    
    def get_all(self) -> List[MedicalHistory]:
        return list(self.medical_histories.values())
    
    def save(self, medical_history: MedicalHistory) -> None:
        self.medical_histories[medical_history.patiend_id] = medical_history

    def update(self, medical_history: MedicalHistory) -> None:
        self.medical_histories[medical_history.patiend_id] = medical_history

    def delete(self, patient_id: int) -> None:
        self.medical_histories.pop(patient_id)

# Prescription

class PrescriptionDAO(ABC):
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class PrescriptionDAOMemoryImpl(PrescriptionDAO):
    def __init__(self):
        self.prescriptions = {}

    def get(self, prescription_id: int) -> Optional[Prescription]:
        return self.prescriptions[prescription_id]
    
    def get_all(self) -> List[Prescription]:
        return list(self.prescriptions.values())
    
    def save(self, prescription: Prescription) -> None:
        self.prescriptions[prescription.prescription_id] = prescription

    def update(self, prescription: Prescription) -> None:
        self.prescriptions[prescription.prescription_id] = prescription

    def delete(self, prescription_id: int) -> None:
        self.prescriptions.pop(prescription_id)

# Appointment

class AppointmentDAO(ABC):
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class AppointmentDAOMemoryImpl(AppointmentDAO):
    def __init__(self):
        self.appointments = {}

    def get(self, appointment_id: int) -> Optional[Appointment]:
        return self.appointments.get(appointment_id)
    
    def get_all(self) -> List[Appointment]:
        return list(self.appointments.values())
    
    def save(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment

    def update(self, appointment: Appointment) -> None:
        self.appointments[appointment.appointment_id] = appointment

    def delete(self, appointment_id: int) -> None:
        self.appointments.pop(appointment_id)