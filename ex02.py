'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

nome_usuario = str(input("Digite seu nome: "))
senha_usuario = str(input("Senha: "))

while nome_usuario == senha_usuario:
    senha_usuario = str(input("A senha deve ser diferente do nome de usuário. \nSenha: "))
print(f"Nome: {nome_usuario} \nSenha: {senha_usuario} \nCadastro concluído com sucesso!")