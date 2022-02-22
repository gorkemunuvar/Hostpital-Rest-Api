class StringHandler():
    @staticmethod
    def select_first_element_of(string: str) -> str:
        return string.strip().split(' ')[0]

    
    def format_date_input(date: str) -> str:
        """yyyy-mm-dd -> yyyy/mm/dd"""
        return date.replace('-', '/')

