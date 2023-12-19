class Statistics():
    
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def show_nr(self):
        for i in self.numbers:
            print(i, end=" ")
    
    def show_max(self):
        print(max(self.numbers))

    def show_min(self):
        print(min(self.numbers))

    def mean(self):
        print(round(sum(self.numbers)/len(self.numbers), 2))

    def median(self):
        x = sorted(self.numbers)

        if len(x)%2:
            print(x[int(len(x)/2)])
        else:
            print((x[int(len(x)/2)-1] + x[int(len(x)/2)] )/ 2)

    def show_all(self):
        self.show_min()
        self.show_max()
        self.mean()
        self.median()
        self.show_nr()

stat1 = Statistics()

stat1.add_number(6)
stat1.add_number(9)
stat1.add_number(21)
stat1.add_number(37)

stat1.show_all()