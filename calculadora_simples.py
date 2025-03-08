
def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("s. Sair do programa ")

        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar o programa!")

            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente")
            continue

        numero_1 = float(input("Primeiro número:"))
        numero_2 = float(input("Segundo número:")) 
          

        if operacao =='1' :
          resultado =  numero_1 + numero_2
          print ("O resultado da operação de soma é: ", resultado)

        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação de subtração é: ", resultado)
            
        elif operacao =='3' :
            resultado =  numero_1 * numero_2
            print ("O resultado da operação de multiplicação é: ", resultado)
        
        else: 
            if numero_2 == 0:
                print("Divisões por zero não são possíveis. Tente novamente.")
                continue
            else:
                resultado =  numero_1 / numero_2
                print ("O resultado da operação Divisão é: ", resultado)

calculadora()