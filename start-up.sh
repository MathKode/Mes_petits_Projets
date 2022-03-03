sudo apt update
sudo apt upgrade -y
sudo apt install vim -y
sudo apt install figlet -y
sudo apt install lolcat -y
sudo apt install ssh -y
sudo apt install youtube-dl -y
sudo apt install ffmpeg -y
sudo apt install cowsay -y
sudo apt install nmap -y
sudo apt install python3 -y
sudo apt install python3-pip -y
pip install tk
pip install Pillow
pip install moviepy
pip install discord.py
pip install pygame
pip install argparse
pip install sockets
pip install numpy
pip install selenium
pip install requests
pip install jsonlib
pip install bs4
pip install pybase64
sudo apt install gcc -y
sudo apt install rsync -y
sudo apt install nsnake -y
sudo apt install cmatrix -y
sudo apt install git -y
sudo apt install tee -y
sudo apt install samba -y
sudo apt install apache2 -y
sudo apt install gnupg -y
#ASCIIquarium
sudo apt install libcurses-perl -y
sudo cpan Term::Animation
cd /tmp
wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
tar -zxvf asciiquarium.tar.gz
cd asciiquarium_1.1/
sudo cp asciiquarium /usr/local/bin
sudo chmod 0755 /usr/local/bin/asciiquarium
#-------------
#Fichier config
sudo echo "#code MontrAnT un message en couleur avec un police aléatoire" | sudo tee -a /etc/bash.bashrc
sudo echo 'message="RaspBerry"' | sudo tee -a /etc/bash.bashrc
sudo echo 'police=("banner" "standard" "big" "block" "bubble" "digital" "lean" "mini" "script" "shadow" "slant" "smslant" "term")' | sudo tee -a /etc/bash.bashrc
sudo echo 'police_nb=$(echo ${police[@]} | wc -w)' | sudo tee -a /etc/bash.bashrc
sudo echo 'nb=$(($RANDOM % $police_nb))' | sudo tee -a /etc/bash.bashrc
sudo echo 'figlet -f ${police[$nb]} $message | lolcat' | sudo tee -a /etc/bash.bashrc
sudo echo 'PS1="\n\033[38;5;21m--[\033[38;5;221m\u@\H\033[38;5;21m]--\n\033[38;5;21m~\033[38;5;46m\w\033[0m$ "' | sudo tee -a ~/.bashrc 
