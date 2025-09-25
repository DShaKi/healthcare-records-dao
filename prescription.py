from typing import Optional
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