# IT Asset Maintenance Management System

---

### 📋 Project Description

Desktop system developed in pure Python for managing maintenance of information technology assets (computers). The system allows the registration of equipment, opening and tracking service orders, controlling computer status, monitoring service level agreement (SLA) deadlines, and accessing the complete maintenance history.

The project was developed as an academic assignment, aiming to apply and demonstrate fundamental Python programming concepts, modular organization, data persistence using JSON files, and the application of business rules.

---

### Relevant Variables

| Variável | Tipo | Descrição |
|---------|------|-----------|
| id | Integer | Unique identifier of the computer |
| nome | String | Equipment name |
| tipo | String | Computer type (Desktop, Notebook, or All‑in‑One) |
| modelo | String | Equipment model |
| processador | String | Installed processor |
| memoria_ram | String | Amount of RAM memory |
| armazenamento | String | Storage capacity |
| sistema_operacional | String | Installed operating system |
| localizacao | String | Physical location of the equipment |
| departamento | String | Responsible department |
| status | String | Current computer status |
| data_cadastro | String | Registration date and time |
| ultima_manutencao | String | Date of the last maintenance |

---

### Context and Problem

Companies and institutions have several computers distributed across departments and sectors, requiring preventive and corrective maintenance to ensure continuity of operations.

The lack of a centralized system makes it difficult to control the inventory of computers, track service orders, comply with service deadlines, and maintain a reliable maintenance history.

---

### 🏗️ System Architecture

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

### 🚀 Installation and Setup

#### Requirements
- Python 3.8 or higher  
- Windows, Linux, or macOS  

#### Installation
1. Clone the repository
```bash
git clone https://github.com/TAPC-hub/-Asset-maintenance
```

2. Create the folder structure
```bash
mkdir dados src
```

3. Run the system
```bash
cd src
python main.py
```

The system uses only Python standard libraries; no additional dependencies are required.

---

### 📖 How to Use

Run the system via terminal:
```bash
python main.py
```

The system displays an interactive menu with the following sections:

#### 1️⃣ Manage Computers
- Register computer
- List computers
- Update status
- Delete computer

#### 2️⃣ Manage Service Orders
- Open a new service order
- Update service order status
- Check SLA deadlines

#### 3️⃣ History and Statistics
- Complete maintenance history
- Maintenance history by computer
- General statistics
- SLA alerts

---

### 🧮 Problem Modeling

#### Formal Definition

**Computer Structure**
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

**Service Order Structure**
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

### 📈 Execution Metrics
The system automatically records:

- Total number of registered computers
- Total number of service orders
- Open and completed service orders
- Distribution by maintenance type
- Distribution by priority
- SLA alerts

---

### 🧪 Testing
Testing is performed manually through system features:

- Registrations with data validation
- Service orders opened only for existing computers
- Correct status updates
- JSON file persistence
- Automatic data loading during startup

---

### 📊 Sensitivity Analysis

- Tests with different service order priorities
- SLA impact analysis
- Complete testing of service order status flow
- Maintenance history consistency analysis

---

### 🔍 Validação e Comparação

| Feature | Manual Process | Proposed System |
|--------------|----------------|------------------|
| Equipment control | ❌ | ✅ |
| SLA control | ❌ | ✅ |
| Maintenance history | ❌ | ✅ |
| Statistics | ❌ | ✅ |

---

### 📝 Preprocessing Decisions

- Input data validation
- Text and date standardization
- Automatic identifier generation
- Data persistence separated by type
- Automatic saving after each operation

---

### 🎯  Expected Results

- Organized control of IT assets
- Reduction of failures and rework
- Compliance with maintenance deadlines
- Reliable historical data for audits
- Support for decision-making

---

### 👥 Authors

Thiago Augusto Pini Ceccoti  

Developed as an academic project – 2026
```
