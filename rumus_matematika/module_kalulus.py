from sympy import symbols, diff, Integral, limit, Subs, factor, sin
import sympy as sy

x = symbols('X')

def Limit():
    global x
    kalkulasi1 = input("masukan angka kamu 1: ")
    valueBebas = int(input("masukan value bebasnya: "))
        
    lim1 = sy.sympify(kalkulasi1)
    
    
    kalkulasi = limit(lim1, x, valueBebas)
    print(kalkulasi)

def turunan():
    global x
    f = sy.sympify(input("masukan input kamu: "))
    turunan = diff(f)
    print(turunan)

def integral():
    global x
    f = sy.sympify(input("masukan inputan kamu: "))
    integral = sy.integrate(f, x)
    print(integral)

def operasiTurunan(nomor_pilian):
    if nomor_pilian == "1":
        f1 = sy.sympify(input("masukan input kamu: "))
        f2 = sy.sympify(input("masukan input kamu: "))
        turunan = diff(f1) + diff(f2)
        print(f'{f1} + {f2} = ',turunan)
    elif nomor_pilian == "2":
        f1 = sy.sympify(input("masukan input kamu: "))
        f2 = sy.sympify(input("masukan input kamu: "))
        turunan = diff(f1) - diff(f2)
        print(f'{f1} - {f2} = ',turunan)
    elif nomor_pilian == "3":
        f1 = sy.sympify(input("masukan input kamu: "))
        f2 = sy.sympify(input("masukan input kamu: "))
        turunan = diff(f1) * diff(f2)
        print(f'{f1} * {f2} = ',turunan)
    elif nomor_pilian == "4":
        f1 = sy.sympify(input("masukan input kamu: "))
        f2 = sy.sympify(input("masukan input kamu: "))
        turunan = diff(f1) * diff(f2)
        print(f'{f1} / {f2} = ',turunan)

