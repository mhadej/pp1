class Song():
    def __init__(self, author, title, year, album):
        self.author = author
        self.title  = title
        self.year   = year
        self.album  = album

    def __str__(self):
        all_info = f'''
        Author: {self.author}
        Title: {self.title}
        Year: {self.year}
        Album: {self.album}'''
        return all_info
    
song1 = Song("Pinkfong", "Baby Shark", 2016, "Self-titled")
print(song1)
song2 = Song("Slipknot", "Nomadic", 2014, ".5 The Gray Chapter")
print(song2)