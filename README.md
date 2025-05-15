# Wator World Simulation

Wa-Tor est une simulation de dynamique de population inventée par A. K. Dewdney. Cette simulation se déroule sur une planète appelée Wa-Tor, qui est entièrement couverte d'eau et a la forme d'un torus (un anneau). Deux types d'entités peuplent cette planète : les requins et les poissons. Ces créatures interagissent selon des règles simples, générant des comportements complexes. 

La simulation affichera une représentation visuelle de l'état du monde, où :
- `~` représente l'eau.
- `🐠` représente un poisson.
- `🦈` représente un requin.

## Fonctionnalités

- Simulation d'un écosystème marin avec des poissons et des requins.
- Comportements de reproduction et de prédation.
- Mouvement aléatoire des créatures.
- Affichage visuel de l'état du monde.
- Statistiques en temps réel sur les populations de poissons et de requins.
- Contrôles pour démarrer, arrêter et réinitialiser la simulation.
- Affichage des paramètres de la simulation.

## Déroulement du projet
Le projet a été mené à bien par Olivier Legendre, Augustin Dendeviel et Stéphane Muller.
- Phase 1 : 2 jours de réflexion sur l'architecture du code
- Phase 2 : Répartition des méthodes à faire par chacun  
    - Stéphane : gestion de l'initialisation, des poissons et affichage console  
    - Augustin : gestion des requins et poissons
    - Olivier  : gestion de l'affichage pygame, historisation
- Phase 3 : Elaboration du code en vérification sur GitHub

## Prérequis

- Python 3.12.3
- Bibliothèque termcolor pandas seaborn pygame matplolib sqlite3

## Installation

1. Clonez le dépôt ou téléchargez le code source.
2. Assurez-vous d'avoir Python installé sur votre machine.
3. Installez les bibliothèques en exécutant la commande suivante :

```bash
pip install termcolor pandas seaborn pygame matplolib sqlite3  
```

## Guide d'utilisation :

Affichage Mode console:  
- fichier : wator_world.py  
    - exécuter le programme avec ce fichier. 

Affichage Mode graphique:
- fichier : app.py  
    - exécuter le programme avec ce fichier.  
    - vous pouvez creer une simulation avec create_and_run_simulation ou lancer le programme avec run_app

# Wator_world.py
## Description des classes
### <ins>WatorWorld

Classe principale qui gère la simulation. Elle initialise le monde, ajoute des poissons et des requins, et gère leurs mouvements et interactions.  

#### Attributs  

- world_map : Une liste 2D représentant la carte du monde.
- school_of_fish : Une liste de tous les poissons dans le monde.
- school_of_shark : Une liste de tous les requins dans le monde.
- nb_fish : Le nombre de poissons.
- nb_shark : Le nombre de requins.
- birth_fish : Le nombre de naissances de poissons.
- birth_shark : Le nombre de naissances de requins.
- dead_fish : Le nombre de poissons morts.
- dead_shark : Le nombre de requins morts.

#### Méthodes

- __init__(self, dim_map_x, dim_map_y, number_of_fish, number_of_shark,CONST_FISH_MATURITY=3, CONST_SHARK_MATURITY=10, CONST_SHARK_INITIAL_ENERGY=5) :  
    - Initialise le monde avec les dimensions, le nombre de poissons et de requins spécifiés.
- initialize_world_map(self) : Initialise la carte du monde avec de l'eau.
- add_creatures_to_world_map(self, number_of_fish, number_of_shark) : 
    - Ajoute des poissons et des requins à la carte du monde.
- move_sharks(self) : Déplace tous les requins.
- move_fishes(self) : Déplace tous les poissons.
- iterate(self) : Exécute un cycle de la simulation.
- display_affichage(self) : Affiche l'état actuel du monde.

# creatures.py
## Description des classes
### <ins>Creature
- La classe de base pour toutes les créatures. Elle contient les attributs communs à toutes les créatures.

#### Attributs

- coordinate : Un tuple représentant les coordonnées (x, y) de la créature.
- age : L'âge de la créature, initialisé à 0.

#### Méthodes

- __init__(self, coordinate: tuple[int]) : Initialise une nouvelle créature avec les coordonnées spécifiées.
------------------------------------------------------------------------------------------------

### <ins>Fish
- Une sous-classe de Creature représentant un poisson.

#### Méthodes

- __init__(self, coordinate: tuple[int]) : 
Initialise un nouveau poisson avec les coordonnées spécifiées.  
- __repr__(self) -> str : Retourne une représentation textuelle de l'objet Fish.

------------------------------------------------------------------------------------------------

### <ins>Shark
- Une sous-classe de Creature représentant un requin.  

#### Attributs
- energy : L'énergie initiale du requin.

#### Méthodes

- __init__(self, coordinate: tuple[int], initial_energy) : 
Initialise un nouveau requin avec les coordonnées et l'énergie initiale spécifiées.  
- __repr__(self) -> str : Retourne une représentation textuelle de l'objet Shark.


# app.py
- import pygame_view as pyv
- import wator_world as ww
- import history
- import history_entity as he

# history.py
- Gestion de l'historique des simulations.
- Sauvegarde et récupération des cartes et des statistiques de l'écosystème.
- Visualisation des statistiques avec des graphiques.
- Utilisation de Pandas et Seaborn pour l'analyse et la visualisation des données.

# history_entity.py
- Création et gestion de tables pour stocker les données de simulation.
- Insertion et récupération de données sur les populations de poissons et de requins.
- Gestion des cartes de l'écosystème pour chaque génération.
- Statistiques sur les naissances et les décès de poissons et de requins.

# pygame_view.py
- Visualisation d'un écosystème marin avec des poissons (en vert) et des requins (en rouge).
- Statistiques en temps réel sur les populations de poissons et de requins.
- Contrôles pour démarrer, arrêter et réinitialiser la simulation.
- Affichage des paramètres de la simulation.





