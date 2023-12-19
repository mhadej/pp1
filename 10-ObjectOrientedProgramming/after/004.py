class Thermometer():
    def __init__(self):
        import random
        self.temperature = round(random.uniform(34.0, 42.000000000001), 1)
    
    def check(self):
        if 41 > self.temperature >= 37:
            print(f"{self.temperature}*C (fever)")
        elif self.temperature >= 41:
            print(f"{self.temperature}*C (CRITICAL TEMPERATURE!!!!!!!11!1!)")
        else:
            print(f"{self.temperature}*C")

thermo1 = Thermometer()

thermo1.check()