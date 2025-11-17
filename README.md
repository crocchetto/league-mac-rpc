
# A Better League of Legends Rich Presence For Discord on Mac!

  

**Enhance your Discord experience while playing League of Legends on Mac!**

This is a port of [league-rpc by Its-Haze](https://github.com/Its-Haze/league-rpc) for MacOS users!

Got questions already? Don't hesitate to join the [Community Server of Its-Haze](https://discord.haze.sh) or contact me **@crocchetto** on Discord about the mac port!

  

## Table of Contents

- [Installation](#installation)

- [Showcase](#showcase)

- [Command Line Arguments](#command-line-arguments)

- [FAQ](#faq)

- [Uninstall](#%EF%B8%8F-uninstall)

- [Build from source](#️-build-from-source)

- [Contact and Support](#-contact-and-support)

  

---

  

## Installation

>  [!IMPORTANT]
> This port is going to install **Homebrew**, the correct **Python version (3.11)** to run this program, create a **virtual environment** and install **all the dependencies** on your Mac. If you want to uninstall everything check the [uninstall](#%EF%B8%8F-uninstall) topic.

  

### 📥 Getting Started

1. Head over to the [Releases Page](https://github.com/crocchetto/league-mac-rpc/releases)

2. Download **`Source code (zip)`** from the latest release (it's under Assets)

3. Unzip the folder and place it somewhere safe (e.g. to your Desktop) and **remember that you won't be moving that or you'll have to do the installation process again**.

4. Open your **Terminal** (`⌘cmd+space` and type `Terminal` or you can find it in Finder `Applications > Utilities`) and type:

```bash

cd path/to/your/folder/

```

(to determine the path you can simply **drag the folder and drop it in the Terminal** after writing `cd ` and **press enter**)

  

5. Then type this command to make the installer executable:

```bash

chmod +x install.sh

```

(again you can also drag and drop the file into the Terminal after writing `chmod +x ` and press enter)

  

6. Finally, run the installer by typing:

```bash

./install.sh

```

(You know the deal, just drag and drop the file into the Terminal and press enter)

  

7. The script will guide you through the installation.

* If you don't have *Homebrew* and/or *Python* installed it will probably **ask your Mac's password** (this is for installing Homebrew/Python, **it's safe**, if you don't trust me install [Homebrew from their website](https://brew.sh/))

8. Once finished, the script will create a `StartLoL_RPC.command` file inside the project folder. You can Place this anywhere and it will still work.

9. That's it! Just double click on it and you'll be good to go. ✨

  

### 🔄 Updating

Right now I have no idea on how to update it yet since this is my first little project. I guess I will provide more info in the future.

  

---

  

## Showcase

  

### Summoner Icons

  

Who let the Kitten and the Penguin out? I did 😎. Now you too, can show off your favorite summoner icon, right there on Discord!

  

![summoner-icon-1](images/in_client_icon_1.png)  ![summoner-icon-2](images/in_client_icon_2.png)

  

### Ranked Games

  

You can show off your rank emblem right in your Discord Presence.

- SoloQ/Flex: Shows off your Rank emblem + LP

- TFT: Shows off your TFT rank emblem + LP

- Arena: Shows off your Arena medallion + Your rating

  

If you want to hide your rank, then add the ``--no-rank`` argument, to **disable** this feature. As it's enabled by default.

  

![lobby-ranked](images/in_soloq_show_ranked_1.png)  ![lobby-ranked-2](images/in_soloq_show_ranked_2.png)

  

### In Game

- Show your selected skin.

- **Animated skins**: Ultimate skins will be animated on Discord.

- **Skin Names**: The name of the skin will be shown when hovering the skin on Discord. This includes **Chromas** as well.

- **KDA**: Display your Kills, Deaths, Assists and Creep Score (cs)

- Can be disabled with `--no-stats`

- **Rank**: Show what rank you have depending on the gamemode you play in (SoloQ, Flex, TFT, Arena, etc.)

- Can be disabled with `--no-rank`

- **Game timer**: The ingame timer is accurately represented on Discord. Which is something even League's own Rich Presence don't do.

  
  

#### Skins

![Aphelios-skin](images/in_game_aphelios_skin_kda.png)

  
  

Example on Discord:

  

![Ezreal-Animated](images/animated_ezreal_showcase.gif)  ![Lux-Animated](images/animated_lux_showcase.gif)

  

##### All Animated Skins

  

<div  align="left">

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Ahri_86.gif"  width="150"  alt="Ahri"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Ezreal_5.gif"  width="150"  alt="Ezreal"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Jinx_60.gif"  width="150"  alt="Jinx"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Kaisa_71.gif"  width="150"  alt="Kaisa"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Lux_7.gif"  width="150"  alt="Lux"/>

</div>

  

<div  align="left">

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/MissFortune_16.gif"  width="150"  alt="Miss Fortune"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Mordekaiser_54.gif"  width="150"  alt="Mordekaiser"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Morgana_80.gif"  width="150"  alt="Morgana"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Samira_30.gif"  width="150"  alt="Samira"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Seraphine_1.gif"  width="150"  alt="Seraphine"/>

</div>

  

<div  align="left">

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Seraphine_2.gif"  width="150"  alt="Seraphine"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Seraphine_3.gif"  width="150"  alt="Seraphine"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Sett_66.gif"  width="150"  alt="Sett"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Sona_6.gif"  width="150"  alt="Sona"/>

<img  src="https://raw.githubusercontent.com/Its-Haze/league-assets/master/animated_skins/Udyr_3.gif"  width="150"  alt="Udyr"/>

</div>

  

### TFT (Teamfight tactics)

Showcase your favorite TFT Companion!

  

![tft-companion-1](images/tft_companion_showcase_1.png)  ![tft-companion-2](images/tft_companion_showcase_2.png)

  

---

  

## Command Line Arguments

  

All arguments are optional - LeagueRPC works perfectly fine without any of them. Use these if you want to customize behavior.

  

To use these on the macOS version you will have to open `StartLoL_RPC.command` with TextEdit (or any other text editor you prefer) and add right after `./venv/bin/python3 -m league_rpc` (e.g. `./venv/bin/python3 -m league_rpc --client-id 1230607224296968303`)

  

**✨ = Enabled by default**

  

### `--launch-league <location>` ✨

LeagueRPC automatically finds and launches League for you. This is important because it takes priority over League's native Discord presence during startup.

  

Only specify a path if League is installed somewhere unusual:

```sh

./venv/bin/python3 -m league_rpc --launch-league  "G:\Riot Games\Riot Client\RiotClientServices.exe"

```

  

### `--client-id <discord-app-id>` ✨

Want to show a different game name on Discord? Create an app at the [Discord Developer Portal](https://discord.com/developers/applications) and use its Application ID.

  

```sh

./venv/bin/python3 -m league_rpc --client-id  1230607224296968303

```

Fun options:

- **League of Kittens**: `1230607224296968303`

- **League of Linux**: `1185274747836174377`

  

### `--no-stats`

Hides your KDA and CS from Discord.

```sh

./venv/bin/python3 -m league_rpc --no-stats

```

  

### `--no-rank`

Hides your rank, LP, and emblem from Discord.

```sh

./venv/bin/python3 -m league_rpc --no-rank

```

  

### `--hide-emojis`

Removes the 🟢/🔴 emojis next to your Online/Away status.

```sh

./venv/bin/python3 -m league_rpc --hide-emojis

```

  

![Online](images/in_client_online_status.png)  ![Away](images/in_client_away_status.png)

  

### `--hide-in-client`

Hides your Rich Presence when you're just sitting in the client. It'll show up again when you queue, enter champ select, or start a game.

```sh

./venv/bin/python3 -m league_rpc --hide-in-client

```

  

### `--add-process <process-name>`

Using a Discord alternative or modified client? Add its process name here. Find it in Task Manager.

```sh

./venv/bin/python3 -m league_rpc --add-process CustomDiscord AnotherProcess

```

  

### `--wait-for-league <seconds>` ✨

How long to wait for League to start before giving up. Default is `-1` (waits forever).

```sh

./venv/bin/python3 -m league_rpc --wait-for-league  30

```

*Mostly useful for legacy Linux setups with Lutris*

  

### `--wait-for-discord <seconds>` ✨

How long to wait for Discord to start. Default is `-1` (waits forever).

```sh

./venv/bin/python3 -m league_rpc --wait-for-discord  30

```

  

### Combining Arguments

Mix and match whatever you need:

```sh

./venv/bin/python3 -m league_rpc --client-id  1230607224296968303  --no-stats  --hide-emojis

```

  

---

  

## 💡 Tips

  

I don't have many tips for now.

  

Remember to stay hydrated! 🥤

  

---

  

## ❓FAQ

  

### 🚫 Will this get my account banned?

Nope! It only uses Riot's local API (`127.0.0.1:2999`), which is completely safe. Vanguard won't care about it either since it doesn't modify any game files nor gives you an advantage in game.

  

### 🛡️ Is this a virus?

No. Some antivirus software might flag it because it's not code-signed (costs $100/year, not worth it for a free project). The entire source code is public on GitHub - feel free to review it or build it yourself.

  

### 🛠️ League's native RPC is still showing instead of LeagueRPC

Make sure StartLoL_RPC.command launches League for you. There's a tiny window during client startup where the native Discord presence can be disabled, and LeagueRPC needs to catch it.

  

If it's still not working:

1. Log out of League

2. Close League completely

3. Start LeagueRPC and let it launch League for you

4. Log back in

  

Still broken? Ask me on Discord (@crocchetto), or on the league-rpc by Its-Haze [Discord Server](https://discord.haze.sh) or open a [GitHub issue](https://github.com/crocchetto/league-mac-rpc/issues).

  

### ✔️ Does Riot approve this?

This is an independent open-source project, not affiliated with Riot Games.

  

### 🎮 Does it support TFT, Arena, ARAM, etc?

Yep! Works with all game modes including TFT, Arena, ARAM, Swarms, and whatever new modes Riot releases.

  

### 📉 Why doesn't my CS update live?

Blame Riot's API - it only updates every 10 minions killed instead of every single one. Nothing I can do about that unfortunately.

  

---

## 🗑️ Uninstall

If you want to completely remove the project and all its dependencies from your Mac, follow these steps in order.

  

### 1. Delete the Project Folder

  

This will remove the script and the launcher.

  

1. Drag the main project folder (the one containing this `README`) to the Bin (Trash).

2. Don't forget to drag the `StartLoL_RPC.command` file if you moved it elsewhere.

3. Empty the trashcan

  

### 2. Uninstall Python 3.11

  

This removes the specific version of Python we installed with Homebrew.

  

1. Open your **Terminal** app.

2. Run the following command:

```bash

brew uninstall python@3.11

```

  

### 3. Uninstall Homebrew

  

**⚠️ Warning:** This is a major step. Homebrew is used by many other applications. Only do this if you are **absolutely sure** you don't need Homebrew for anything else. Uninstalling it will remove all other packages you may have installed with it.

  

1. Open your **Terminal** app.

2. Run the official uninstall script by copy-pasting this command:

```bash

/bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh))"

```

3. The script will ask for your Mac's password and guide you through the rest of the removal process.

  

---

  

## 🏗️ Build from Source

For the cool kids who want to build it themselves:

  

- For **Windows**:

  

```powershell
# Clone and navigate
git clone https://github.com/Its-Haze/league-rpc.git
cd league-rpc

# Set up virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# Build
pyinstaller --onefile --name leagueRPC.exe league_rpc/__main__.py --clean --distpath .

# Run
.\leagueRPC.exe
```

  

- For **Mac**:

  

Would you look at that, It's all in the [Installation](#installation) up there.... Maybe we are the cool kids! 😎

  

---

  

## 📞 Contact and Support

Got questions about the main project? Join the [Discord Server of Its-Haze](https://discord.haze.sh)

Feel free to contact me directly on Discord (@crocchetto) or on Telegram (@AmAWolf).

  

For issues related to the code, or project as a whole, please open an [issue on my GitHub](https://github.com/crocchetto/league-mac-rpc/issues) or on [Its-Haze's GitHub](https://github.com/Its-Haze/league-rpc/issues).
