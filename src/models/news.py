class News():
    def __init__(self, id: str = None, title: str = None,
                 description: str = None, date: str = None,
                 image_base64: str = None) -> None:
        self.id = id if id else ''
        self.title = title if title else ''
        self.description = description if description else ''
        self.date = date if date else ''
        self.image_base64 = image_base64 if image_base64 else ''
