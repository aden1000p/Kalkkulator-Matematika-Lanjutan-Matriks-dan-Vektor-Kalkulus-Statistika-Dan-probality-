from rumus_matematika.module_kalulus import Limit, turunan, operasiTurunan, integral

tampungMatriks1 = []
tampungMatriks2 = []

def baris(n):
    print("=" * n)

menu = ['Limit', 'Turunan', 'Operasi Turunan', 'Integral']


def tampilan_utama():
        for i in range(10):
            baris(30)
            
            if i == 5:
                while True:
                    print("Matriks dan vektor")
                    for index, i in enumerate(menu, start=1):
                        print(index, i)

                    guess = input("masukan pilihan kamu (dengan number):  ketik 0 jika mau berhenti: ")

                    if guess == '0':
                        break
                    
                    if guess == "1":
                        Limit()

                    elif guess == '2':
                        turunan()

                    elif guess == "3":
                        list = ['tambah', 'kurang', 'bagi', 'kali']
                        for index, i in enumerate(list, start=1):
                            print(index, i)
                        
                        pilihan = input("pilih nomor berapa: ")
                        
                        operasiTurunan(pilihan)

                    elif guess == "4":
                        integral()
