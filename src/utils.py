import json
import os
from datetime import datetime


def criar_pasta_dados():
    if not os.path.exists("dados"):
        os.makedirs("dados")
        print("📁 'data' folder created successfully!")


def carregar_dados(nome_arquivo):
    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"
    
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print(f"Data loaded from {nome_arquivo}")
            return dados
    except FileNotFoundError:
        print(f"File {nome_arquivo} not found. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print(f"File {nome_arquivo} is empty or corrupted. Returning empty list.")
        return []


def salvar_dados(dados, nome_arquivo):
    criar_pasta_dados()
    caminho_arquivo = f"dados/{nome_arquivo}"
    
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f"✅ Data saved to {nome_arquivo}")
            return True
    except Exception as e:
        print(f"❌ Error saving {nome_arquivo}: {e}")
        return False


def obter_data_atual():
    agora = datetime.now()
    return agora.strftime("%Y-%m-%d %H:%M:%S")
