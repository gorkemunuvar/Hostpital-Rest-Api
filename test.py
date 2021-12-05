import json
import cx_Oracle


class Hospital():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name



hospital = Hospital()
print(hospital.name)

hospital1 = Hospital('adsfdsa', 'Aigerim')
print(hospital1.name)