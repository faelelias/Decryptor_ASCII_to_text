#importando argumentos
import sys

def decode(encoded_string):
    while True:
        encoded_string = input("Entre com os dígitos numéricos 'ASCII', para ser decodificado: \n ") #solicitando entrada
        i=0
        conv = encoded_string[::-1]   #invertendo a String
        print(conv)

        #validando a entrada
        def valid(conv):
            try:
                num = conv
                if not conv.isdigit():
                    print("Digite apenas numeros!")
            except:
                pass

        valid(conv)

    # validando os valores ASCII . Tabela ASCII possui um  total 127 caracteres
        while i < len(conv):        # Verificando se a quantidade de carecteres da entrada é menor que o contador
            v = int(conv[i:i + 3])  #verificando se o numero tem 3 digitos
            if v > 127:             #  no caso de 3 caracteres , ele verifica se a entrada é maior que 127 , numero total da tabela ASCII
                v = int(conv[i:i + 2]) # validando se tem 2 caracteres
                i += 2              # interador
            else:
                i += 3              # interador
            sys.stdout.write(chr(v)) #imprime o resultado

        print()
        # solicitando a interação do usuário para terminar o flow
        sair = input('Deseja sair: [s]im ou [n]ão: \n ')
        if sair == 's':
            break
        else:
            continue



decode(64511795011010015012310123511111611011101901501611011101511234451110100171161150161179235117940101150190123511790012311100179611801711511101411231112371111138)

