import math

# Menentukan titik pusat deret Taylor
a = 25

# Menentukan nilai x yang akan dihampiri
x = 26

# Menghitung jarak x terhadap titik pusat
h = x - a

# Menghitung nilai sebenarnya dari akar 26
nilai_sebenarnya = math.sqrt(x)

# Koefisien Taylor untuk orde 0 sampai orde 4
c0 = 5
c1 = 0.1
c2 = -0.001
c3 = 0.00002
c4 = -0.0000005

# Menghitung polinom Taylor orde 0
P0 = c0

# Menghitung polinom Taylor orde 1
P1 = c0 + c1 * h

# Menghitung polinom Taylor orde 2
P2 = c0 + c1 * h + c2 * h**2

# Menghitung polinom Taylor orde 3
P3 = c0 + c1 * h + c2 * h**2 + c3 * h**3

# Menghitung polinom Taylor orde 4
P4 = c0 + c1 * h + c2 * h**2 + c3 * h**3 + c4 * h**4

# Menyimpan semua hasil polinom ke dalam list
hasil = [P0, P1, P2, P3, P4]

# Menampilkan nilai sebenarnya
print("Nilai sebenarnya =", nilai_sebenarnya)

# Melakukan perulangan untuk menampilkan P0 sampai P4
for i in range(5):

    # Mengambil nilai polinom berdasarkan orde
    nilai_P = hasil[i]

    # Menghitung galat absolut
    galat = abs(nilai_P - nilai_sebenarnya)

    # Menampilkan hasil polinom dan galatnya
    print("P" + str(i), "=", nilai_P, "| Galat =", galat)