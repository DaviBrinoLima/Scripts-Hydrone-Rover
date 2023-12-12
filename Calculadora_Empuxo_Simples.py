def calculadora_empuxo():
    diametro= float(input("Insira o diamêtro do círculo em mm: "))
    raio= (diametro/2)/1000
    area_circulo= 3.14*(raio**2)


    comprimento_lateral= float(input("Insira o comprimento dos Cascos laterais em metros: "))
    volume_lateral= (area_circulo*comprimento_lateral)


    comprimento_central= float(input("Insira o comprimento do Casco Central em metros: "))
    volume_central= (area_circulo*comprimento_central)


    calado= float(input("Insira quantos porcento de calado está sendo considerado (De Forma Decimal): "))
    densidade= float(input("Insira qual a densidade do ambiente em que o Trimarã está: "))
    gravidade= float(input("Insira qual valor é considerado para a gravidade: "))
    volume= (volume_lateral*2)+volume_central


    empuxo= densidade*gravidade*(volume*calado)
    massa= round(empuxo/gravidade, 2)


    print(f"A massa que o trimarã consegue suportar é: {massa} kg")
    print(volume)
    print(empuxo)

if __name__=='__main__':
    calculadora_empuxo()