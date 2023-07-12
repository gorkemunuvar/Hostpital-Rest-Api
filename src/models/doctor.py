class Doctor():
    def __init__(self, id: str = None, polyclinic_id: str = None,
                 profession_id: str = None, name: str = None,
                 surname: str = None, father: str = None,
                 description: str = None, image_path: str = None,
                 profession: str = None, education: str = None,
                 experience: str = None, achievements: str = None,
                 image_base64: str = None) -> None:
        self.id = id
        self.polyclinic_id = polyclinic_id
        self.profession_id = profession_id
        self.name = name
        self.surname = surname
        self.father = father
        self.description = description
        self.image_path = image_path
        self.profession = profession
        self.education = education
        self.experience = experience
        self.achievements = achievements
        self.image_base64 = image_base64
