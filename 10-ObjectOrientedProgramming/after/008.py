class C():

    def __init__(self, name, surname, age, seniority):
        self.name       = name
        self.surname    = surname
        self.age        = age
        self.seniority  = seniority

    def __str__(self):
        if self.age >= 18:
            print(f'{self.surname.upper()}{self.name[0].upper()}{self.seniority}')
        else:
            print(f'{self.surname.lower()}{self.name[0].lower()}{self.seniority}')

employee1 = C("Anna","May",17,7)
employee2 = C("George","Brown",21,4)

employee1.__str__()
employee2.__str__()