class StringHandler():
    @staticmethod
    def select_first_element_of(string: str) -> str:
        return string.strip().split(' ')[0]