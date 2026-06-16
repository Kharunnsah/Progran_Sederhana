# Latihan

# kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("masukkan Operator (+,-,*,/) :")
angka_2 = float(input("Masukkan angka 2 = "))

# Percabangannnya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else :
    print("Masukkan yang bener dong!!")    
print("Akhir dari program, terima gajih!!")    

