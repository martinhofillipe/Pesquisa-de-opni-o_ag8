# contadores
excelente = 0
ruim = 0

# loop para 10 entrevistados
for i in range(10):
    print(f"\nEntrevistado {i + 1}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    # estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

        # resultado final
        print("\nResultado da pesquisa:")
        print(f"Quantidade de pessoas que responderam EXCELENTE: {excelente}")
        print(f"Quantidade de pessoas que responderam RUIM: {ruim}")