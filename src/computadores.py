from utils import obter_data_atual, carregar_dados, salvar_dados #importando as funções obter_data_atual, carregar_dados e salvar_dados do arquivo utils.py

ARQUIVO_COMPUTADORES = "computadores.json" #constante que salva Arquivo onde os dados dos computadores serão salvos

def carregar_computadores(): #Função para carregar os dados dos computadores do arquivo JSON
    return carregar_dados(ARQUIVO_COMPUTADORES) #Chama a função carregar_dados do arquivo utils.py, passando o nome do arquivo JSON onde os dados dos computadores estão salvos, e retorna os dados carregados

def salvar_computadores(lista_computadores): #Função para salvar os dados dos computadores no arquivo JSON
    return salvar_dados(lista_computadores, ARQUIVO_COMPUTADORES) #Chama a função salvar_dados do arquivo utils.py, passando a lista de computadores e o nome do arquivo JSON onde os dados dos computadores devem ser salvos, e retorna o resultado da operação de salvamento

def gerar_novo_id(lista_computadores): #Função para gerar um novo ID para um computador
    if not lista_computadores: #Verifica se a lista de computadores está vazia
        return 1 #Se estiver vazia, retorna 1 como o primeiro ID
    else:
        ids = [computador["id"] for computador in lista_computadores] #Cria uma lista de IDs dos computadores existentes
        return max(ids) + 1 #Retorna o próximo ID disponível, que é o máximo ID existente mais 1

def buscar_computador_id(lista_computadores, id_computador):
    for computador in lista_computadores: #Percorre a lista de computadores
        if computador["id"] == id_computador: #Verifica se o ID do computador atual é igual ao ID buscado
            return computador #Se for igual, retorna o computador encontrado
    return None

def cadastrar_computador(lista_computadores): #Cadastra novo computador no sistema
    print("\n" + "="*50) #Estilização visual para separar as seções do programa
    print("📝 CADASTRO DE NOVO COMPUTADOR")#Estilização visual para separar as seções do programa
    print("="*50)#Estilização visual para separar as seções do programa

    nome = input("Digite o nome do computador: ").strip() #Solicita ao usuário que digite o nome do computador e armazena na variável nome
    tipo = input("Tipo (Desktop/Notebook/All-in-One): ").strip() #Solicita o tipo da maquina
    modelo = input("Modelo (ex: Dell OptiPlex 3080): ").strip() #Solicita o modelo da maquina
    processador = input("Processador (ex: Intel Core i5-10400): ").strip() #Solicita o Processador
    memoria_ram = input("Memória RAM (ex: 8GB, 16GB): ").strip() #Solicita a quantidade de memória RAM
    armazenamento = input("Armazenamento (ex: 256GB SSD, 1TB HD): ").strip() #Solicita a capacidade de armazenamento
    sistema_operacional = input("Sistema Operacional (ex: Windows 11 Pro): ").strip() #Solicita o sistema operacional instalado
    localizacao = input("Localização (ex: Laboratório - Sala 201): ").strip()  #Solicita a localização do computador
    departamento = input("Departamento (ex: TI, Administrativo): ").strip() #Solicita o departamento responsável pelo computador

    novo_id = gerar_novo_id(lista_computadores) #Gera um novo ID para o computador usando a função gerar_novo_id

    novo_computador = { #Cria um dicionário com os dados do novo computador
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "modelo": modelo,
        "processador": processador,
        "memoria_ram": memoria_ram,
        "armazenamento": armazenamento,
        "sistema_operacional": sistema_operacional,
        "localizacao": localizacao,
        "departamento": departamento,
        "status": "Operacional",
        "data_cadastro": obter_data_atual(),
        "ultima_manutencao": None
    }

    lista_computadores.append(novo_computador) #Adiciona o novo computador a lista de computadores
    salvar_computadores(lista_computadores) #Salva a lista de computadores atualizada no arquivo JSON usando a função salvar_computadores
    print("\n" + "="*50)
    print(f"✅ COMPUTADOR CADASTRADO COM SUCESSO!")
    print(f"   ID: {novo_id}")
    print(f"   Nome: {nome}")
    print("="*50)
    
    return lista_computadores

def deletar_computador(lista_computadores):
    """Remove um computador do sistema."""
    if not lista_computadores:
        print("\nNenhum computador cadastrado ainda!")
        return lista_computadores
    
    print("\n" + "="*50)
    print("DELETAR COMPUTADOR")
    print("="*50)
    
    # Lista computadores de forma resumida
    print("\nCOMPUTADORES CADASTRADOS:")
    print("-"*50)
    for comp in lista_computadores:
        print(f"ID: {comp['id']} | Nome: {comp['nome']} | Status: {comp['status']}")
    print("-"*50)
    
    try:
        id_busca = int(input("\nDigite o ID do computador a deletar: "))
    except ValueError:
        print("ID inválido!")
        return lista_computadores
    
    # Busca o computador
    computador = buscar_computador_id(lista_computadores, id_busca)
    
    if not computador:
        print(f"Computador com ID {id_busca} não encontrado!")
        return lista_computadores
    
    # Confirmação antes de deletar
    print(f"\nATENÇÃO: Você está prestes a deletar:")
    print(f"   ID: {computador['id']}")
    print(f"   Nome: {computador['nome']}")
    print(f"   Localização: {computador['localizacao']}")
    
    confirmacao = input("\nTem certeza? Digite 'SIM' para confirmar: ").strip().upper()
    
    if confirmacao == "SIM":
        lista_computadores.remove(computador)
        salvar_computadores(lista_computadores)
        print(f"\n✅ Computador {computador['nome']} deletado com sucesso!")
    else:
        print("\n❌ Operação cancelada!")
    
    return lista_computadores
def listar_computadores(lista_computadores): #Função para listar os computadores cadastrados no sistema
    if not lista_computadores: #Verifica se a lista de computadores está vazia
        print("\n Não há cadastro de computadores!")
        return
    print("\n" + "="*100)
    print("📋 INVENTÁRIO DE COMPUTADORES")
    print("="*100)
    print(f"{'ID':<5} {'Nome':<25} {'Modelo':<20} {'Status':<15} {'Localização':<20}") #Cabeçalho da tabela com formatação para alinhar as colunas, usando f-string para formatar a string e os especificadores de formatação para definir a largura de cada coluna e o alinhamento dos dados (esquerda, direita ou centralizado)
    print("-"*100)
    for comp in lista_computadores: #Percorre a lista de computadores
                print(f"{comp['id']:<5} {comp['nome']:<25} {comp['modelo']:<20} {comp['status']:<15} {comp['localizacao']:<20}")

    print("="*100)
    print(f"Total de computadores cadastrados: {len(lista_computadores)}")

def listar_computadores_resumido(lista_computadores): #Função para listar os computadores cadastrados no sistema
    """Lista computadores de forma resumida (ID, Nome, Status)."""
    if not lista_computadores:
        print("⚠️ Nenhum computador cadastrado!")
        return
    
    print("\n" + "-"*60)
    print(f"{'ID':<5} {'Nome':<25} {'Status':<15}")
    print("-"*60)
    
    for comp in lista_computadores: #Percorre a lista de computadores
        print(f"{comp['id']:<5} {comp['nome']:<25} {comp['status']:<15}")
    
    print("-"*60)

def exibir_detalhes_computador(computador):
    """Exibe os detalhes de um computador específico."""
    print("\n" + "="*60)
    print(f"💻 DETALHES DO COMPUTADOR - ID: {computador['id']}")
    print("="*60)
    # REMOVA a linha do Patrimônio
    print(f"Nome:              {computador['nome']}")
    print(f"Tipo:              {computador['tipo']}")
    print(f"Modelo:            {computador['modelo']}")
    print(f"Processador:       {computador['processador']}")
    print(f"Memória RAM:       {computador['memoria_ram']}")
    print(f"Armazenamento:     {computador['armazenamento']}")
    print(f"Sistema Operacional: {computador['sistema_operacional']}")
    print(f"Localização:       {computador['localizacao']}")
    print(f"Departamento:      {computador['departamento']}")
    print(f"Status:            {computador['status']}")
    print(f"Data Cadastro:     {computador['data_cadastro']}")
    print(f"Última Manutenção: {computador['ultima_manutencao'] or 'Nenhuma'}")
    print("="*60)
def atualizar_status_computador(lista_computadores): #Função para atualizar o status de um computador específico, recebendo a lista de computadores como parâmetro

    if not lista_computadores: #
        print("\n Nenhum computador cadastrado ainda!")
        return lista_computadores
    
    print("\n" + "="*50)
    print("🔄 ATUALIZAR STATUS DO COMPUTADOR")
    print("="*50)

    listar_computadores_resumido(lista_computadores) #Chama a função listar_computadores_resumido para exibir a lista de computadores de forma resumida, facilitando a escolha do computador para atualização

    try:
        id_busca = int(input ("\nDigite o ID do computador que deseja atualizar o status: ").strip()) #Solicita ao usuário que digite o ID do computador que deseja atualizar o status e armazena na variável id_busca
    except ValueError: #Trata o erro caso o usuário digite um valor que não seja um número inteiro
        print("ID inválido! Por favor, digite um número inteiro.")
        return lista_computadores
    computador = buscar_computador_id(lista_computadores, id_busca) #Chama a função buscar_computador_id para encontrar o computador com o ID digitado pelo usuário e armazena na variável computador
    if not computador: #Verifica se o computador foi encontrado
        print(f"Computador com ID {id_busca} não encontrado!")
        return lista_computadores
    print(f"\nComputador selecionado: {computador['nome']} (ID: {computador['id']})") #Exibe o nome e ID do computador selecionado para atualização
    print("Status atual: ", computador['status']) #Exibe o status atual do computador
    print("\nOpções de status:")
    print("1 - Operacional")
    print("2 - Em Manutenção")
    print("3 - Inativo")
    opcao =input("Digite o número correspondente ao novo status: ").strip() #Solicita ao usuário que digite o número correspondente ao novo status e armazena na variável opcao
    if opcao == "1":
        novo_status = "Operacional"
    elif opcao == "2":
        novo_status = "Em Manutenção"
    elif opcao == "3":
        novo_status = "Inativo"
    else:
        print("❌ Opção inválida!")
        return lista_computadores
    
    computador["status"] = novo_status #Atualiza o status do computador com o novo status selecionado pelo usuário
    if novo_status == "Em Manutenção": #Se o novo status for "Em Manutenção", atualiza a data da última manutenção para a data atual usando a função obter_data_atual
        computador["ultima_manutencao"] = obter_data_atual() #Atualiza a data da última manutenção para a data atual usando a função obter_data_atual do arquivo utils.py
    salvar_computadores(lista_computadores) #Salva a lista de computadores atualizada no arquivo JSON usando a função salvar_computadores
    print(f"\nStatus do computador '{computador['nome']}' atualizado para '{novo_status}' com sucesso!")

    return lista_computadores


    
