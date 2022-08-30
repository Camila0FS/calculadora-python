"Programa_calculadora"
"Descrição - realiza operações aritiméticas"
"Usuário: Camila Freitas Sant´Ana"
"Versão: 0.0.9 VRS Final" 
"Data: 30/08/2022"

#Entrada de dados

def soma(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mult(x,y):
    return(x*y)

def div(x,y):
    return(x/y)

opcao = 1
print("0. Sair")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicação")
print("4. Divisão ")

# Processamento de dados

while opcao:
    opcao = int(input("Escolha uma das opções acima. "))
    if opcao > 4:
        print("Escolha uma opção válida!")
        continue;
    
    else:
        numero_1=float(input("Primeiro número: \n"))
        numero_2=float(input("Segundo número: \n"))
 
 # Saída de dados
        if opcao == 1:
            print("O resultado de ",numero_1,"+",numero_2,"é igual a: ",soma(numero_1,numero_2))
        elif opcao == 2:
            print("O resultado de ",numero_1,"-",numero_2,"é igual a: ",sub(numero_1,numero_2))
        elif opcao == 3:
            print("O resultado de ",numero_1,"*",numero_2,"é igual a: ",mult(numero_1,numero_2))
        elif opcao == 4:
            print("O resultado de ",numero_1,"/",numero_2,"é igual a: ",div(numero_1,numero_2))

