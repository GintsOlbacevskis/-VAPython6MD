try:
    number = 10
    divisor = 2
    result = number / divisor
    print(f"Rezultāts: {result}")
except ZeroDivisionError:
    print("Kļūda: Dalīšanas ar nulli nav atļauta")
finally:
    print("Matemātiskā funkcija veikta")