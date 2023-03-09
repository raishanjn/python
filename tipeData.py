#tipe data : Angka satuan (integer) yang gak ada komanya
data_integer = 190909
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data : angka dengan nilai koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#tipe data : kumpulan karakter (string)
data_string = "raisha"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#tipe data : biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

##tipe data khusus

#tipe data  bilangan kompleks
data_complex = complex(2,7)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bahas C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))