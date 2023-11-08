one_symbol = 4
symbol_on_str = 25
str_on_page = 50
page_on_book = 100
bites_in_book = one_symbol * symbol_on_str * str_on_page *page_on_book
total_disk_in_bites = 1.44 * 1024 * 1024
amount_of_books = total_disk_in_bites // bites_in_book
print("Количество книг, помещающихся на дискету:", int(amount_of_books))
