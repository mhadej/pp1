class E_Book():

    def __init__(self, title, author, pages):
        self.title   = title
        self.author  = author
        self.pages   = pages
        self.current = 0
        self.is_open = False

    def next_page(self):
        if self.is_open:
            if self.current < self.pages:
                self.current += 1
        else:
            print("Studencie, otwórz książkę!")

    def prev_page(self):
        if self.is_open:
            if 0 < self.current < self.pages:
                self.current -= 1
        else:
            return "Studencie, otwórz książkę!"

    def open_book(self):
        self.is_open = True

    def close_book(self):
        self.is_open = False

    def status(self):
        return f"Book status: {self.title}, {self.author}, {self.current}/{self.pages}"