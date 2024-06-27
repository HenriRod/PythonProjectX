usuario = "khk"
senha = 123

inputusuario = input("digite seu usuario")

if inputusuario == usuario:
    inputsenha = input("digite sua senha")
    if inputsenha == senha:
        print(f"Bem vindo {usuario}! ")
    else:
        print(f"senha incorreta! voce realmente é {usuario} ?")
else:
    print("usuario incorreto")