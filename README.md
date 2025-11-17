# A Better League of Legends Rich Presence For Discord on Mac!

**Enhance your Discord experience while playing League of Legends on Mac!**

This is an unofficial port of [league-rpc by Its-Haze](https://github.com/Its-Haze/league-rpc) designed natively for **macOS** users!

Got questions? Don't hesitate to join the [Community Server of Its-Haze](https://discord.haze.sh) or contact me **@crocchetto** on Discord about this mac port!

## Table of Contents

- [Installation](#installation)

- [Configuration](#configuration)

- [Showcase](#showcase)

- [Tips](#-tips)

- [FAQ](#faq)

- [Uninstall](#%EF%B8%8F-uninstall)

- [Build from source](#%EF%B8%8F-build-from-source)

- [Contact and Support](#-contact-and-support)

---

## Installation

You have **two ways** to use LeagueRPC. Choose the one that fits you best!

### 1. LeagueRPC App (Recommended)

The easiest method. Works like a normal Mac app. No manual installation of Python or Homebrew required.

1.  Head over to the [Releases Page](https://github.com/crocchetto/league-mac-rpc/releases).

2.  Download the **`LeagueRPC_vx.x_App.zip`** file.

3.  Unzip it and drag **`LeagueRPC.app`** to your **Applications** folder (optional, you can keep it wherever you like).

4.  **Double-click** to run. A terminal window will open automatically to show you the status.
> [!IMPORTANT]
> **"App is damaged" Error?**
> 
> Since this app is open-source and not signed by Apple (which costs about $99/year), macOS might show a warning saying *"LeagueRPC is damaged and can't be opened"*. **This is a false positive.**
>
> **To fix it:**
> 1. Open the **Terminal** app.
> 2. Type `xattr -cr ` (make sure there is a space at the end).
> 3. **Drag and drop** the `LeagueRPC.app` into the terminal window.
> 4. Press **Enter**.
> 5. Open the App again.

---

### 2. Installer Script (Advanced)

Use this if you prefer running from source, want to see the code, or if the App doesn't work for you. 

>  [!WARNING]
> This is going to install **Homebrew**, the correct **Python version (3.11)** to run this program, create a **virtual environment** and install **all the dependencies** on your Mac. If you want to uninstall everything check the [uninstall](#%EF%B8%8F-uninstall) topic.

1.  Download the **`LeagueRPC_vx.x_Installer.zip`** file from Releases.

2.  Unzip the folder and place it somewhere safe you want.

3.  Open your **Terminal** and navigate to the folder:
    ```bash
    cd path/to/your/folder/
    ```
    *(Tip: type `cd ` and drag the folder into the terminal)*

4.  Make the installer executable:
    ```bash
    chmod +x install.sh
    ```
    *(Again: type `chmod +x ` and drag the file into the terminal)*

5.  Run the installer:
    ```bash
    ./install.sh
    ```
    *(You know the deal: just drag the file into the Terminal and press enter)*

6.  Follow the instructions
* If you don't have *Homebrew* and/or *Python* installed it will probably **ask your Mac's password** (this is for installing Homebrew/Python, **it's safe**, if you don't trust me install [Homebrew](https://brew.sh/) from their website)

8.  Once finished, the script will create a `StartLoL_RPC.command` file inside the project folder. You can Place this anywhere and it will still work.

9.  That's it! Just double click on it and you'll be good to go. ✨

---

## Configuration

You can customize the Rich Presence just by editing the **`config.json`** file.

You can find it:

* **For App Users:**
    1.  Right-click `LeagueRPC.app`.
    2.  Choose **Show Package Contents**.
    3.  Go to `Contents` > `Resources`.
    4.  Open `config.json` with TextEdit (or any other text editor you prefer), change values (e.g. `"no_stats": true`), save, and restart the App.

* **For Installer Users:**
    1.  Simply edit the `config.json` file located in the main folder.

**✨ = Enabled by default**

### `"launch_league": "default"` ✨
LeagueRPC automatically finds and launches League for you (`/Applications/League of Legends.app`).
If your game is installed elsewhere, replace `"default` with the path to your game.

### `"client_id": "default"` ✨
Want to show a different game name on Discord? Create an app at the [Discord Developer Portal](https://discord.com/developers/applications) and use its Application ID replacing the `"default"` with Another Application ID.

Fun options:
- **League of Kittens**: `1230607224296968303`
- **League of Linux**: `1185274747836174377`

### `"no_stats": false`
Replace `false` with `true` to hide your KDA and CS from Discord.

### `"no_rank": false`
Replace `false` with `true` to hide your rank, LP, and emblem from Discord.

### `"hide_emojis": false`
Replace `false` with `true` to remove the 🟢/🔴 emojis next to your Online/Away status.

![Online](images/in_client_online_status.png) ![Away](images/in_client_away_status.png)

### `"hide_in_client": false`
Replace `false` with `true` to hide your Rich Presence when you're just sitting in the client. It'll show up again when you queue, enter champ select, or start a game.

### `"add_process": []`
Using a Discord alternative or modified client? Add its process name between the brachets (e.g. `"add_process": ["Discord2"]`).

### `"wait_for_league": -1`
How long to wait for League to start before giving up

### `"wait_for_discord": -1`
How long to wait for Discord to start

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

## 💡 Tips

I don't have many tips for now.

Remember to stay hydrated! 🥤

---

## ❓FAQ

### 🚫 Will this get my account banned?
Nope! It only uses Riot's local API (127.0.0.1:2999), which is completely safe. Vanguard won't care about it either since it doesn't modify any game files nor gives you an advantage in game.

### 🛡️ Is this a virus?
No. Some antivirus software might flag it because it's not code-signed (which costs $100/year, not worth it for a free project). The entire source code is public on GitHub - feel free to review it or build it yourself.

### 🛠️ League's native RPC is still showing instead of LeagueRPC
Make sure StartLoL_RPC launches League for you. There's a tiny window during client startup where the native Discord presence can be disabled, and LeagueRPC needs to catch it.

If it's still not working:

1. Log out of League

2. Close League completely

3. Start LeagueRPC (App or Script) and let it launch League for you

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

If you want to completely remove the project from your Mac.

### If you used the App:
1. Just drag `LeagueRPC.app` to the Trash. That's it.

### If you used the Installer Script:

1. **Delete the Project Folder:** Drag the folder containing this README to the Trash.

2. **Uninstall Python 3.11 (Optional):**
   ```bash
   brew uninstall python@3.11
   ```
3. Uninstall Homebrew

Homebrew is used by many other applications. Only do this if you are **absolutely sure** you don't need Homebrew for anything else. Uninstalling it will remove all other packages you may have installed with it.

* Open your **Terminal** app.

* Run the official uninstall script by copy-pasting this command:

```bash
/bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh))"
```

* The script will ask for your Mac's password and guide you through the rest of the removal process.

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

Clone the repository:
```bash
git clone https://github.com/crocchetto/league-mac-rpc.git
cd league-mac-rpc
```

Setup Python Environment:
```bash
brew install python@3.11
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv venv
source venv/bin/activate
```

Install Dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
```

Build the App:
```bash
pyinstaller --noconfirm --onedir --windowed --clean \
 --name "LeagueRPC" \
 --add-data "league_rpc:league_rpc" \
 --add-data "config.json:." \
 --hidden-import "pypresence" \
 --hidden-import "lcu_driver" \
 --icon="icon.icns" \
 league_rpc/__main__.py
```

---

## 📞 Contact and Support

Got questions about the main project? Join the [Discord Server of Its-Haze](https://discord.haze.sh)

Feel free to contact me directly on Discord (@crocchetto) or on Telegram (@AmAWolf) about the mac port!.

For issues related to the code, or project as a whole, please open an [issue on my GitHub](https://github.com/crocchetto/league-mac-rpc/issues) or on [Its-Haze's GitHub](https://github.com/Its-Haze/league-rpc/issues).
