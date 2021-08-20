def main():
    #escribe tu código abajo de esta línea

    a = int(input("Dame el peso inicial: "))
    b = int(input("Dame el peso final: "))
    c = int(input("Dame la cantidad de meses: "))
    s = (a-b)/c
    print("Lo que debes bajar por mes es:",s)

if __name__ == '__main__':
    main()
