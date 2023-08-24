minuman = ["air zamzam","freshtea","coca-cola","pepsi","teh kotak",]
print(minuman[2])

#append itu menambahkan data dari belakang 
minuman.append("Marimas")

#pop menghapus data 
minuman.pop(2)
print(minuman)

makanan = ("nasi tutug ocom","sate","baso","seblak","indomie")
update =list(makanan)
update[0] = "nasi timbel"
tuple = tuple(update)
print(tuple)