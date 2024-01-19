class C():

    def __init__(self, dict1):
        self.dict1 = dict1
    
    def m1(self, s, n):
        self.dict1.update({f"{s}":n})

    def m2(self, string):
        suma = 0
        for letter in string:
            for key, value in self.dict1.items():
                if key == letter:
                    suma += value
        return suma
    
stadion = C({"A":120,"D":150,"G":90,"K":110})
stadion.m1("G", 130)

print(stadion.m2("GD"))
print(stadion.m2("KEJ"))