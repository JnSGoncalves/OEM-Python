from funcoes import *

print("""Autores:

Jônatas da Silva Gonçalves.
Wallace dos Santos Izidoro.
Pedro Henrique da Fonseca do Nascimento.
Vinícius do Nascimento Generoso.\n""")

print("Calculadora OEM em Python:\n")

print("Caso deseje entrar com valores em notação científica, utilize o formato abaixo:")
print("1.23 x 10^4 --> 1.23e4\n")

while True:
    print("""1. Entrada de Frequência de Onda
2. Entrada de Comprimento de onda
3.
4.
5.
6.
0. Sair\n""")
    
    
    opcao = input("Digite a opção que deseja: ")
    print()
    
    if(opcao == '1'):
        freq = float(input("Digite a frequência de onda (Hz): "))
        
        comprimento, k, w = freqInput(freq)
        
        comprimentoNotacao = "{:.4e}".format(comprimento)
        kNotacao = "{:.4e}".format(k)
        wNotacao = "{:.4e}".format(w)
        
        print(f"Comprimento de onda = {comprimentoNotacao}m" )
        print(f"K = {kNotacao} rad/m")
        print(f"W = {wNotacao} rad/s" ) 
        
    if(opcao == '2'):
        comprimento = float(input("Digite o comprimento de onda (m): "))
    
        f, k, w = comprimentoInput(comprimento)

        fNotacao = "{:.4e}".format(f)
        kNotacao = "{:.4e}".format(k)
        wNotacao = "{:.4e}".format(w)

        print(f"Frequência = {fNotacao} Hz")
        print(f"K = {kNotacao} rad/m" )
        print(f"W = {wNotacao} rad/s")    
        
    elif(opcao == '0'):
        print("Saindo...")
        break
    
    