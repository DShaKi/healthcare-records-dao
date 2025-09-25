from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import date

class Prescription:
    def __init__(self,
                 prescription_id: int,
                 patient_id: int,
                 doctor_id: int,
                 medication_name: str,
                 dosage: str,
                 frequency: str,
                 start_date: date,
                 end_date: Optional[date] = None,
                 instructions: Optional[str] = None,
                 notes: Optional[str] = None):
        self.prescription_id = prescription_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication_name = medication_name
        self.dosage = dosage
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date
        self.instructions = instructions
        self.notes = notes

    def __repr__(self):
        return (f"Prescription ID: {self.prescription_id}\nPatient: {self.patient_id}\nMedication: {self.medication_name}\n"
                f"Dosage: {self.dosage}\nFrequency: {self.frequency}")
    
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

