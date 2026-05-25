from main import verificar_par_impar


def test_numero_par():
    assert verificar_par_impar(2, 2) == "Par"


def test_numero_impar():
    assert verificar_par_impar(1, 2) == "Impar"

#Fim
