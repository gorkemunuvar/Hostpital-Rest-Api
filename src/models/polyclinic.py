class Polyclinic():
    def __init__(self, id: str = None, title: str = None,
                 description: str = None, image_path: str = None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.image_path = image_path
