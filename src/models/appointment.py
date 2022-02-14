class Appointment():
    def __init__(self, id: str = None, date: str = None, time: str = None,
                 profession_id: str = None, profession_name: str = None,
                 doctor_id: str = None, doctor_name: str = None,
                 doctor_surname: str = None, patient_id: str = None,
                 patient_name: str = None, patient_surname: str = None,
                 patient_father: str = None, patient_birthday: str = None,
                 note: str = None) -> None:
        self.id = id
        self.date = date
        self.time = time
        self.profession_id = profession_id
        self.profession_name = profession_name
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.doctor_surname = doctor_surname
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_surname = patient_surname
        self.patient_father = patient_father
        self.patient_birthday = patient_birthday
        self.note = note
