from computadores import carregar_computadores, salvar_computadores, cadastrar_computador, listar_computadores, atualizar_status_computador, deletar_computador

from ordens import carregar_ordens, salvar_ordens, criar_ordem, listar_ordens_abertas, atualizar_status_ordem, verificar_sla_atraso

from historico import exibir_historico_completo, exibir_historico_por_computador, exibir_estatisticas, exibir_sla_alerta


def exibir_menu_principal():
    print("\n" + "="*50)
    print("      COMPUTER MAINTENANCE SYSTEM")
    print("="*50)
    print("[1] Manage Computers")
    print("[2] Manage Service Orders")
    print("[3] History and Statistics")
    print("[0] Exit")
    print("="*50)


def exibir_menu_computadores():
    print("\n--- MANAGE COMPUTERS ---")
    print("[1] Register computer")
    print("[2] List computers")
    print("[3] Update status")
    print("[4] Delete computer")
    print("[0] Back")


def exibir_menu_ordens():
    print("\n--- MANAGE SERVICE ORDERS ---")
    print("[1] Open new order")
    print("[2] List open orders")
    print("[3] Update order status")
    print("[4] Check SLA")
    print("[0] Back")


def exibir_menu_historico():
    print("\n--- HISTORY AND STATISTICS ---")
    print("[1] Full history")
    print("[2] History by computer")
    print("[3] General statistics")
    print("[4] SLA alerts")
    print("[0] Back")


def main():
    computadores = carregar_computadores()
    ordens = carregar_ordens()
    
    while True:
        exibir_menu_principal()
        opcao = input("Enter your option: ")
        
        if opcao == "1":
            while True:
                exibir_menu_computadores()
                sub_opcao = input("Enter your option: ")
                
                if sub_opcao == "1":
                    computadores = cadastrar_computador(computadores)
                elif sub_opcao == "2":
                    listar_computadores(computadores)
                elif sub_opcao == "3":
                    computadores = atualizar_status_computador(computadores)
                elif sub_opcao == "4":
                    computadores = deletar_computador(computadores)
                elif sub_opcao == "0":
                    break
                else:
                    print("Invalid option!")
        
        elif opcao == "2":
            while True:
                exibir_menu_ordens()
                sub_opcao = input("Enter your option: ")
                
                if sub_opcao == "1":
                    ordens = criar_ordem(ordens, computadores)
                elif sub_opcao == "2":
                    listar_ordens_abertas(ordens)
                elif sub_opcao == "3":
                    ordens = atualizar_status_ordem(ordens, computadores)
                elif sub_opcao == "4":
                    verificar_sla_atraso(ordens)
                elif sub_opcao == "0":
                    break
                else:
                    print("Invalid option!")
        
        elif opcao == "3":
            while True:
                exibir_menu_historico()
                sub_opcao = input("Enter your option: ")
                
                if sub_opcao == "1":
                    exibir_historico_completo(ordens)
                elif sub_opcao == "2":
                    exibir_historico_por_computador(ordens, computadores)
                elif sub_opcao == "3":
                    exibir_estatisticas(ordens, computadores)
                elif sub_opcao == "4":
                    exibir_sla_alerta(ordens)
                elif sub_opcao == "0":
                    break
                else:
                    print("Invalid option!")
        
        elif opcao == "0":
            print("\nSaving data and closing the system...")
            salvar_computadores(computadores)
            salvar_ordens(ordens)
            print("Goodbye!")
            break
        
        else:
            print("Invalid option!")


main()
