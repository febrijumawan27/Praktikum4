data=[]
while True:
    nama = input("Masukan Nama : ")
    nim = input("Masukan NIM : ")
    tugas = int(input("Masukan Nilai Tugas : "))
    uts = int(input("Masukan Nilai UTS : "))
    uas = int(input("Masukan Nilai UAS : "))
    nilai = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
    data.append([nama, nim, tugas, uts, uas, nilai])
    lagi = input("Tambah lagi (y/t)?")
    if lagi.lower() == 't':
        break
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("************************Data Mahasiswa***************************")
print("^^^^^^^^^^^^^^^^^^Universitas Pelita Bangsa^^^^^^^^^^^^^^^^^^^^^^")
print("=================================================================")
print("| No |       NAMA       |    NIM    | Tugas | UTS | UAS | Akhir |")
print("=================================================================")
i=0
for x in data:
    i+=1
    print("| {6:2d} | {0:16s} | {1:9s} | {2:5d} | {3:3d} | {4:3d} | {5:2.2f} |"\
          .format(x[0][:16], x[1][:9], x[2], x[3], x[4], x[5], i))
print("=================================================================")
print("***************************Selesai*******************************")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
