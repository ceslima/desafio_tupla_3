def contar_caracteres(string):
    """
    Conta a ocorrência de cada caractere em uma string.

    Args:
        string: A string de entrada.

    Returns:
        Um dicionário onde as chaves são os caracteres e os valores são as contagens.
        Retorna None se a entrada não for uma string.
    """
    try:
        if not isinstance(string, str):
            raise TypeError("A entrada deve ser uma string.")

        contador = {}
        for caractere in string:
            if caractere in contador:
                contador[caractere] += 1
            else:
                contador[caractere] = 1
        return contador

    except TypeError as e:
        print(f"Erro: {e}")
        return None

# Solicita a string do usuário
entrada_usuario = input("")

# Chama a função e imprime o resultado
resultado = contar_caracteres(entrada_usuario)

if resultado:
    print(resultado)
