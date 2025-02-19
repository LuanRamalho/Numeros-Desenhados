def exibir_numeros():
    numeros = {
        "0": [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ],
        "1": [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            " *** "
        ],
        "2": [
            " *** ",
            "*   *",
            "   * ",
            "  *  ",
            "*****"
        ],
        "3": [
            " *** ",
            "*   *",
            "   **",
            "*   *",
            " *** "
        ],
        "4": [
            "   * ",
            "  ** ",
            " * * ",
            "*****",
            "   * "
        ],
        "5": [
            "*****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ],
        "6": [
            " *** ",
            "*    ",
            "**** ",
            "*   *",
            " *** "
        ],
        "7": [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            " *   "
        ],
        "8": [
            " *** ",
            "*   *",
            " *** ",
            "*   *",
            " *** "
        ],
        "9": [
            " *** ",
            "*   *",
            " ****",
            "    *",
            " *** "
        ]
    }
    
    for numero in range(10):
        print(f"Número {numero}:")
        for linha in numeros[str(numero)]:
            print(linha)
        print("\n")


# Chama a função para exibir os números de 0 a 9
exibir_numeros()
input()
