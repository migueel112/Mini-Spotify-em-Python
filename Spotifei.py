def fazer_cadastro():
    print("\n=== FAZER CADASTRO ===\n")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    confirmacao_senha = input("Confirme a senha: ")

    if "@" not in email:
        print("\nO email deve conter '@'. Tente novamente.\n")
        return fazer_cadastro()
    if len(senha) < 6:
        print("\nA senha deve ter pelo menos 6 caracteres. Tente novamente.\n")
        return fazer_cadastro()
    if senha != confirmacao_senha:
        print("\nAs senhas não coincidem. Tente novamente.\n")
        return fazer_cadastro()

    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(f"{email},{senha}\n")
    print("\nCadastro realizado com sucesso!\n")


def entrar():
    print("\n=== FAZER LOGIN ===\n")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    try:
        with open("cadastros.txt", "r") as arquivo:
            for linha in arquivo:
                if linha.strip() == f"{email},{senha}":
                    print("\nLogin bem-sucedido!\n")
                    maindois(email)
                    return
    except FileNotFoundError:
        print("\nNenhum cadastro encontrado. Por favor, cadastre-se primeiro.\n")
        return
    print("\nEmail ou senha incorretos. Tente novamente.\n")


def escolha_menu_um():

    print("\n=== BEM-VINDO AO SPOTIFEI! ===")
    print("O seu app de música.\n")
    print("Escolha uma das opções:")
    print("1 - Fazer cadastro")
    print("2 - Fazer login")
    print("3 - Sair\n")
    escolha = int(input("Digite o número da opção desejada: "))
    if escolha == 1:
        fazer_cadastro()
    elif escolha == 2:
        entrar()
    elif escolha == 3:   
       sair()
    else:
        print("Opção inválida. Tente novamente.")
        return escolha_menu_um()

def sair():
    print("\nSaindo do programa...\n")
    exit()

def mainUm():
    while True:
        escolha = escolha_menu_um()
        if escolha == 1:
            fazer_cadastro()
        elif escolha == 2:
            entrar()
        elif escolha == 3:
            print("\nSaindo do programa...\n")
            break


def maindois(email):
    while True:
        print("\n=== MENU PRINCIPAL ===\n")
        print("1 - Buscar músicas")
        print("2 - Criar playlists")
        print("3 - Gerenciar playlists")
        print("4 - Ver histórico")
        print("5 - Listar informações sobre uma música")
        print("6 - Curtir ou descurtir uma música")
        print("7 - Ver músicas curtidas e descurtidas")
        print("8 - Sair para o menu de login\n")

        while True:
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha in [1, 2, 3, 4, 5, 6, 7, 8]:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Digite um número válido.")

        if escolha == 1:
            print("\nVocê escolheu buscar uma música.\n")
            buscar_musica(email)
        elif escolha == 2:
            print("\nVocê escolheu criar uma playlist.\n")
            criar_playlist(email)
        elif escolha == 3:
            print("\nVocê escolheu gerenciar uma playlist.\n")
            gerenciar_playlist(email)
        elif escolha == 4:
            print("\nVocê escolheu ver o histórico.\n")
            historico(email)
        elif escolha == 5:
            print("\nVocê deseja listar informações sobre uma música.\n")
            listar_info_musica(email)
        elif escolha == 6:
            curtir_musica(email)
        elif escolha == 7:
            try:
                print("\nVocê escolheu ver suas músicas curtidas ou descurtidas\n")

                print("1 - Músicas curtidas")
                print("2 - Músicas descurtidas")
                print("3 - Voltar ao menu principal\n")
                escolha = int(input("Escolha uma opção:"))
                if escolha == 1:
                    with open(f"musicas_curtidas_{email}.txt", "r") as arquivo:
                        conteudo = arquivo.readlines()
                        if conteudo:
                            print("\nMúsicas curtidas:")
                            for linha in conteudo:
                                print(linha.strip())
                        else:
                            print("\nNenhuma música curtida.\n")
                elif escolha == 2:
                    with open(f"musicas_descurtidas_{email}.txt", "r") as arquivo:
                        conteudo = arquivo.readlines()
                        if conteudo:
                            print("\nMúsicas descurtidas:")
                            for linha in conteudo:
                                print(linha.strip())
                        else:
                            print("\nNenhuma música descurtida.\n")
                elif escolha == 3:
                    return maindois(email)
            except FileNotFoundError:
                print("Arquivo não encontrado.")
        elif escolha == 8:
            print("\nSaindo para o menu de login...\n")
            return mainUm()


def buscar_musica(email):
    musica_procurada = input("Digite o nome da música que deseja buscar: ")
    try:
        with open("musicas.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return maindois(email)

    for linha in conteudo:
        musica, artista, ano = map(str.strip, linha.split(","))
        if musica_procurada.lower() in musica.lower():
            print(f"\nMúsica '{musica_procurada}' encontrada!")
            print(f"Música: {musica}, Artista: {artista}, Ano: {ano}\n")
            with open(f"historico_{email}.txt", "a") as historico:
                historico.write(f"{musica},{artista},{ano}\n")
            return maindois(email)

    print(f"\nMúsica '{musica_procurada}' não encontrada.\n")
    return maindois(email)


def curtir_musica(email):
    print("\nVocê deseja curtir ou descurtir uma música?")
    print("1 - Curtir")
    print("2 - Descurtir")
    print("3 - Voltar ao menu principal\n")
    try:
        escolha = int(input("Digite o número da opção desejada: "))
        if escolha == 1:
            musica_procurada = input("Digite o nome da música que deseja curtir: ")
            try:
                with open("musicas.txt", "r") as arquivo:
                    conteudo = arquivo.readlines()
            except FileNotFoundError:
                print("Arquivo de músicas não encontrado.")
                return maindois(email)

            for linha in conteudo:
                musica, artista, ano = linha.strip().split(",")
                if musica_procurada.lower() in musica.lower():
                    with open(f"musicas_curtidas_{email}.txt", "a") as arquivo_curtidas:
                        arquivo_curtidas.write(f"{musica},{artista},{ano}\n")
                    print(f"\nMúsica '{musica_procurada}' adicionada às músicas curtidas.\n")
                    return maindois(email)

            print(f"\nMúsica '{musica_procurada}' não encontrada.\n")
        elif escolha == 2:
            Descurtir_musica(email)
        elif escolha == 3:
            print("Voltando ao menu principal...\n")
    except ValueError:
        print("Digite um número válido.")
    return maindois(email)


def Descurtir_musica(email):
    musica_procurada = input("Digite o nome da música que deseja descurtir: ")
    try:
        with open("musicas.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return maindois(email)

    for linha in conteudo:
        musica, artista, ano = linha.strip().split(",")
        if musica_procurada.lower() in musica.lower():
            with open(f"musicas_descurtidas_{email}.txt", "a") as arquivo_descurtidas:
                arquivo_descurtidas.write(f"{musica},{artista},{ano}\n")
            print(f"\nMúsica '{musica_procurada}' adicionada às músicas descurtidas.\n")
            return maindois(email)
    print(f"\nMúsica '{musica_procurada}' não encontrada.\n")
    return maindois(email)


def criar_playlist(email):
    nome_playlist = input("Digite o nome da nova playlist: ")
    with open(f"playlists_{email}.txt", "a") as arquivo:
        arquivo.write(f"{nome_playlist}\n")
    print(f"\nPlaylist '{nome_playlist}' criada com sucesso!\n")
    return maindois(email)


def gerenciar_playlist(email):
    playlist_gerenciada = input("Digite o nome da playlist que deseja gerenciar: ")
    try:
        with open(f"playlists_{email}.txt", "r") as arquivo:
            playlists = [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        print("Você não possui playlists ainda.")
        return maindois(email)

    if playlist_gerenciada in playlists:
        print("\n1 - Adicionar música")
        print("2 - Remover música")
        print("3 - Excluir playlist")
        print("4 - Voltar ao menu principal\n")
        try:
            escolha = int(input("Digite o número da opção desejada: "))
            if escolha == 1:
                return adicionar_musica(email, playlist_gerenciada)
            elif escolha == 2:
                return remover_musica(email, playlist_gerenciada)
            elif escolha == 3:
                return excluir_playlist(email, playlist_gerenciada)
            elif escolha == 4:
                return maindois(email)
        except ValueError:
            print("Digite um número válido.")
    else:
        print("Playlist não encontrada.")
    return maindois(email)


def adicionar_musica(email, playlist_gerenciada):
    nome_musica = input("Digite o nome da música que deseja adicionar: ")
    with open(f"playlists_{email}.txt", "a") as arquivo:
        arquivo.write(f"{playlist_gerenciada}: {nome_musica}\n")
    print(f"\nMúsica '{nome_musica}' adicionada à playlist '{playlist_gerenciada}'.\n")
    return maindois(email)


def remover_musica(email, playlist_gerenciada):
    nome_musica = input("Digite o nome da música que deseja remover: ")
    try:
        with open(f"playlists_{email}.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Você não possui playlists ainda.")
        return maindois(email)

    encontrou = False
    with open(f"playlists_{email}.txt", "w") as arquivo:
        for linha in linhas:
            if linha.strip() != f"{playlist_gerenciada}: {nome_musica}":
                arquivo.write(linha)
            else:
                encontrou = True
    if encontrou:
        print(f"\nMúsica '{nome_musica}' removida da playlist '{playlist_gerenciada}'.\n")
    else:
        print(f"\nMúsica '{nome_musica}' não encontrada na playlist '{playlist_gerenciada}'.\n")
    return maindois(email)


def excluir_playlist(email, playlist_gerenciada):
    with open(f"playlists_{email}.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open(f"playlists_{email}.txt", "w") as arquivo:
        for linha in linhas:
            if not (linha.startswith(f"{playlist_gerenciada}:") or linha.strip() == playlist_gerenciada):
                arquivo.write(linha)

    print(f'\nPlaylist "{playlist_gerenciada}" excluída com sucesso!\n')
    return maindois(email)


def historico(email):
    try:
        with open(f"historico_{email}.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
            if conteudo:
                print("\nHistórico de músicas:")
                for linha in conteudo:
                    print(linha.strip())
            else:
                print("\nNenhum histórico encontrado.\n")
    except FileNotFoundError:
        print("\nNenhum histórico encontrado.\n")
    return maindois(email)


def listar_info_musica(email):
    musica_procurada = input("Digite o nome da música para ver informações: ")
    try:
        with open("musicas.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print("Arquivo de músicas não encontrado.")
        return maindois(email)

    for linha in conteudo:
        musica, artista, ano = map(str.strip, linha.split(","))
        if musica_procurada.lower() in musica.lower():
            print(f"\nInformações da música:\nMúsica: {musica}\nArtista: {artista}\nAno: {ano}\n")
            return maindois(email)
    print("\nMúsica não encontrada.\n")
    return maindois(email)


if __name__ == "__main__":
    mainUm()
