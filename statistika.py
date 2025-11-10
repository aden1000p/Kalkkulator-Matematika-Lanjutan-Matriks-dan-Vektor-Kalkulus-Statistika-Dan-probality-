from rumus_matematika.module_statistika import mean, median, mode
tampungMatriks1 = []
tampungMatriks2 = []

def baris(n):
    print("=" * n)

menu = ['mean', 'median', 'mode']


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
                        mean()

                    elif guess == '2':
                        median()

                    elif guess == "3":
                        mode()

                    elif guess == "4":
                        pass

                    elif guess == "5":
                        pass

                    elif guess == "6":
                        pass
