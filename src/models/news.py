class News():
    def __init__(self, title: str = None, description: str = None,
                 date: str = None, image_path: str = None) -> None:
        self.title = title
        self.description = description
        self.date = date
        self.image_path = image_path