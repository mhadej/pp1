class Tv():

    channel_names = []

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        import random as rand
        

        if self.channel_names:
            x = rand.randint(0, len(self.channel_names)-1)
            if self.is_on:
                print(f"TV is on {x+1} channel - {self.channel_names[x]}")
            else:
                print("TV is off.")
    
    def set_channels(self, channel_list):
        self.channel_names = channel_list

    def show_channels(self):
        print("Channel list:")
        for i in range(len(self.channel_names)):
            print(f"{i+1}. {self.channel_names[i]}")



tv1 = Tv()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels(["Polsat", "TVN", "Filmbox"])
tv1.show_channels()
tv1.show_status()
tv1.turn_off()
tv1.show_status()