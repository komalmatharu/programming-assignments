def main ():
    SIZE = 5

    print(" " * (SIZE * 4) + "X" * (SIZE * 6 + 1))
    print(" " * (SIZE * 4) + "X" * (SIZE * 6 + 1))
    print(" " * (SIZE * 4) + "X" * SIZE + " " * (SIZE * 4+1) + "X" * SIZE)
    print(" " * (SIZE * 4) + "X" * (SIZE * 3) + " " + "X" * (SIZE * 3))
    print(" " * (SIZE * 4) + "X" * (SIZE * 3 - 1) + " " * 3 + "X" * (SIZE * 3 - 1))
    
    for i in range(3):
        print(" " * (SIZE * 5 - i) + "X" * SIZE + " " * SIZE + "*" * (2 * i +1 ) + " " * SIZE + "X" * SIZE)

    for i in range(3):
        print(" " * (SIZE * 5 - i -3) + "X" * SIZE + " " * SIZE + "*" * 3 + " " * (2 * i + 1) + "*" * 3 + " " * SIZE + "X" * SIZE)

    print(" " * (SIZE * 5 - 6) + "X" * SIZE + " " * SIZE + "*" * 13 + " " * SIZE + "X" * SIZE)
    print(" " * (SIZE * 5 - 7) + "X" * SIZE + " " * SIZE + "*" * 15 + " " * SIZE + "X" * SIZE)

    for i in range(3):
        print(" " * (SIZE * 5 - i - 8) + "X" * SIZE + " " * SIZE + "*" * 3 + " " * (11 + 2 * i) + "*" * 3 + " " * SIZE + "X" * SIZE)

    print(" " * (SIZE * 5 - 11) + "X" * SIZE + " " * (SIZE * 2 + 23) + "X" * SIZE)

    print(" " * (SIZE * 4 - 11) + "X" * (SIZE * 6 + 23))
    print(" " * (SIZE * 4 - 11) + "X" * (SIZE * 6 + 23))
    print(" " * (SIZE * 4 - 11) + "X" * SIZE + " " * (SIZE * 4 +23) + "X" * SIZE)
    print(" " * (SIZE * 4 - 11) + "X" * (SIZE * 6 + 23))
    print(" " * (SIZE * 4 - 11) + "X" * (SIZE * 6 + 23))
    
main()

