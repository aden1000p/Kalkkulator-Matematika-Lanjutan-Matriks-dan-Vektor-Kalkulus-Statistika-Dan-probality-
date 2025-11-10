import numpy as np

def operasiMatriks():
    def tambahMatriks(matriks1, matriks2):
        tambah  = matriks1 + matriks2
        print(matriks1, ' + ', matriks2, ' = ', tambah)
    
    def kurangMatriks(matriks1, matriks2):
        kurang  = matriks1 - matriks2
        print(matriks1, ' - ', matriks2, ' = ', kurang)
    
    def perkalianMatriks(matriks1, matriks2):
        kali= matriks1 * matriks2
        print(matriks1, ' * ', matriks2, ' = ', kali)
    
    def pembagianMatriks(matriks1, matriks2):
        bagi = matriks1 / matriks2
        print(matriks1, ' / ', matriks2, ' = ', bagi)
    
    def moduleMatriks(matriks1, matriks2):
        module = matriks1 % matriks2
        print(matriks1, ' % ', matriks2, ' = ', module)
    
    tampungnilai1 = []
    tampungnilai2 = []
    
    listed = ['tambah', 'kurang', 'bagi', 'kali', 'module']
    
    kolom = int(input("masukan Berapa kolom: "))
    
    print("mengisi matriks ke 1 ")
    for i in range(kolom):
        nilai1 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai1.append(nilai1)
    
    print("mengisi matriks ke 2")
    for j in range(kolom):
        nilai2 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai2.append(nilai2)

    matriks1 = np.array(tampungnilai1)
    matriks2 = np.array(tampungnilai2)
    
    print("OPERASI MATRIKS")
    
    for i, j in enumerate(listed, start=1):
        print(i, j)
    
    print(matriks1)
    print(matriks2)
    
    try:
        guess = input("masukan pilihan kamu (berupa pilihan nomor): ")
        
        if guess == "1":
            tambahMatriks(matriks1, matriks2)
        elif guess == "2":
            kurangMatriks(matriks1, matriks2)
        elif guess == "3":
            perkalianMatriks(matriks1, matriks2)
        elif guess == "4":
            pembagianMatriks(matriks1, matriks2)
        elif guess == "5":
            moduleMatriks(matriks1, matriks2)
        else:
            print("tidak ada menu terseida coba lagi ")
    except:
        print("Kayaknya Kamu ada masalah deh")

def inversMatriks():
    tampungnilai = []
    kolom = int(input("masukan Berapa kolom: "))
    
    for i in range(kolom):
        nilai1 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai.append(nilai1)
    
    NilaiNumpy = np.array(tampungnilai)
    
    inverse_numpy = np.linalg.inv([NilaiNumpy])
    
    print(f"Inverse dari \n{NilaiNumpy} = \n{inverse_numpy}")

def DeterminanMatriks():
    tampungnilai = []
    kolom = int(input("masukan Berapa kolom: "))
    
    for i in range(kolom):
        nilai1 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai.append(nilai1)
    
    NilaiNumpy = np.array(tampungnilai)
    
    determinan_numpy = np.linalg.det(NilaiNumpy)
    
    print(f"Inverse dari \n{NilaiNumpy} = \n{determinan_numpy}")

def OperasiVektor():
    operasiMatriks()


def dotMatriks():
    tampungnilai1 = []
    tampungnilai2 = []

    kolom = int(input("masukan Berapa kolom: "))
    
    for i in range(kolom):
        nilai1 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai1.append(nilai1)
    
    for i in range(kolom):
        nilai2 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai2.append(nilai2)
    
    NilaiNumpy1 = np.array(tampungnilai1)
    NilaiNumpy2 = np.array(tampungnilai2).reshape(-1, 1)
    
    dot_numpy = NilaiNumpy1.dot(NilaiNumpy2)
    
    print(f"Inverse dari \n{NilaiNumpy1} * \n{NilaiNumpy2}= \n{dot_numpy}")
    
    
def CrossMatriks():
    tampungnilai1 = []
    tampungnilai2 = []

    kolom = int(input("masukan Berapa kolom: "))
    
    for i in range(kolom):
        nilai1 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai1.append(nilai1)
    
    for i in range(kolom):
        nilai2 = list(map(int, input("masukan angka kesukaan kamu:? ").split()))
        tampungnilai2.append(nilai2)
    
    NilaiNumpy1 = np.array(tampungnilai1)
    NilaiNumpy2 = np.array(tampungnilai2)
    
    dot_numpy = np.linalg.cross(NilaiNumpy1, NilaiNumpy2)
    print(f"Inverse dari \n{NilaiNumpy1} * \n{NilaiNumpy2}= \n{dot_numpy}")
    