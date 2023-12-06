class Phone:
    def __init__(self, producer, model, year):
        self.producer = producer
        self.model    = model
        self.year     = year

    def show_spec(self):
        print(f"Producer: {self.producer}, model: {self.model}, year: {self.year}")
    
    def send_hello(self):
        print("Hello!")

    def turn_on(self, turned):
        print(f"Is turned on? {turned}")

my_phone = Phone("Realme", 7, 2020)
my_phone.show_spec()
my_phone.send_hello()
my_phone.turn_on(True)
