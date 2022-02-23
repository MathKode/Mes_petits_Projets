rsync -avhPn --delete 2nd/ math@192.168.1.18:~/Document/Ecole/2nd
read -p "[Y]es/[N]o : " choix
if [ $choix = "Y" ]; then
	echo Transfert Autorisation n°2 :
	rsync -avhP --delete 2nd/ math@192.168.1.18:~/Document/Ecole/2nd
fi
