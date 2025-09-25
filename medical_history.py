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
        self.patient_id = patient_id
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
        return f"patient id: {self.patient_id}\ndiagnoses: {self.diagnose}\nmedications: {self.medications}\nsurgeries: {self.surgeries}\nfamily_history: {self.family_history}\nimmunizations: {self.immunizations}\nchronic conditions: {self.chronic_condition}\nlifestyle factors: {self.lifestyle_factors}\nnotes: {self.notes}"