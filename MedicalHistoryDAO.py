from abc import ABC, abstractmethod
from typing import List, Optional

class MedicalHistory:
    def __init__(self, patient_id: int,
                 diagnoses: str, 
                 allergies: list[str], 
                 medications: list[str], 
                 surgeries: list[str], 
                 family_history: list[str], 
                 immunizations: list[str], 
                 chronic_conditions: list[str], 
                 lifestyle_factors: list[str], 
                 notes: str):
        self.patiend_id = patient_id
        self.diagnose = diagnoses
        self.allergies = allergies
        self.medications = medications
        self.surgeries = surgeries
        self.family_history = family_history
        self.immunizations = immunizations
        self.chronic_condition = chronic_conditions
        self.lifestyle_factors = lifestyle_factors
        self.notes = notes
    
    def __repr__(self):
        return f"id: {self.patiend_id}\ndiagnoses: {self.diagnose}\nmedications: {self.medications}\nsurgeries: {self.surgeries}\nfamily_history: {self.family_history}\nimmunizations: {self.immunizations}\nchronic conditions: {self.chronic_condition}\nlifestyle factors: {self.lifestyle_factors}\nnotes: {self.notes}"
    
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

if __name__ == "__main__":
    dao = MedicalHistoryDAOMemoryImpl()

    history1 = MedicalHistory(
        patient_id=101,
        diagnoses=["Hypertension", "Hypercholesterolemia"],
        allergies=["Penicillin (rash)"],
        medications=["Simvastatin 40mg daily", "Lisinopril 10mg daily"],
        surgeries=["Appendectomy at age 12"],
        family_history=["Father had hypertension and heart disease", "Mother has type 2 diabetes"],
        immunizations=["Influenza vaccine 2024", "COVID-19 vaccine series completed"],
        chronic_conditions=["High blood pressure", "High cholesterol"],
        lifestyle_factors=["Non-smoker", "Occasional alcohol consumption", "Regular walking exercise"],
        notes="Patient advised to reduce salt intake and monitor blood pressure regularly."
    )

    history2 = MedicalHistory(
        patient_id=102,
        diagnoses=["Osteoarthritis", "Type 2 Diabetes (diet-managed)"],
        allergies=[],
        medications=["Metformin 500mg twice daily", "Naproxen 500mg as needed"],
        surgeries=["Left hip replacement (2018)"],
        family_history=["Brother diagnosed with Perthe’s disease"],
        immunizations=["Tetanus booster 2023", "Pneumococcal vaccine 2021"],
        chronic_conditions=["Osteoarthritis", "Diabetes"],
        lifestyle_factors=["Former smoker (quit 5 years ago)", "Low alcohol intake", "Exercises with physiotherapy weekly"],
        notes="Recommend continued physiotherapy and blood sugar monitoring."
    )


    dao.save_medical_history(history1)
    dao.save_medical_history(history2)

    for h in dao.get_all_medical_histories():
        print(h)
        print("-------------------------------------------------------------------------------------------")