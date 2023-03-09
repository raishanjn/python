#input user

#data yang dimasukkan pasti string
data = input("Masukkan Data = ")
print("data = ",data,", type = ", type(data))

#jika ingin mengambil int, maka
angka = float(input("Masukkan Angka ="))
angka = int(input("Masukkan Angka ="))
print("data = ",angka,", type = ", type(angka))

#bagaimana dengan boolean
biner = bool(int(input("Masukkan Nilai Boolean: ")))
print("data = ",biner,", type = ", type(biner))