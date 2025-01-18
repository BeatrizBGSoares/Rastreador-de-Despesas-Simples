import os

ARQUIVO_DESPESAS = 'despesas.txt'

def carregar_despesas():
    if not os.path.exists(ARQUIVO_DESPESAS):
        return []
    
    with open(ARQUIVO_DESPESAS, 'r') as arquivo:
        despesas = arquivo.readlines()
    
    return [linha.strip() for linha in despesas]

def salvar_despesa(nome, valor, categoria):
    with open(ARQUIVO_DESPESAS, 'a') as arquivo:
        arquivo.write(f"{nome},{valor},{categoria}\n")
    print(f"Despesa de {nome} no valor de R${valor} na categoria '{categoria}' adicionada com sucesso!")

def listar_despesas():
    despesas = carregar_despesas()
    if not despesas:
        print("Nenhuma despesa registrada.")
        return
    
    print("\nDespesas registradas:")
    for despesa in despesas:
        nome, valor, categoria = despesa.split(',')
        print(f"Nome: {nome} | Valor: R${valor} | Categoria: {categoria}")
    
def calcular_total():
    despesas = carregar_despesas()
    total = 0.0
    for despesa in despesas:
        _, valor, _ = despesa.split(',')
        total += float(valor)
    print(f"\nTotal de despesas: R${total:.2f}")

def menu():
    while True:
        print("\n----- Rastreador de Despesas -----")
        print("1. Adicionar Despesa")
        print("2. Listar Despesas")
        print("3. Calcular Total")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome da despesa: ")
            valor = float(input("Valor da despesa (R$): "))
            categoria = input("Categoria da despesa: ")
            salvar_despesa(nome, valor, categoria)
        elif escolha == '2':
            listar_despesas()
        elif escolha == '3':
            calcular_total()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()
