def soma(a, b):
    if a < 10:
        print("O valor de 'a' é muito pequeno. Deve ser pelo menos 10.")
    elif a < 20:
        resultado = a + b
        print(
            f"O valor de 'a' está entre 10 e 19. A soma de {a} e {b} é {resultado}.")
    else:
        print(f"O valor de 'a' é {a}, que é maior ou igual a 20.")


soma(15, 120)
