# 📋 Organizador de Tarefas com Dashboard e Streak

## 📖 Sobre o projeto

Este projeto surgiu após uma conversa entre dois amigos sobre um problema em comum: **a falta de organização no dia a dia**.

Ambos perceberam que:

* tarefas eram esquecidas
* metas não eram cumpridas
* a produtividade era inconsistente

A partir disso, nasceu a ideia de criar uma ferramenta simples, mas eficiente, para **organizar tarefas diárias e acompanhar a consistência ao longo do tempo**.

---

## 🎯 Objetivo

O objetivo do projeto é ajudar usuários a:

* Organizar suas tarefas diárias
* Criar disciplina e consistência
* Visualizar seu progresso
* Desenvolver o hábito de concluir atividades

---

## 🚀 Funcionalidades

✔ Sistema de **login e cadastro**
✔ Tarefas individuais por usuário
✔ Checklist de tarefas concluídas
✔ Cálculo de **streak (dias consecutivos produtivos)**
✔ Barra de progresso diária (%)
✔ Dashboard com métricas
✔ Gráfico de produtividade (últimos dias)
✔ Armazenamento em banco de dados SQLite

---

## 🧠 Importância do projeto

A organização diária é um dos pilares da produtividade.

A falta dela pode gerar:

* procrastinação
* acúmulo de tarefas
* estresse
* baixa eficiência

Este projeto atua diretamente nesse problema, incentivando:

* disciplina
* constância
* clareza de objetivos

O sistema de **streak** é especialmente importante, pois cria um senso de compromisso contínuo com as tarefas.

---

## 🏗️ Estrutura do projeto

```
organizador/
│
├── main.py          # Inicialização do sistema
├── ui.py            # Interface gráfica (Tkinter)
├── auth.py          # Login e cadastro
├── tasks.py         # Gerenciamento de tarefas
├── streak.py        # Lógica de produtividade
├── charts.py        # Gráficos (matplotlib)
├── database.py      # Conexão com SQLite
└── dados.db         # Banco de dados
```

---

## ⚙️ Tecnologias utilizadas

* Python
* Tkinter (interface gráfica)
* SQLite (banco de dados)
* Matplotlib (gráficos)
* PyInstaller (geração de executável)

---

## 💻 Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

---

### 2. Instalar dependências

No Windows:

```
python -m pip install matplotlib pyinstaller
```

---

### 3. Executar o projeto

```
python main.py
```

---

## 📦 Gerar executável (.exe)

Para criar um executável para Windows:

```
pyinstaller --onefile --noconsole main.py
```

O arquivo será gerado em:

```
dist/main.exe
```

---

## 📊 Como o sistema funciona

1. O usuário cria uma conta ou faz login
2. Adiciona tarefas diárias
3. Marca tarefas como concluídas
4. O sistema calcula:

   * progresso diário (%)
   * streak de dias produtivos
5. O gráfico mostra o desempenho ao longo dos dias

---

## 🔥 Diferenciais

* Interface simples e funcional
* Organização modular (código separado por responsabilidade)
* Persistência de dados com SQLite
* Feedback visual (progresso + gráfico)
* Foco em consistência (streak)

---

## 📈 Possíveis melhorias futuras

* Criptografia de senha
* Tema moderno (UI/UX aprimorado)
* Sincronização em nuvem
* Aplicativo mobile
* Sistema de metas semanais/mensais

---

## 🤝 Conclusão

Mais do que um projeto técnico, este é um projeto com propósito:

> ajudar pessoas a se tornarem mais organizadas e consistentes.

A ideia nasceu de um problema real — e isso é o que torna esse projeto relevante.

---

## 👨‍💻 Autor

Desenvolvido por você 🚀
