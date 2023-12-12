import argparse

def calculator_reverse_empuxo():
    carga= float(input("Insira quantos Kg o barco precisa aguentar: "))
    comprimento_lateral= float(input("Insira quantos metros os cascos laterais tem de comprimento: "))
    comprimento_meio= float(input("Insira quantos metros o casco centro tem de comprimento: "))


    escolha_gravidade= float(input("Qual valor deve considerado para a Gravidade? 9.8 ou 10 m/s**2?"))
    if escolha_gravidade == 9.8:
        gravidade= escolha_gravidade

    else:
        gravidade= escolha_gravidade

    
    escolha_densidade: input("Qual densidade deve ser considerada? água ou outro?")
    if escolha_densidade == 'água':
        densidade= 1000

    else:
        densidade= float(input("Insira a densidade do fluído em Kg/m**3: "))

    

    empuxo= carga*gravidade


