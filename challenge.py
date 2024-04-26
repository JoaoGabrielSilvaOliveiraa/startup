from datetime import date
import calendar 

usuarios = []





def mostrar():
    print("Escolha a opção abaixo:")
    print('1. Agendar com o mecânico')
    print('2. Verificar custo de serviços')
    print('3. Fazer Cadastro')
    print('4. Sair')
    return int(input("Escolha uma opção: "))

def verificar_fim_de_semana(dia):
    if dia == 5:  # 5 representa sábado e 6 representa domingo na biblioteca calendar
        print("Sábado! Por favor, insira outro dia.")
        return True
    elif dia == 6:
        print("Domingo! Por favor, insira outro dia.")
        return True
    else:
        return False

def agendar_mecanico():
    while True:
        ano = int(input("Digite o ano: "))
        mes = int(input("Digite o mês (número): "))
        print(calendar.month(ano, mes))
        dia = int(input("Digite o dia: "))

        while verificar_fim_de_semana(calendar.weekday(ano, mes, dia)):
            dia = int(input("Digite outro dia: "))
        
        print("Dia cadastrado com sucesso:", dia, "/", mes, "/", ano)
        
        voltar = input("Deseja voltar ao menu principal? (s/n): ")
        if voltar.lower() != 's':
            return
       
            
        
    

usuarios = []

def fazer_cadastro():
    while True:
        email = input("Digite o seu email: ")
        
        if any(usuario[0] == email for usuario in usuarios):
            print("Este email já está cadastrado. Por favor, faça login.")
            return
        
        senha = input("Digite a sua senha: ")
        confirmar_senha = input("Digite novamente a sua senha para confirmar: ")
        
        if senha == confirmar_senha:
            usuarios.append([email, senha])
            print("Usuário cadastrado com sucesso.")
        else:
            print("As senhas não coincidem. Por favor, tente novamente.")
        
        voltar = input("Deseja voltar ao menu principal? (s/n): ")
        if voltar.lower() != 's':
            break


def verificar_custos():
    while True:
        custos_servicos = {
            1: 200,  # Custo da troca de óleo
            2: 300,  # Custo da troca de pneu
            3: 500   # Custo da manutenção preventiva
        }

        print("Escolha o serviço para verificar o custo:")
        print('1. Troca de óleo')
        print('2. Troca de pneu')
        print('3. Manutenção preventiva')
        
        escolha_servico = int(input("Escolha um serviço (1, 2 ou 3): "))
        
        if escolha_servico in custos_servicos:
            custo = custos_servicos[escolha_servico]
            print(f"O custo do serviço é R${custo}.")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        
        voltar = input("Deseja voltar ao menu principal? (s/n): ")
        if voltar.lower() != 's':
            break

def menu():
    while True:
        opcao = mostrar()
        
        if opcao == 1:
            agendar_mecanico()
        elif opcao == 2:
            verificar_custos()
        elif opcao == 3:
            fazer_cadastro()
        elif opcao == 4:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()

