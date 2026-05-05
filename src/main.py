# main.py
# Sistema de Manutenção de Computadores - Menu Principal

from computadores import carregar_computadores, salvar_computadores, cadastrar_computador, listar_computadores, atualizar_status_computador, deletar_computador

from ordens import carregar_ordens, salvar_ordens, criar_ordem, listar_ordens_abertas, atualizar_status_ordem, verificar_sla_atraso

from historico import exibir_historico_completo, exibir_historico_por_computador, exibir_estatisticas, exibir_sla_alerta


def exibir_menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n" + "="*50)
    print("      SISTEMA DE MANUTENÇÃO DE COMPUTADORES")
    print("="*50)
    print("[1] Gerenciar Computadores")
    print("[2] Gerenciar Ordens de Serviço")
    print("[3] Histórico e Estatísticas")
    print("[0] Sair")
    print("="*50)


def exibir_menu_computadores():
    """Exibe o submenu de computadores."""
    print("\n--- GERENCIAR COMPUTADORES ---")
    print("[1] Cadastrar computador")
    print("[2] Listar computadores")
    print("[3] Atualizar status")
    print("[4] Deletar computador")
    print("[0] Voltar")


def exibir_menu_ordens():
    """Exibe o submenu de ordens de serviço."""
    print("\n--- GERENCIAR ORDENS DE SERVIÇO ---")
    print("[1] Abrir nova ordem")
    print("[2] Listar ordens abertas")
    print("[3] Atualizar status da ordem")
    print("[4] Verificar SLA")
    print("[0] Voltar")


def exibir_menu_historico():
    """Exibe o submenu de histórico."""
    print("\n--- HISTÓRICO E ESTATÍSTICAS ---")
    print("[1] Histórico completo")
    print("[2] Histórico por computador")
    print("[3] Estatísticas gerais")
    print("[4] Alertas de SLA")
    print("[0] Voltar")


def main():
    """Função principal do sistema."""
    # Carrega os dados
    computadores = carregar_computadores()
    ordens = carregar_ordens()
    
    while True:
        exibir_menu_principal()
        opcao = input("Digite sua opção: ")
        
        # Opção 1: Gerenciar Computadores
        if opcao == "1":
            while True:
                exibir_menu_computadores()
                sub_opcao = input("Digite sua opção: ")
                
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
                    print("Opção inválida!")
        
        # Opção 2: Gerenciar Ordens
        elif opcao == "2":
            while True:
                exibir_menu_ordens()
                sub_opcao = input("Digite sua opção: ")
                
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
                    print("Opção inválida!")
        
        # Opção 3: Histórico
        elif opcao == "3":
            while True:
                exibir_menu_historico()
                sub_opcao = input("Digite sua opção: ")
                
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
                    print("Opção inválida!")
        
        # Opção 0: Sair
        elif opcao == "0":
            print("\nSalvando dados e encerrando o sistema...")
            salvar_computadores(computadores)
            salvar_ordens(ordens)
            print("Até mais!")
            break
        
        else:
            print("Opção inválida!")

main()
