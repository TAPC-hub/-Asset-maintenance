## Sistema de Gerenciamento de Manutenção de Ativos de TI

---

### 📋 Descrição do Projeto
 
Sistema desktop desenvolvido em Python puro para gerenciamento de manutenção de ativos de tecnologia da informação (computadores). O sistema permite o cadastro de equipamentos, abertura e acompanhamento de ordens de serviço, controle de status dos computadores, monitoramento de prazos de atendimento (SLA) e consulta ao histórico completo de manutenções realizadas.

O projeto foi desenvolvido como trabalho acadêmico, com o objetivo de aplicar e demonstrar conceitos fundamentais de programação em Python, organização modular, persistência de dados em arquivos JSON e aplicação de regras de negócio.

---

### Variáveis Relevantes

| Variável | Tipo | Descrição |
|---------|------|------------|
| id | Inteiro | Identificador único do computador |
| nome | String | Nome do equipamento |
| tipo | String | Tipo do computador (Desktop, Notebook ou All-in-One) |
| modelo | String | Modelo do equipamento |
| processador | String | Processador instalado |
| memoria_ram | String | Quantidade de memória RAM |
| armazenamento | String | Capacidade de armazenamento |
| sistema_operacional | String | Sistema operacional instalado |
| localizacao | String | Local físico do equipamento |
| departamento | String | Departamento responsável |
| status | String | Situação atual do computador |
| data_cadastro | String | Data e hora de cadastro |
| ultima_manutencao | String | Data da última manutenção |

---

### Contexto e Problema
 
**Contexto**: Empresas e instituições possuem diversos computadores distribuídos entre setores e departamentos, que necessitam de manutenção preventiva e corretiva para garantir a continuidade das atividades.

**Problema a Resolver**: A falta de um sistema centralizado dificulta o controle do inventário de computadores, o acompanhamento das ordens de serviço, o cumprimento dos prazos de atendimento e a manutenção de um histórico confiável de manutenções.

**Aplicação Prática**:
- Controle de inventário de ativos de TI
- Registro e acompanhamento de manutenções
- Monitoramento de prazos de atendimento (SLA)
- Histórico para análise de problemas recorrentes

---

### 🏗️ Arquitetura do Sistema

```
manutencao_ativos_ti/
│
├── dados/
│   ├── computadores.json         # Inventário de computadores
│   └── ordens_servico.json       # Ordens de serviço
│
├── src/
│   ├── __init__.py
│   ├── main.py                   # Menu principal
│   ├── computadores.py           # Gestão de computadores
│   ├── ordens.py                 # Gestão de ordens de serviço
│   ├── historico.py              # Histórico e estatísticas
│   └── utils.py                  # Funções utilitárias
│
└── README.md
```

---

### 🚀 Instalação e Configuração

#### Requisitos
- Python 3.8 ou superior
- Windows, Linux ou macOS

#### Instalação
1. Baixe ou clone o projeto  
```bash
git clone https://github.com/TAPC-hub/-Asset-maintenance
```

2. Crie a estrutura de pastas  
```bash
mkdir dados src
```

3. Execute o sistema  
```bash
cd src
python main.py
```

O sistema utiliza apenas bibliotecas padrão do Python, não sendo necessária a instalação de dependências adicionais.

---

### 📖 Como Usar

Execute o sistema via terminal:
```bash
python main.py
```

O sistema apresenta um menu interativo com as seguintes seções:

#### 1️⃣ Gerenciar Computadores
- Cadastrar computador
- Listar computadores
- Atualizar status
- Deletar computador

#### 2️⃣ Gerenciar Ordens de Serviço
- Abrir nova ordem de serviço
- Atualizar status da ordem
- Verificar prazos de SLA

#### 3️⃣ Histórico e Estatísticas
- Histórico completo de manutenções
- Histórico por computador
- Estatísticas gerais
- Alertas de SLA

---

### 🧮 Modelagem do Problema

#### Definição Formal

**Estrutura do Computador**
```python
{
  "id": int,
  "nome": str,
  "tipo": str,
  "modelo": str,
  "processador": str,
  "memoria_ram": str,
  "armazenamento": str,
  "sistema_operacional": str,
  "localizacao": str,
  "departamento": str,
  "status": str,
  "data_cadastro": str,
  "ultima_manutencao": str
}
```

**Estrutura da Ordem de Serviço**
```python
{
  "id_os": int,
  "id_computador": int,
  "nome_computador": str,
  "tipo_manutencao": str,
  "descricao": str,
  "prioridade": str,
  "tecnico_responsavel": str,
  "data_abertura": str,
  "data_conclusao": str,
  "status": str,
  "sla_previsto": str,
  "solucao_aplicada": str
}
```

---

### 📈 Métricas de Execução

O sistema registra automaticamente:
- Total de computadores cadastrados
- Total de ordens de serviço
- Ordens abertas e concluídas
- Distribuição por tipo de manutenção
- Distribuição por prioridade
- Alertas de SLA

---

### 🧪 Testes

Os testes são realizados manualmente por meio das funcionalidades do sistema:
- Cadastro com validação de dados
- Abertura de OS apenas para computadores existentes
- Atualização correta de status
- Persistência em arquivos JSON
- Carregamento automático de dados na inicialização

---

### 📊 Análise de Sensibilidade

- Testes com diferentes prioridades de ordens
- Verificação do impacto no SLA
- Testes completos do fluxo de status das ordens
- Análise de consistência do histórico

---

### 🔍 Validação e Comparação

| Funcionalidade | Processo Manual | Sistema Proposto |
|--------------|----------------|------------------|
| Controle de equipamentos | ❌ | ✅ |
| Controle de SLA | ❌ | ✅ |
| Histórico de manutenções | ❌ | ✅ |
| Estatísticas | ❌ | ✅ |

---

### 📝 Decisões de Pré-processamento

- Validação dos dados de entrada
- Padronização de textos e datas
- Geração automática de identificadores
- Persistência separada por tipo de dado
- Salvamento automático após cada operação

---

### 🎯 Resultados Esperados

- Organização e controle de ativos de TI
- Redução de falhas e retrabalho
- Cumprimento de prazos de manutenção
- Histórico confiável para auditoria
- Suporte à tomada de decisões

---

### 👥 Autores
Thiago Augusto Pini Ceccoti  

Desenvolvido como trabalho acadêmico – 2026
``
