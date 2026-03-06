<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<br />
<div align="center">

  <h3 align="center">Local AI CLI Assistant</h3>

  <p align="center">
    Asistent AI local în linie de comandă construit cu LangChain și Ollama.
    <br />
    Permite interacțiune directă cu un model LLM care rulează complet local.
  </p>
</div>

---

## Table of Contents

<details>
  <summary>Deschide</summary>
  <ol>
    <li><a href="#problema-rezolvata">Problema Rezolvată</a></li>
    <li><a href="#arhitectura-sistemului">Arhitectura Sistemului</a></li>
    <li><a href="#stack-tehnologic">Stack Tehnologic</a></li>
    <li><a href="#cum-se-ruleaza-proiectul">Cum se Rulează Proiectul</a></li>
    <li><a href="#exemplu-output">Exemplu Output</a></li>
  </ol>
</details>

---

## Problema Rezolvată

Acest proiect demonstrează cum se poate construi un **asistent AI simplu care rulează local**, fără cloud și fără API key.

Problema rezolvată:

- interacțiune cu un **LLM local**
- rulare complet **offline**
- streaming al răspunsului în timp real
- integrarea unui model AI într-o aplicație **Python CLI**

Aplicația permite utilizatorului să trimită întrebări către modelul `llama3` și să primească răspunsuri direct în terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Arhitectura Sistemului

Arhitectura aplicației este simplă și orientată pe CLI.

Fluxul aplicației:

```
Utilizator (Terminal Input)
        │
        ▼
Aplicație Python CLI
(main.py)
        │
        ▼
LangChain
(ChatOllama wrapper)
        │
        ▼
Server Ollama Local
(http://localhost:11434)
        │
        ▼
Model LLM (llama3)
        │
        ▼
Răspuns Streaming
        │
        ▼
Output în Terminal
```

Componente:

- **CLI Interface** – preia inputul utilizatorului
- **LangChain** – gestionează comunicarea cu modelul
- **Ollama** – rulează modelul local
- **LLM (llama3)** – generează răspunsul

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Stack Tehnologic

Tehnologiile utilizate în proiect:

- **Python 3.11+**
- **LangChain**
- **Ollama**
- **langchain-ollama**
- **LLM model: llama3**

Caracteristici tehnice demonstrate:

- integrare LLM local
- streaming token-by-token
- aplicație CLI
- arhitectură simplă pentru proiect AI

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Cum se Rulează Proiectul

### Prerequisites

1. Instalează **Ollama**

https://ollama.com/download

2. Verifică instalarea

```bash
ollama --version
```

3. Descarcă modelul

```bash
ollama pull llama3
```

---

### Instalare

Clonează repository-ul:

```bash
git clone https://github.com/your_username/your_repo.git
cd your_repo
```

Creează mediu virtual:

```bash
python -m venv .venv
```

Activează mediul virtual (Windows):

```bash
.venv\Scripts\activate
```

Instalează dependențele:

```bash
pip install langchain langchain-ollama
```

---

## Rularea Aplicației

Rulează aplicația:

```bash
python main.py
```

Aplicația pornește un **AI assistant în terminal**.

Pentru ieșire:

```bash
quit
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Exemplu Output

Exemplu de interacțiune:

```bash
Welcome! I'm your AI assistant.

You: explain what artificial intelligence is

Assistant: Artificial intelligence is a field of computer science
that focuses on creating systems capable of performing tasks
that normally require human intelligence.
```

Răspunsurile sunt generate **în timp real (streaming)** direct în terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>