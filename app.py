import matriks as mt
import statistika as st
import kalkulus as kk
def baris(n):
    print("=" * n)

menu = ['Aljabar Linear', 'Kalkulus', 'Staistika', 'Probalitas']

def tampilan():
    for i in range(10):
        baris(30)
        if i == 6:
            while True:
                print("Kalkulator Matematika Lanjutan ")
                for index, i in enumerate(menu, start=1):
                    print(index, i)
            
                guess = input("masukan pilihan kamu (dengan number):  ketik 0 jika mau berhenti: ")
                
                if guess == '0':
                    break
                
                if guess == "1":
                    mt.tampilan_utama()
                
                elif guess == "2":
                    kk.tampilan_utama()
                
                elif guess == "3":
                    st.tampilan_utama()

if __name__ == "__main__":
    tampilan()
