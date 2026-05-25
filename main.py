def verificar_par_impar(n1, n2):
    # Verifica se a soma de dois números é par ou ímpar.
    if (n1 + n2) % 2 == 0:
        return  "Par"
    return "Impar"

if __name__ == "__main__":
    print(verificar_par_impar(2, 2))
