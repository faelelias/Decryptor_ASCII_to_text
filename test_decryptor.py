def encoder():
    ini_str = input('Digite sua Frase a ser convertida para ASCII: \n')
    result = [ord(c) for c in ini_str]
    print(f'Sua frase codificada em ASCII é : {result}')

encoder()
