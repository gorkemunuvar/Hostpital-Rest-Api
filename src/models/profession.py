
class Profession():
    def __init__(self, id: str = None, polyclinic_id: str = None,
                 name: str = None, type: str = None) -> None:
        self.id = id if id else ''
        self.polyclinic_id = polyclinic_id if polyclinic_id else ''
        self.name = name if name else ''
        self.type = type if type else ''
        