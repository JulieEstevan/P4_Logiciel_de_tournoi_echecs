# Gestion de tournois d'échecs

Ce projet est une application console en Python permettant de gérer des tournois d'échecs selon le système suisse. Elle offre les fonctionnalités suivantes :
- **Gestion des joueurs** : Ajouter et lister les joueurs avec leurs informations.
- **Gestion des tournois** : Créer et gérer des tournois à plusieurs rondes.
- **Génération d'appariements** : Associer les joueurs selon les règles du système suisse.
- **Enregistrement des résultats** : Saisir les résultats des matchs et mettre à jour les points.
- **Rapports** : Générer des rapports sur les joueurs et les tournois.

## Prérequis
- **Python 3.13**, ou supérieur, installé sur votre ordinateur.
- Les dépendances Python répertoriées dans `requirements.txt`.

## Installation

1. **Clone le repository du projet:**

```bash
git clone <REPOSITORY_URL>
```

2. **Navigue dans le dossier du projet:**

```bash
cd nom_du_projet
```

3. **Créer un environnement virtuel:**

```bash
python -m venv env
```

**Sur Windows:**
```bash
env\Scripts\activate
```

**Sur macOS/Linux:**
```bash
source env/bin/activate
```

4. **Installe les dépendances:**
```bash
pip install -r requirements.txt
```
**Usage**
```bash
main.py
```
Le programme affiche un menu principal vous permettant d'effectuer les actions suivantes :

1. **Ajouter un joueur** : Saisir les informations d'un nouveau joueur.
2. **Liste des joueurs** : Afficher la liste des joueurs inscrits.
3. **Créer un tournoi** : Initialiser un nouveau tournoi.
4. **Démarrer un tournoi** : Démarrer le tournoi sélectionné.
5. **Liste des tournois** : Afficher la liste des tournois existants.
6. **Rapports** : Afficher différents types de rapports.
7. **Quitter** : Fermer le programme.

### Instructions générales

- **Navigation dans le menu** : Saisissez le numéro correspondant à l’action que vous souhaitez effectuer.
- **Saisie des informations** : Suivez les instructions à l’écran pour saisir les données requises.
- **Format de date** : Les dates doivent être au format `jj/mm/aaaa`.
- **Numéro d’identification national** : Doit être composé de deux lettres majuscules suivies de cinq chiffres (exemple : `AB12345`).

## Structure du projet :
```
P4_Logiciel_de_tournoi_echecs/

├── controllers/
│   ├── match_controller.py
│   ├── player_controller.py
│   ├── report_controller.py
│   ├── round_controller.py
│   └── tournament_controller.py
├── data/
│    ├── players.json
│    └── tournaments.json
├── flake-report/
│   ├── back.svg
│   ├── file.svg
│   ├── index.html
│   └── style.css
├── models/
│   ├── match_model.py
│   ├── player_model.py
│   ├── round_model.py
│   └── tournament_model.py
├── utils/
│    └── clear.py
├── views/
│   ├── menu_view.py
│   ├── match_view.py
│   ├── player_view.py
│   └── tournament_view.py
├── .flake8
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

# Chess Tournament Management

This project is a console application in Python for managing chess tournaments using the Swiss system. It offers the following features:
- **Player Management** : Add and list players with their information.
- **Tournament Management** : Create and manage tournaments with multiple rounds.
- **Pairing Generation** : Pair players according to the Swiss system rules.
- **Result Recording** : Enter match results and update points.
- **Reports** : Generate reports on players and tournaments.

## Prerequisites
- **Python 3.7** or higher installed on your machine.
- Python dependencies listed in `requirements.txt`.

## Installation

1. **Clone the project repository:**

```bash
git clone <REPOSITORY_URL>
```

2. **Navigate to the project directory:**

```bash
cd nom_du_projet
```

3. **Create a virtual environment:**

```bash
python -m venv env
```

**On Windows:**
```bash
env\Scripts\activate
```

**On macOS/Linux:**
```bash
source env/bin/activate
```

4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

**Usage**
```bash
main.py
```
The program displays a main menu allowing you to perform the following actions :

1. **Add a player**: Enter the information of a new player.
2. **List players**: Display the list of registered players.
3. **Create a tournament**: Initialize a new tournament.
4. **Start a tournament**: Start the selected tournament.
5. **List tournaments**: Display the list of existing tournaments.
6. **Reports**: Display different type of report.
7. **Quit**: Close the program.

### General Instructions

- **Menu navigation**: Enter the number corresponding to the action you want to perform.
- **Entering information**: Follow the on-screen instructions to enter the required data.
- **Date format**: Dates must be in the format `dd/mm/yyyy`.
- **National ID**: Must consist of two uppercase letters followed by five digits (example: `AB12345`).


## Project Structure:
```
P4/

├── controllers/
│   ├── match_controller.py
│   ├── player_controller.py
│   ├── report_controller.py
│   ├── round_controller.py
│   └── tournament_controller.py
├── data/
│    ├── players.json
│    └── tournaments.json
├── flake-report/
│   ├── back.svg
│   ├── file.svg
│   ├── index.html
│   └── style.css
├── models/
│   ├── match_model.py
│   ├── player_model.py
│   ├── round_model.py
│   └── tournament_model.py
├── utils/
│    └── clear.py
├── views/
│   ├── menu_view.py
│   ├── match_view.py
│   ├── player_view.py
│   └── tournament_view.py
├── .flake8
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```