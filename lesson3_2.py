def about_me (name, surname, date, city, email, phone):
    return (f"{name.capitalize()} {surname.capitalize()}, родился(ась) {date} в городе {city.capitalize()}. E-mail: {email}. Телефон: {phone}")


print(about_me(input('Введите имя: '),
               input('Введите фамилию: '),
               input('Введите дату рождения: '),
               input('Введите город рождения: '),
               input('Введите e-mail: '),
               input('Введите номер телефона: ')))
