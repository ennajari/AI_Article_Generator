# 🧠 Article Generation Crew - Multi-Agent RAG System

## 🚀 Project Overview

This project demonstrates how to use **multi-agent collaboration** with [CrewAI](https://docs.crewai.com/) to generate high-quality articles using **Retrieval-Augmented Generation (RAG)** and **vector databases**.

We implement a full pipeline that includes:
- Data ingestion into a vector database
- RAG-based information retrieval
- Collaboration between multiple AI agents:
  - 🕵️ Researcher Agent
  - 📝 Outline Specialist
  - ✍️ Writer Agent
  - 🧹 Editor Agent

---

## 🧱 Project Structure
<pre>
article-generation-crew/
│
├── notebooks/                 # Dossier pour les notebooks Jupyter
│   ├── 1_setup_environment.ipynb      # Configuration de l'environnement
│   ├── 2_rag_vectordb_demo.ipynb      # Démonstration de RAG et base de données vectorielle
│   ├── 3_agent_implementation.ipynb   # Implémentation des agents
│   └── 4_full_article_generation.ipynb # Génération complète d'article
│
├── data/                      # Dossier pour stocker les données
│   ├── documents/             # Documents source pour RAG
│   └── vectors/               # Stockage pour la base de données vectorielle
│
├── src/                       # Code source réutilisable
│   ├── agents/                # Définitions des agents
│   │   ├── __init__.py
│   │   ├── researcher.py      # Agent Researcher
│   │   ├── outline_maker.py   # Agent Outline Specialist
│   │   ├── writer.py          # Agent Writer
│   │   └── editor.py          # Agent Editor
│   │
│   ├── utils/                 # Fonctions utilitaires
│   │   ├── __init__.py
│   │   ├── vector_store.py    # Gestion de la base de données vectorielle
│   │   └── rag_utils.py       # Utilitaires pour RAG
│   │
│   └── __init__.py
│
├── outputs/                   # Dossier pour les articles générés
│
├── requirements.txt           # Dépendances du projet
├── .env                       # Fichier pour les variables d'environnement (clés API)
└── README.md                  # Documentation du projet

</pre>
---

## 🛠️ Technologies & Tools

- 🔗 **CrewAI**: Agent orchestration framework
- 📚 **LangChain** / **LlamaIndex**: For document parsing and RAG
- 🔍 **FAISS** / **ChromaDB**: Vector database for semantic search
- 🤖 **OpenAI / HuggingFace LLMs**: For language generation
- 🐍 **Python 3.10+**
- 📒 **Jupyter Notebooks**

---

## 🧠 Agents Description

| Agent             | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| 🕵️ Researcher      | Retrieves relevant content using RAG from the vector DB             |
| 📝 Outline Maker   | Structures the article into a logical and informative outline       |
| ✍️ Writer          | Expands the outline into a full article with coherent flow          |
| 🧹 Editor          | Reviews grammar, flow, and overall polish to improve quality        |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/article-generation-crew.git
cd article-generation-crew
```
### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure environment variables
Create a .env file at the root with your API keys:
#### 🧪 Running the Project
##### Option 1: Using Jupyter Notebooks
Start with 1_setup_environment.ipynb and follow through to 4_full_article_generation.ipynb.

##### Option 2: Run via Python script
If main.py is implemented:
```bash
python main.py
```
##### 📂 Example Output
You can find generated articles in the outputs/ folder, structured and refined through multi-agent collaboration.

##### ✨ Future Improvements
Integrate memory and context between agents

Add GUI or web interface with Streamlit

Extend support to other LLM providers (Claude, Mistral, etc.)

Add evaluation metrics (e.g., ROUGE, BLEU)

##### 📄 License
This project is licensed under the MIT License. See the LICENSE file for more information.

##### 🙌 Acknowledgments
CrewAI

LangChain

OpenAI

##### 🤝 Contributing
Contributions, ideas, and feedback are welcome! Feel free to open an issue or PR.

---

Souhaites-tu aussi que je t’aide à créer le fichier `main.py`, `requirements.txt`, ou `config.yaml` pour accompagner ce README ?

