from typing import Optional
from datetime import datetime

class Appointment:
    def __init__(self,
                 appointment_id: int,
                 patient_id: int,
                 doctor_id: int,
                 appointment_date: datetime.date,
                 start_time: datetime.time,
                 end_time: datetime.time,
                 status: str,
                 appointment_type: Optional[str] = None,
                 location: Optional[str] = None,
                 notes: Optional[str] = None):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.appointment_type = appointment_type
        self.location = location
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return (f"Appointment ID: {self.appointment_id}\nPatient: {self.patient_id}\nDoctor: {self.doctor_id}\n"
                f"Date: {self.appointment_date}, {self.start_time}-{self.end_time}\nStatus: {self.status}")