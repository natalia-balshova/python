class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: {self._income.get("wage") + self._income.get("bonus")}')


tomas_m = Position('Tomas', 'Miller', 'teacher', 1200.5, 200)
print(tomas_m.name)
print(tomas_m.surname)
print(tomas_m.position)
print(tomas_m._income)
tomas_m.get_full_name()
tomas_m.get_total_income()
