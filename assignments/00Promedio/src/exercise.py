def main():
    #escribe tu código abajo de esta línea
    # promedio de  10 numeros leidos de teclado
    sum=0
    for i in range(0,10):
        print(i)
        num=int(input("Dame el numero "))
        sum = sum + num
    promedio = sum / 10
    print(f"El promedio de 10 numeros es {promedio}")

    pass

if __name__=='__main__':
    main()
