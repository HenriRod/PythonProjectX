# A.
#if ( 2 + 2 < 4 ):
#    print(True)
#else:
#    print(False)

# B.
#if ( 7 // 3 == 1 + 1 ):
#    print(True)
#else:
#    print(False)

# C.
#if ( ( 3**2 + 4**2 ) == 25 ):
#    print(True)
#else:
#    print(False)

# D.
#if ( 2 + 4 + 6 > 12 ):
#    print(True)
#else:
#    print(False)




# A.
#if ( 1387 % 19 == 0):
#    print(True)
#else:
#    print(False)

# B.
#if ( 31 % 2 == 0 ):
#    print(True)
#else:
#    print(False)

# C.
#if ( min (34, 29, 31) < 30 ):
#    print(True)
#else:
#    print(False) 





# A.
#idade = 69
#if idade > 60:
#    print("Você tem direitos aos beneficios")

# B.
#dano = 15
#escudo = 0
#if dano > 10 and escudo == 0:
#    print("Você esta morto")

# C.
#norte = False
#sul = False
#leste = False
#oeste = False
#if ((norte or sul or leste or oeste ) == True):
#    print("Você escapou")



# A.
#ano = 368
#if ano % 4 == 0:
#    print("Pode ser um ano bissexto")
#else:
#    print("Definitivamente não é um ano bissexto")

# B.
#cima = True
#baixo = True
#if ( cima and baixo ) == True:
#    print ("Você escolheu um caminho! ")
#else:
#    print("Decida-se!")



# A.

#a = 3
#b = 3
#c = 3
#if (a>0 and b>0 and c>0) and (a+b>c and a+c>b and b+c>a):
#    #se chegou até aqui é porque é um triangulo valido!
#    if a==b==c:
#        print("Equilátero")
#    elif a==b or a==c or b==c:
#        print("Isósceles")
#    elif a!=b and a!=c and b!=c:
#        print("Escaleno")
#else:
#    print("Não é um triangulo")


# B.

um = float(input(" Digite o primeiro número "))
dois = float(input(" Digite o segundo número "))
simbolo = input("Digite o simbolo + , - , * , / ")

if simbolo == "+":
    print(f"{um + dois}")
elif simbolo == "-":
    print(f"{um - dois}")
elif simbolo == "*":
    print(f"{um * dois}")
elif simbolo == "/":
    print(f"{um / dois}")