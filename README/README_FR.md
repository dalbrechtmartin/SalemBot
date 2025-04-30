# 🧙‍♀️ SalemBot – Bot RPG Fantastique pour Discord

**SalemBot** est un bot Discord écrit en Python qui vous plonge dans un univers magique, inspiré des RPG et de la sorcellerie. Il est conçu exclusivement pour le serveur **L'antre de Salem** et permet aux membres d’incarner des magiciens dans une aventure personnalisée et immersive.

---

## ✨ Objectifs du projet

- Fournir un **bot Discord exclusif** au serveur L'antre de Salem.
- Créer un **jeu de rôle magique** interactif dans l'univers de la sorcellerie.
- Développer une **progression personnalisée** : inventaire, quêtes, pouvoirs, objets magiques, familiers, etc.
- Offrir une **expérience narrative unique**, mêlant interactions, choix et développement de personnage.

---

## 🧩 Fonctionnalités principales

### 🪄 Création de personnage
- Débutez votre aventure avec la commande `/meow`.
- Obtenez une **baguette magique unique** via un **quiz** inspiré du test de baguette d’*Harry Potter*.

### 💼 Profil du magicien
- Affichez votre profil : niveau, XP, or, objets possédés, baguette, quêtes actives...
- Évolution du personnage avec **gain d’expérience** et de **niveaux**.

### 🎒 Inventaire
- Gérez votre inventaire magique : **cartes de tarot**, **tuniques**, **potions**, **reliques**, etc.
- Certains objets débloquent de **nouvelles fonctionnalités** ou quêtes.

### 🛒 Boutique magique
- Achetez des objets avec votre or.
- Débloquez des objets en atteignant certains niveaux.
- Exemples d'objets : **cartes de tarot**, **tuniques de sorcier**, **ingrédients magiques**.

### 🔮 Cartes de tarot
- Si vous possédez des cartes, débloquez :
  - La **lecture de l’avenir** pour les autres joueurs.
  - L’accès à des **quêtes mystiques**.

### 📜 Quêtes
- Activez des **quêtes uniques** selon vos objets et votre progression.
- Réalisez des tâches pour gagner de l’**XP** et de l’**or**.
- Les quêtes apparaissent sur votre profil si elles sont actives.

### 🐈 Familiers
- Obtenez un **familier magique**.
- Chaque familier a son propre **profil** : nom, niveau, affinité, santé.
- Envoyez votre familier en mission pour **chercher des objets**.
- Il faudra le **nourrir** régulièrement pour qu’il survive.

### ⚔️ Attributs & puissance
- Chaque joueur possède des **PV**, une **puissance magique**, et peut améliorer sa baguette.
- Les tuniques et objets augmentent vos **capacités magiques**.

---

## ⚙️ Technologies utilisées

- **[Python](https://www.python.org/)** 3.12+
- **[discord.py](https://github.com/Rapptz/discord.py)** (avec commandes `app_commands`)
- **dotenv** pour la gestion des tokens
- Fichiers JSON pour la sauvegarde des profils et données (base de données légère)

---

## 🚧 Fonctionnalités à venir

- Système de **combat magique** entre joueurs
- Intégration de **lieux magiques** explorables
- **Evénements aléatoires** (éclipses, portails...)
- **PNJ interactifs** et dialogue scénarisé
- Système de **guildes de sorciers**

---

## 🔒 Limitations

> SalemBot est conçu pour être **exclusivement utilisé sur le serveur Discord privé L'antre de Salem**. Il ne répondra pas aux commandes sur d’autres serveurs.

---

## 🚀 Lancer le bot localement

```bash
# 1. Cloner le repo
git clone https://github.com/ton-pseudo/SalemBot.git
cd SalemBot

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Ajouter ton token Discord dans un fichier `.env`
DISCORD_TOKEN=token_ici

# 5. Lancer le bot
python src/main.py
```

---

## 🛡️ Licence

**SalemBot** est un logiciel propriétaire.  
© 2025 dalbrechtmartin. **Tous droits réservés.**

> L'utilisation, la copie, la distribution ou la modification de ce code est strictement interdite sans autorisation explicite de l'auteure.


