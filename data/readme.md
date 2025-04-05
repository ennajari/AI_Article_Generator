# 📁 data/

Ce dossier contient les données utilisées pour le système RAG.

## documents/
- Contient les documents texte utilisés comme base de connaissance pour l'agent Researcher.

## vectors/
- Contient les fichiers FAISS/Chroma générés pour la recherche sémantique.
- Ces fichiers sont créés automatiquement par `src/utils/vector_store.py`.

⚠️ Ne pas modifier les fichiers du dossier `vectors/` manuellement.
