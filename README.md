# Economist Reader — Anki

Reader d'articles avec génération de decks Anki via Claude.

## Structure

```
economist-reader/
├── app.py              # Backend Flask
├── requirements.txt
├── Procfile            # Pour Railway
└── templates/
    └── index.html      # Frontend complet
```

## Déploiement sur Railway (gratuit)

### 1. Créer un repo GitHub

```bash
git init
git add .
git commit -m "init"
gh repo create economist-reader --public --push
```

### 2. Déployer sur Railway

1. Va sur [railway.app](https://railway.app) → **New Project → Deploy from GitHub**
2. Sélectionne ton repo `economist-reader`
3. Dans **Variables**, ajoute :
   - `ANTHROPIC_API_KEY` = ta clé (depuis [console.anthropic.com](https://console.anthropic.com))
4. Railway détecte automatiquement le Procfile et déploie

Tu obtiens une URL publique du type `https://economist-reader-xxx.up.railway.app`

## Utilisation

1. Colle le texte de ton article
2. Clique sur les mots inconnus (ou sélectionne plusieurs mots pour une expression)
3. Clique **Générer le deck Anki**
4. Télécharge le `.txt`
5. Dans Anki : **Fichier → Importer**, séparateur `|`
   - Champ 1 = recto (traduction FR)
   - Champ 2 = verso (mot EN + définition + exemple)

## Format des cartes

```
traduction française|MOT — Définition en anglais. Ex: Exemple d'utilisation.
```
