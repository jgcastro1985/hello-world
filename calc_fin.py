import math
print()
print('Bem-vindo(a)! Esse é meu programa para fazer cálculos financeiros em Python!')
print('Digite o numeral correspondente a opção que deseja calcular')
print('LEMBRE-SE: Digite "." ao invés de "," para as casas decimais')
print('"1": Montante Final')
print('"2": Montante Inicial')
#print('"3": Taxa de juros')
print('"3": Período')
print('"4": Montante periódico')
print()
valor = float(input())
print()
if valor == 1:
    a_z = float(input('Digite o Montante Inicial: R$ ' ))
    q = float(input('Digite a Taxa de juros (% ao mês): '))/100+1
    n = float(input('Digite o período (em meses): '))
    x = float(input('Digite o Montante periódico (por mês): R$ '))
    a_n = int(100*((a_z*(q**n))+(x*(q**n-1)/(q-1))))/100
    print()
    print('O Montante Final é de: R$', a_n)
    print()
    print('Obrigado por utilizar meu programa para fazer cálculos financeiros em Python!')
    print()
else:
    if valor == 2:
        a_n = float(input('Digite o Montante Final: R$ '))
        q = float(input('Digite a Taxa de juros (% ao mês): '))/100+1
        n = float(input('Digite o período (em meses): '))
        x = float(input('Digite o Montante periódico (por mês): R$ '))
        a_z = int(100*(a_n-x*(q**n-1)/(q-1))/(q**n))/100
        print()
        print('O Montante Inicial é de: R$', a_z)
        print()
        print('Obrigado por utilizar meu programa para fazer cálculos financeiros em Python!')
        print()
    else:
#        if valor == 3:
#            a_n = float(input('Digite o Montante Final: R$ '))
#            a_z = float(input('Digite o Montante Inicial: R$ '))
#            n = float(input('Digite o período (em meses): '))
#            r = float(input('Digite o Montante periódico (por mês): R$ '))
#            def f(x, n, a_n, a_z, r):
#                return (a_z * x**(n+1)) + ((r-a_z) * x**n) - (a_n * x) + a_n - r
#            q = scipy.optimize.brentq(f, 0.0, 100.0)
#            q = int((q-1)*1000000)/10000
#            print()
#            print('A taxa de juros é de:', q)
#            print()
#            print('Obrigado por utilizar meu programa para fazer cálculos financeiros em Python!')
#            print()
#        else:
        if valor == 3:
            a_n = float(input('Digite o Montante Final: R$ '))
            a_z = float(input('Digite o Montante Inicial: R$ '))
            q = float(input('Digite a Taxa de juros (% ao mês): '))/100+1
            x = float(input('Digite o Montante periódico (por mês): R$ '))
            n = int(math.log((a_n-x-a_n*q)/(a_z-x-a_z*q),q))+1
            print()
            print('O Período é de', n, 'meses')
            print()
            print('Obrigado por utilizar meu programa para fazer cálculos financeiros em Python!')
            print()
        else:
            if valor == 4:
                a_n = float(input('Digite o Montante Final: R$ '))
                a_z = float(input('Digite o Montante Inicial: R$ '))
                q = float(input('Digite a Taxa de juros (% ao mês): '))/100+1
                n = float(input('Digite o período (em meses): '))
                x = int((a_n-a_z*(q**n))*100*(q-1)/(q**n-1))/100
                print()
                print('O Montante periódico é de: R$', x)
                print()
                print('Obrigado por utilizar meu programa para fazer cálculos financeiros em Python!')
                print()
            else:
                print()
                print('Favor escolher um valor válido!')
                print()
