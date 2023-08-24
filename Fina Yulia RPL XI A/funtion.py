def greeting(nama):
    print("hallo",nama)

greeting("Fina YUlia Lestari")
 
def penjumlahan(a, b):
     hasil = a + b
     return hasil

hasil_penjumlahan = penjumlahan(7, 9)
print("hasil dari penjumlahan adalah", hasil_penjumlahan)

#fungsi dengan variabel panjang argument(*args)
def jumlahkan(*args):
    total = 0
    for agngka in args:
        total =+ agngka
    return total

hasil = jumlahkan(12,30,40,50,5,3,7,0,700,1000) 
print(f"hasiol penjumlahan: {hasil}")