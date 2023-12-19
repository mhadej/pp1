class Phone():
    
    def __init__(self, model, rok_p, waga):
        self.model = model 
        self.rok_p = rok_p 
        self.waga  = waga
        self.is_on = False

    def __str__(self):
        return f"Model: {self.model}, rok: {self.rok_p}, waga: {self.waga}g"
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False       


phonk1 = Phone("Huawei", 2002, 300)
phonk2 = Phone("Samsun", 2020, 420)

phonk1.turn_on()
phonk1.turn_off()