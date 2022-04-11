class PhoneBook():
    def __init__(self) -> None:
        self.list = {}

    def add(self, name: str, phone: str):
        self.list[name] = phone

    def lookup(self, name: str):
        return self.list[name]

    def is_consistant(self):
        for name1, number1 in self.list.items():
            for name2, number2 in self.list.items():
                if name1 == name2:
                    continue
                if  number1.startswith(number2):
                    return False
        return True
    
    def get_names(self):
        return self.list.keys()

    def get_numbers(self):
        return self.list.values()