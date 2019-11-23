nama1=[]
nim1=[]
tugas1=[]
uts1=[]
uas1=[]
nilai1=[]
jawab='y'
while jawab=='y':
    nama = input("Nama Mahasiswa : ")
    nim = input("Nomor Induk Mahasiswa : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    nilai = (tugas)*30/100+(uts)*35/100+(uas)*35/100

    nama1.append(nama)
    nim1.append(nim)
    tugas1.append(tugas)
    uts1.append(uts)
    uas1.append(uas)
    nilai1.append(nilai)

    jawab=(input("Tambah data (y/t) ?"))
    if jawab=='t':

        print("=====================================================");
        print("|No | Nama  |    NIM    |Tugas|UTS|UAS|Akhir|");
        print("=====================================================");
        for i in range(len(nama1)):
            print("|",i+1,"|", nama1[i] ,"|",nim1[i],"|",tugas1[i],"|",uts1[i],"|",uas1[i],"|",nilai1[i],"|")
        print("=====================================================");
        print("Program Finished")
