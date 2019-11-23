list_a = [21, 23, 25, 27, 29]
print(list_a)
print(list_a[2])
print(list_a[1:4])
print(list_a[-1])

#Ubah Element List

list_a[3] = 20
print(list_a[3])
list_a[3:4] = 22, 24
print(list_a[3:5])

#Tambah ELement List

list_b = list_a[0:2]
print(list_b)
list_b.append(26)
print(list_b)
list_b.extend([30, 32, 35])
print(list_b)
list_c = list_a + list_b
print(list_c)
