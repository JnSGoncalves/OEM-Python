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
    print("""1. Entrada de Frequência de Onda (F)
2. Entrada de Comprimento de onda (λ)
3. Entrada de Número de onda (k)
4. Entrada de Frequência angular (w)
5. Entrada da Amplitude do campo Magnético (Bm)
6. Entrada de Amplitude do campo Elétrico (Em)
7. Entrada de Intensidade de uma onda Eletromagnética (I)
0. Sair\n""")
    
    
    opcao = input("Digite a opção que deseja: ")
    print()
    
    if(opcao == '1'):
        freq = float(input("Digite a frequência de onda (Hz): "))
        
        comprimento, k, w = freqInput(freq)
        
        comprimentoNotacao = "{:.4e}".format(comprimento)
        kNotacao = "{:.4e}".format(k)
        wNotacao = "{:.4e}".format(w)

        print()
        print(f"λ (Comprimento de onda) = {comprimentoNotacao} m" )
        print(f"K (Número de onda) = {kNotacao} rad/m")
        print(f"W (Frequência angular da onda) = {wNotacao} rad/s" ) 
        print()
        
    elif(opcao == '2'):
        comprimento = float(input("Digite o comprimento de onda (m): "))
    
        f, k, w = comprimentoInput(comprimento)

        fNotacao = "{:.4e}".format(f)
        kNotacao = "{:.4e}".format(k)
        wNotacao = "{:.4e}".format(w)

        print()
        print(f"F (Frequência) = {fNotacao} Hz")
        print(f"K (Número de onda) = {kNotacao} rad/m" )
        print(f"W (Frequência angular da onda) = {wNotacao} rad/s")    
        print()

    elif(opcao == '3'):
        k = float(input("Digite o valor de K (rad/m): "))
        comprimento, f, w = nOndaInput(k)

        comprimentoNotacao = "{:.4e}".format(comprimento)
        fNotacao = "{:.4e}".format(f)
        wNotacao = "{:.4e}".format(w)

        print()
        print(f"λ (Comprimento de onda) = {comprimentoNotacao} m")
        print(f"F (Frequência) = {fNotacao} Hz")
        print(f"W (Frequência angula da onda) = {wNotacao} rad/s")
        print()

    elif(opcao == "4"):
        w = float(input("Digite o valor de W (rad/s): "))
        comprimento, f, k = freqAngInput(w)

        comprimentoNotacao = "{:.4e}".format(comprimento)
        fNotacao = "{:.4e}".format(f)
        kNotacao = "{:.4e}".format(k)

        print()
        print(f"λ (Comprimento de onda) = {comprimentoNotacao} m")
        print(f"K (Número de onda) = {kNotacao} rad/m")
        print(f"F (Frequência) = {fNotacao} Hz")
        print()
        
    elif(opcao == '5'):
        bm = float(input("Digite a amplitude do campo magnético (Bm) (T): "))
        
        em, i = bmInput(bm)
    
        emNotacao = "{:.4e}".format(em)
        iNotacao = "{:.4e}".format(i)
        
        print()
        print(f"Em - Amplitude do Campo Elétrico = {emNotacao} V/m")
        print(f"Intensidade da Onda {iNotacao} W/m^2")
        print()

    elif(opcao == '6'):
        em = float(input("Digite a amplitude do campo elétrico (Em) (V): "))

        bm, intensidade = emInput(em)

        bmNotacao = "{:.4e}".format(bm)
        intensidadeNotacao = "{:.4e}".format(intensidade)

        print()
        print(f"Bm (Amplitude do campo magnético) = {bmNotacao} T")
        print(f"I (Intensidade da onda) = {intensidadeNotacao} w/m²")
        print() 

    elif(opcao == '7'):
        intensidade = float(input("Digite a intensidade da onda eletromagnética (I) (w/m²): "))

        bm, em = intensidadeInput(intensidade)

        bmNotacao = "{:.4e}".format(bm)
        emNotacao = "{:.4e}".format(em)

        print()
        print(f"Bm (Amplitude do campo magnético) = {bmNotacao} T")
        print(f"Em (Amplitude do campo elétrico) = {emNotacao} V/m")
        print()

    elif(opcao == '8'):
        
        print()
        
    elif(opcao == '0'):
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
        print()
    
    