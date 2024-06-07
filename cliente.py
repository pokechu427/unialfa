import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    # Substitua 'obj_369e8b0f96954353a3b166bc579639db@localhost:53649' pelo URI do servidor
    calculadora = Pyro4.Proxy("PYRO:obj_369e8b0f96954353a3b166bc579639db@localhost:53649")

    # Realiza a soma, subtração e multiplicação
    soma = calculadora.somar(85, 3)
    subtracao = calculadora.subtrair(85, 3)
    multiplicacao = calculadora.multiplicar(85, 3)

    # Exibe os resultados
    print("A soma é:", soma)
    print("A subtração é:", subtracao)
    print("A multiplicação é:", multiplicacao)

if __name__ == "__main__":
    main()
