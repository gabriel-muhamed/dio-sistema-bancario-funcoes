import random
from datetime import date

home_menu = """
=============================

[e] Entrar
[c] Cadastrar

=============================

=> """

login_cpf_menu = """
=============================

Insira o CPF para entrar!

=============================

=> """

options_menu = """
=============================

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

=============================

=> """

## Catch today
today = date.today()
formatted_date = today.strftime('%d/%m/%Y')

## Register/Login
def create_current_account():
    number = ''.join(random.choices('0123456789', k=5))
    final_number = ''.join(random.choices('0123456789', k=1))
    account_number = "000" + number + "-" + final_number
    return account_number

def register_cpf(users):
    cpf = numeric_only("Digite o seu CPF => ")
    
    if not verify_user_exist(cpf, users):
        name = input("Digite o seu Nome => ")
        city = input("Digite a sua cidade e o seu estado => ")
        neighborhood = input("Digite o seu bairro => ")
        house_number = input("Digite o número da sua casa => ")
        address = (city + ", " + neighborhood + ", " + house_number)
        birth = input("Digite a sua data de nascimento => ")
        account_number = create_current_account()

        user_infos = {
            'Nome': name,
            'Data de Nascimento': birth,
            'CPF': cpf,
            'Endereço': address,
            'Conta': account_number
        }

        users.append(user_infos)
        print('Usuário cadastrado no sistema!')
    else:
        print('Usuário já cadastrado!')

def numeric_only(prompt):
    while True:
        input_value = input(prompt)
            
        if input_value.isdigit() and len(input_value) == 11:
            return (input_value)
        elif not input_value.isdigit():
            print("Insira apenas números!")
        else:
            print("Insira um CPF válido")

def verify_user_exist(cpf, users):
    for user in users:
        if cpf == user['CPF']:
            return True
    return False

## Deposit
def deposit(deposit_value, account_balance, account_statement):
    account_balance = account_balance + int(deposit_value)
    added = {
        'Data' : formatted_date,
        'Valor' : 'R$' + deposit_value
    }

    account_statement.append(added)

    print(f"Valor de R${deposit_value} depositado!")
    return account_balance

# Withdraw
def withdraw(withdraw_value, account_balance, account_statement):
    if account_balance >= int(withdraw_value):
        account_balance = account_balance - int(withdraw_value)
        withdrawal = {
            'Data' : formatted_date,
            'Valor' : '-R$' + withdraw_value
        }
        print(f"Valor de R${withdraw_value} sacado!")
        account_statement.append(withdrawal)
        return account_balance
    elif account_balance < int(withdraw_value):
        print("Valor indisponível para saque!")
        return account_balance

# Statement
def statement(account_statement, balance):
    print(f'Extrato: {account_statement}')
    print(f'Saldo: {balance}')


## Account variables
users = [{'Nome': 'Joaquim', 'Data de Nascimento': '20/01/1988', 'CPF': '12345678910', 'Endereço': 'Curitiba - PR, Bairro Joaquim, 123', 'Conta': '00044497-6'}]

while True:
    ## Account Variables
    account_balance = 0
    account_statement = []

    ## Login/Register
    home = input(home_menu).lower()
        
    if home == "u":
        print(users)
    elif home == "e":
        cpf = numeric_only(login_cpf_menu)
        if verify_user_exist(cpf, users):
            logged_in_user = True
            while logged_in_user == True:
                options = input(options_menu)
                # Deposit
                if options ==  'd':
                    deposit_value = input("Insira o valor que deseja depositar => ")
                    account_balance = deposit(deposit_value, account_balance, account_statement)
                elif options == 's':
                    withdraw_value = input("Insira o valor de saque => ")
                    account_balance = withdraw(withdraw_value=withdraw_value, account_balance=account_balance, account_statement=account_statement)
                elif options == 'e':
                    statement(account_statement, balance=account_balance)
                elif options == 'q':
                    print("Você deslogou!")
                    logged_in_user = False
                else:
                    print("Comando não identificado")     
        elif not verify_user_exist(cpf, users):
            print("Usuário não existente ou CPF incorreto!")
    elif home == "c":
        register_cpf(users=users)
    else:
        print("Comando não identificado")
