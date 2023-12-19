import book

book1 = book.E_Book("Saga Zmierzch", "Pattison", 5)

book1.open_book()
print(book1.status())
book1.next_page()
book1.next_page()
print(book1.status())
book1.close_book()
book1.next_page()
book1.next_page()
book1.next_page()
print(book1.status())