# 🧙‍♀️ SalemBot – A Fantastic RPG Bot for Discord

**SalemBot** is a Discord bot written in Python that immerses you in a magical universe inspired by RPGs and witchcraft. It is exclusively designed for the **L'antre de Salem** server, allowing members to embody wizards in a personalized and immersive adventure.

---

## ✨ Project Goals

- Provide an **exclusive Discord bot** for the L'antre de Salem server.
- Create an interactive **magical role-playing game** in the world of witchcraft.
- Develop **custom progression**: inventory, quests, powers, magical items, familiars, etc.
- Offer a **unique narrative experience**, blending interactions, choices, and character development.

---

## 🧩 Key Features

### 🪄 Character Creation
- Start your adventure with the `/meow` command.
- Obtain a **unique magic wand** through a **quiz** inspired by the *Harry Potter* wand test.

### 💼 Wizard Profile
- Display your profile: level, XP, gold, owned items, wand, active quests...
- Character progression with **experience gain** and **leveling up**.

### 🎒 Inventory
- Manage your magical inventory: **tarot cards**, **robes**, **potions**, **relics**, etc.
- Some items unlock **new features** or quests.

### 🛒 Magic Shop
- Purchase items with your gold.
- Unlock items by reaching certain levels.
- Examples of items: **tarot cards**, **wizard robes**, **magical ingredients**.

### 🔮 Tarot Cards
- If you own tarot cards, unlock:
    - **Fortune-telling** for other players.
    - Access to **mystical quests**.

### 📜 Quests
- Activate **unique quests** based on your items and progression.
- Complete tasks to earn **XP** and **gold**.
- Active quests appear on your profile.

### 🐈 Familiars
- Obtain a **magical familiar**.
- Each familiar has its own **profile**: name, level, affinity, health.
- Send your familiar on missions to **find items**.
- You must **feed** it regularly to keep it alive.

### ⚔️ Attributes & Power
- Each player has **HP**, **magical power**, and can upgrade their wand.
- Robes and items enhance your **magical abilities**.

---

## ⚙️ Technologies Used

- **[Python](https://www.python.org/)** 3.12+
- **[discord.py](https://github.com/Rapptz/discord.py)** (with `app_commands`)
- **dotenv** for token management
- JSON files for saving profiles and data (lightweight database)

---

## 🚧 Upcoming Features

- **Magical combat** system between players
- Integration of **explorable magical locations**
- **Random events** (eclipses, portals...)
- **Interactive NPCs** with scripted dialogue
- **Wizard guilds** system

---

## 🔒 Limitations

> SalemBot is designed to be **exclusively used on the private Discord server L'antre de Salem**. It will not respond to commands on other servers.

---

## 🚀 Running the Bot Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/SalemBot.git
cd SalemBot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Discord token to a `.env` file
DISCORD_TOKEN=your_token_here

# 5. Run the bot
python src/main.py
```
