import numpy as np 

def mean():
    guess = list(map(int, input("masukan nilai kamu: ").split()))
    meannNumpy = np.mean(guess)
    print(guess)
    print('nilai rata-rata dari data : {}' .format(meannNumpy))

def median():
    guess = list(map(int, input("masukan nilai kamu: ").split()))
    medianNumpy = np.median(guess)
    print(guess)
    print("nilai median dari data adalah: {}" .format(medianNumpy))

def mode():
    guess = list(map(int, input("masukan nilai kamu: ").split()))
    values, counts = np.unique(guess, return_counts=True)
    mode = values[np.argmax(counts)]
    print(guess)
    print("nilai median dari data adalah: {}" .format(mode))

def range():
    guess = list(map(int, input("masukan nilai kamu: ").split()))
    arrayGuess = np.array(guess)
