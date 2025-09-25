class Patient:
    def __init__(self, patient_id: int, name: str, age: int, contact: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.contact = contact
    
    def __repr__(self):
        return f"{self.patient_id}, {self.name}, {self.age}, {self.contact}"