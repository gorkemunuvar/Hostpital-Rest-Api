class Doctor():
    def __init__(self, id: str = None, name: str = None,
                 surname: str = None, description: str = None,
                 image_path: str = None, expertise: str = None,
                 education: str = None, experience: str = None,
                 achievements: str = None,) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.description = description
        self.image_path = image_path
        self.expertise = expertise
        self.education = education
        self.experience = experience
        self.achievements = achievements
