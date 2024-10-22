# TODO Найдите количество книг, которое можно разместить на дискете


inf_volume_mb = 1.44
pages = 100
strings = 50
symbols = 25
one_symbol_byte = 4
inf_volume_byte = inf_volume_mb * 1024 * 1024
book_volume_byte = one_symbol_byte * symbols * strings * pages
count = inf_volume_byte // book_volume_byte
print("Количество книг, помещающихся на дискету:", int(count))