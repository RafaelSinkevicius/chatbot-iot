# Chatbot para Indústria de Reciclagem

Este projeto implementa um **chatbot inteligente** voltado para a **indústria de reciclagem**, com foco na **consulta de dados operacionais e indicadores de eficiência** da linha de separação de materiais (plásticos e metais). Ele simula uma solução tecnológica para **aumentar a automação** e **melhorar o monitoramento do processo produtivo**.

---

## 🚀 Funcionalidades

- ✅ Consulta ao volume de materiais recicláveis processados.
- ✅ Exibição do tempo de operação da linha.
- ✅ Cálculo e retorno de indicadores-chave de eficiência (produtividade, taxa de erro, etc).
- ✅ Interface interativa via terminal (CLI) e Web (Flask).
- ✅ Dados simulados para testes e validação do chatbot.

---

## 🧱 Estrutura do Projeto
```
recycling_chatbot/
│
├── app/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── processor.py
│   └── utils.py
│
├── data/
│   └── operations.json
│
├── interface/
│   ├── terminal_ui.py
│   └── web_ui/
│       ├── templates/
│       │   └── index.html
│       ├── static/
│       │   └── script.js
│       └── server.py
│
├── tests/
│   ├── test_chatbot.py
│   └── test_processor.py
│
├── requirements.txt
├── run_terminal.py
├── run_web.py
└── README.md
```

---

## 🛠️ Como Executar

### ✅ 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/recycling_chatbot.git
cd recycling_chatbot
```

---

### ✅ 2. Instale as dependências

```bash
pip install -r requirements.txt
```
⚠️ Recomendado usar um ambiente virtual (venv) para evitar conflitos.

---

### 💻 Modo Terminal (CLI)

```bash
python run_terminal.py
```

---

### 🌐 Modo Web (via navegador)

```bash
python run_web.py
```

Acesse no navegador: http://localhost:5000

---

### 🧪 Rodar Testes

```bash
pytest tests/
```

---

### 📁 Exemplo de Dados (operations.json)

```bash
[
  {
    "data": "2025-04-10",
    "volume_processado_kg": 1250,
    "tempo_operacao_horas": 6,
    "eficiencia_percentual": 89.5
  }
]
```

---

### 🧠 Tecnologias Utilizadas
- Python 3.12+

- Flask

- HTML + JS (para interface web)

- JSON (para simulação de dados)

- Pytest (para testes)