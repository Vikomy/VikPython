symbols = 100 * 50 * 25
symbols_data = symbols * 4
data = 1.44 * 1024 * 1024
books = int(data//symbols_data)
print("Количество книг, помещающихся на дискету:", books)
