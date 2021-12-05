from models.doctor import Doctor


class Polyclinic():
    def __init__(self, id: str = None, hospital_id: str = None,
                 title: str = None, description: str = None,
                 image_path: str = None, doctors: list[Doctor] = None) -> None:
        self.id = id
        self.hospital_id = hospital_id
        self.title = title
        self.description = description
        self.image_path = image_path
        self.doctors = doctors
