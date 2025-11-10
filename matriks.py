import numpy as np
import rumus_matematika.module_matriks as mmv

tampungMatriks1 = []
tampungMatriks2 = []

def baris(n):
    print("=" * n)

menu = ['Operator matriks', 'Inverse', 'Determinan', 'Operator Vektor', 'Dot', 'Cross', 'Aksioma Metriks']

def tampilan_utama():
        for i in range(10):
            baris(30)
            
            if i == 5:
                while True:
                    print("Matriks dan vektor")
                    for index, i in enumerate(menu, start=1):
                        print(index, i)

                    
                    try:
                        guess = input("masukan pilihan kamu (dengan number):  ketik 0 jika mau berhenti: ")

                        if guess == '0':
                            break
                        
                        if guess == "1":
                            mmv.operasiMatriks()

                        elif guess == '2':
                            mmv.inversMatriks()

                        elif guess == "3":
                            mmv.DeterminanMatriks()

                        elif guess == "4":
                            mmv.OperasiVektor()

                        elif guess == "5":
                            mmv.dotMatriks()

                        elif guess == "6":
                            mmv.CrossMatriks()

                    except:
                        print("Nilai error")