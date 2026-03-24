import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

def exibir_nome_do_programa():
    """
    Exibe o nome estilizado do programa no terminal.
    """
    print("""
 
 ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗███████╗██████╗░██████╗░███████╗░██████╗░██████╗
 ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
 ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░█████╗░░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
 ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔══╝░░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
 ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗███████╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
 ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    """
    Exibe as opções disponíveis para o usuário no menu principal.
    """
    print("1. Cadastrar restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no terminal.

    Parâmetros:
    - texto (str): Texto que será exibido como subtítulo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    """
    Finaliza a execução do programa exibindo uma mensagem de encerramento.
    """
    exibir_subtitulo("Encerrando o programa")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    """
    Exibe uma mensagem de erro quando o usuário escolhe uma opção inválida.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista.

    Solicita ao usuário:
    - Nome do restaurante
    - Categoria

    Adiciona o restaurante com status inativo.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados com nome, categoria e status.
    """
    exibir_subtitulo('Listando os restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status\n")

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f"- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/inativo) de um restaurante.

    Solicita o nome do restaurante e altera seu status.
    """
    exibir_subtitulo('Alternando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            encontrado = True
            restaurante['ativo'] = not restaurante['ativo']

            if restaurante['ativo']:
                print(f'O restaurante {nome_restaurante} foi ativado com sucesso')
            else:
                print(f'O restaurante {nome_restaurante} foi desativado com sucesso')

    if not encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Lê a opção escolhida pelo usuário e direciona para a função correspondente.

    Trata erros de entrada inválida.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():
    """
    Função principal do programa.

    Responsável por iniciar o sistema, exibir o menu e capturar a escolha do usuário.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
