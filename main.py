x = int(input("Podaj liczbę x (1-100): "))

if 1 <= x <= 100:
    length = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        length += 1
    print(f"Długość ciągu dla liczby {x} wynosi {length}.")
else:
    print("Nieprawidłowa liczba x. Podaj liczbę z zakresu 1-100.")
