from utils import obter_data_atual, carregar_dados, salvar_dados

ARQUIVO_COMPUTADORES = "computadores.json"

def carregar_computadores():
    return carregar_dados(ARQUIVO_COMPUTADORES)

def salvar_computadores(lista_computadores):
    return salvar_dados(lista_computadores, ARQUIVO_COMPUTADORES)

def gerar_novo_id(lista_computadores):
    if not lista_computadores:
        return 1
    else:
        ids = [computador["id"] for computador in lista_computadores]
        return max(ids) + 1

def buscar_computador_id(lista_computadores, id_computador):
    for computador in lista_computadores:
        if computador["id"] == id_computador:
            return computador
    return None

def cadastrar_computador(lista_computadores):
    print("\n" + "="*50)
    print("📝 REGISTER NEW COMPUTER")
    print("="*50)

    nome = input("Enter computer name: ").strip()
    tipo = input("Type (Desktop/Notebook/All-in-One): ").strip()
    modelo = input("Model (e.g., Dell OptiPlex 3080): ").strip()
    processador = input("Processor (e.g., Intel Core i5-10400): ").strip()
    memoria_ram = input("RAM (e.g., 8GB, 16GB): ").strip()
    armazenamento = input("Storage (e.g., 256GB SSD, 1TB HD): ").strip()
    sistema_operacional = input("Operating System (e.g., Windows 11 Pro): ").strip()
    localizacao = input("Location (e.g., Lab - Room 201): ").strip()
    departamento = input("Department (e.g., IT, Administrative): ").strip()

    novo_id = gerar_novo_id(lista_computadores)

    novo_computador = {
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
        "status": "Operational",
        "data_cadastro": obter_data_atual(),
        "ultima_manutencao": None
    }

    lista_computadores.append(novo_computador)
    salvar_computadores(lista_computadores)

    print("\n" + "="*50)
    print("✅ COMPUTER REGISTERED SUCCESSFULLY!")
    print(f"   ID: {novo_id}")
    print(f"   Name: {nome}")
    print("="*50)
    
    return lista_computadores

def deletar_computador(lista_computadores):
    if not lista_computadores:
        print("\nNo computers registered yet!")
        return lista_computadores
    
    print("\n" + "="*50)
    print("DELETE COMPUTER")
    print("="*50)
    
    print("\nREGISTERED COMPUTERS:")
    print("-"*50)
    for comp in lista_computadores:
        print(f"ID: {comp['id']} | Name: {comp['nome']} | Status: {comp['status']}")
    print("-"*50)
    
    try:
        id_busca = int(input("\nEnter the computer ID to delete: "))
    except ValueError:
        print("Invalid ID!")
        return lista_computadores
    
    computador = buscar_computador_id(lista_computadores, id_busca)
    
    if not computador:
        print(f"Computer with ID {id_busca} not found!")
        return lista_computadores
    
    print(f"\nWARNING: You are about to delete:")
    print(f"   ID: {computador['id']}")
    print(f"   Name: {computador['nome']}")
    print(f"   Location: {computador['localizacao']}")
    
    confirmacao = input("\nAre you sure? Type 'YES' to confirm: ").strip().upper()
    
    if confirmacao == "YES":
        lista_computadores.remove(computador)
        salvar_computadores(lista_computadores)
        print(f"\n✅ Computer {computador['nome']} deleted successfully!")
    else:
        print("\n❌ Operation cancelled!")
    
    return lista_computadores

def listar_computadores(lista_computadores):
    if not lista_computadores:
        print("\nNo computers registered!")
        return

    print("\n" + "="*100)
    print("📋 COMPUTER INVENTORY")
    print("="*100)
    print(f"{'ID':<5} {'Name':<25} {'Model':<20} {'Status':<15} {'Location':<20}")
    print("-"*100)

    for comp in lista_computadores:
        print(f"{comp['id']:<5} {comp['nome']:<25} {comp['modelo']:<20} {comp['status']:<15} {comp['localizacao']:<20}")

    print("="*100)
    print(f"Total computers: {len(lista_computadores)}")

def listar_computadores_resumido(lista_computadores):
    if not lista_computadores:
        print("⚠️ No computers registered!")
        return
    
    print("\n" + "-"*60)
    print(f"{'ID':<5} {'Name':<25} {'Status':<15}")
    print("-"*60)
    
    for comp in lista_computadores:
        print(f"{comp['id']:<5} {comp['nome']:<25} {comp['status']:<15}")
    
    print("-"*60)

def exibir_detalhes_computador(computador):
    print("\n" + "="*60)
    print(f"💻 COMPUTER DETAILS - ID: {computador['id']}")
    print("="*60)
    print(f"Name:              {computador['nome']}")
    print(f"Type:              {computador['tipo']}")
    print(f"Model:             {computador['modelo']}")
    print(f"Processor:         {computador['processador']}")
    print(f"RAM:               {computador['memoria_ram']}")
    print(f"Storage:           {computador['armazenamento']}")
    print(f"Operating System:  {computador['sistema_operacional']}")
    print(f"Location:          {computador['localizacao']}")
    print(f"Department:        {computador['departamento']}")
    print(f"Status:            {computador['status']}")
    print(f"Registration Date: {computador['data_cadastro']}")
    print(f"Last Maintenance:  {computador['ultima_manutencao'] or 'None'}")
    print("="*60)

def atualizar_status_computador(lista_computadores):
    if not lista_computadores:
        print("\nNo computers registered yet!")
        return lista_computadores
    
    print("\n" + "="*50)
    print("🔄 UPDATE COMPUTER STATUS")
    print("="*50)

    listar_computadores_resumido(lista_computadores)

    try:
        id_busca = int(input("\nEnter the computer ID to update: ").strip())
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return lista_computadores

    computador = buscar_computador_id(lista_computadores, id_busca)

    if not computador:
        print(f"Computer with ID {id_busca} not found!")
        return lista_computadores

    print(f"\nSelected computer: {computador['nome']} (ID: {computador['id']})")
    print("Current status:", computador['status'])

    print("\nStatus options:")
    print("1 - Operational")
    print("2 - Under Maintenance")
    print("3 - Inactive")

    opcao = input("Enter the number for the new status: ").strip()

    if opcao == "1":
        novo_status = "Operational"
    elif opcao == "2":
        novo_status = "Under Maintenance"
    elif opcao == "3":
        novo_status = "Inactive"
    else:
        print("❌ Invalid option!")
        return lista_computadores
    
    computador["status"] = novo_status

    if novo_status == "Under Maintenance":
        computador["ultima_manutencao"] = obter_data_atual()

    salvar_computadores(lista_computadores)

    print(f"\nStatus of computer '{computador['nome']}' updated to '{novo_status}' successfully!")

    return lista_computadores
