while True:
    print("1: Juros\n2: sair")
    try:
        escolha = int(input("Opeçao: "))
        if escolha == 1:
            p = float(input('Valor Inicial: '))
            r = float(input('Numero de Juros: '))
            n = int(input('Numero de Anos: '))
            a = p*(1 + (r/100))**n
            print( 'Depois de '+str(n)+ ' se investtir '+str(p)+ ' vai ter um retorno de '+str(round(a,2))+'€')
        elif escolha == 2:
            break
    except:
        Ex_Ficheiro("!!!!ERRO!!!")
        print("ERRO!!!")
print("A sair...")
exit()