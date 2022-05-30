class Date:
    def __init__(self, day, month, year):
        self.str_date = f'{day:02}-{month:02}-{year}'

    @classmethod
    def method_1(cls, str_date):
        day, month, year = map(int, str_date.split('-'))
        return [day, month, year]

    @staticmethod
    def method_2(str_date):
        day, month, year = map(int, str_date.split('-'))
        if day <= 31 and month <= 12 and year <= 2099:
            return f'{day:02}-{month:02}-{year}'
        else:
            return 'Проверьте введенные данные'


a = Date(12, 1, 1987)
print(a.str_date)
print(Date.method_1('12-02-2005'))
print(a.method_1('10-01-1987'))
print(Date.method_2('01-10-2022'))
print(a.method_2('44-10-2022'))

