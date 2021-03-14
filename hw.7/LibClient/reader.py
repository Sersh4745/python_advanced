class Reader:
    def __init__(self, id: int, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

        # Тут храним id книг, которые пользователь взял почитать
        self.books = []

    def __repr__(self):
        return f'{self.id}) {self.name} {self.surname}'
