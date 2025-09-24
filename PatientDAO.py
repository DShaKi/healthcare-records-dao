from abc import ABC, abstractmethod
from typing import List, Optional

class Patient:
    def __init__(self, patient_id: int, name: str, age: int, contact: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.contact = contact
    
    def __repr__(self):
        return f"{self.patient_id}, {self.name}, {self.age}, {self.contact}"

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

if __name__ == "__main__":
    dao = PatientDAOMemoryImpl()

    p1 = Patient(1, "Ali Imani", "30", "ali@ali.com")
    p2 = Patient(5, "Ahmad Khazaei", "50", "9109088234")

    dao.save_patient(p1)
    dao.save_patient(p2)

    for p in dao.get_all_patients():
        print(p)