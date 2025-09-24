from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime

from datetime import datetime
from typing import Optional

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
        return (f"Appointment: {self.appointment_id}\nPatient: {self.patient_id}\nDoctor: {self.doctor_id}\n"
                f"Date: {self.appointment_date}, {self.start_time}-{self.end_time}\nStatus: {self.status})")

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