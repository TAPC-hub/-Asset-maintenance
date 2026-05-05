import json
import os
from datetime import datetime


def criar_pasta_dados():
    if not os.path.exists("dados"):
        os.makedirs("dados")
        print("📁 Pasta 'dados' criada com sucesso!")


def carregar_dados(nome_arquivo):

    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print(f"Dados carregados de {nome_arquivo}")
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Retornando lista vazia.")
        return []
    except json.JSONDecodeError:
        print(f"Arquivo {nome_arquivo} está vazio ou corrompido. Retornando lista vazia.")
        return []


def salvar_dados(dados, nome_arquivo):

    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"
    
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f"✅ Dados salvos em {nome_arquivo}")
            return True
    except Exception as e:
        print(f"❌ Erro ao salvar {nome_arquivo}: {e}")
        return False


def obter_data_atual():
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")
