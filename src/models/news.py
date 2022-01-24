class News():
    def __init__(self, id: str = None, title: str = None,
                 description: str = None, date: str = None,
                 image_base64: str = None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.image_base64 = image_base64
