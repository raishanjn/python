#operasi aritmatika

a = 7
b = 2

#operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi eksponen/pangkat **
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus/sisa pembagian %
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division/kebalikan modulus //
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalilan dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 2
y = 3
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)
 #kurung akan mengambil langkah paling pertama 
hasil = (x + y) * z
print('(',x,'+',y,') *',z, '=',hasil)