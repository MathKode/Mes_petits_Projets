init () {
	ansi="\033[38;5;"
	ansib="\033[48;5;"
	debut="\033["
	sep=";"
	m="m"
	fin="f"
	height=$(tput lines)
	width=$(tput cols)
	height=$(($height / 2))
	#declare -A lettre_dico=([1]="A" [2]="Z" [3]="E" [4]="R" [5]="T" [6]="Y" [7]="U" [8]="I" [9]="O" [10]="P" [11]="Q" [12]="S" [13]="D" [14]="F" [15]="G" [17]="H" [18]="J" [19]="K" [20]="L" [21]="M" [22]="W" [23]="X" [24]="C" [25]="V" [26]="B" [27]="N") 
	lettre_dico=("A" "Z" "E" "R" "T" "Y" "U" "I" "O" "P" "Q" "S" "D" "F" "G" "H" "J" "K" "L" "M" "W" "X" "C" "V" "B" "N")
	#Enlève les commandes tapper (stty echo)
	stty -echo
	#Enlève le curseur (tput cnorm)
	tput civis
}
touche () {
	# touche height width x y lettre color
	color=$6

	#h = Hauteur ; w = Largeur
	h=$1
	w=$2
	
	#x = Colonne ; y = Lines
	x=$3
	y=$4
	
	#top = _*w
	top=""
	t=0
	while [ $t -lt $w ]; do
		top=$(echo $top\_)
		t=$(($t+1))
	done
	echo -ne "$ansi$color$m$debut$y$sep$x$fin$top"
	
	#bottom = ‾*w
	bottom=""
	t=0
	while [ $t -lt $w ];do
		bottom=$(echo $bottom\‾)
		t=$(($t+1))
	done
	yd=$(($y - 1 + $h))
	echo -ne "$ansi$color$m$debut$yd$sep$x$fin$bottom"
	
	#cote |      |
	t=0
	end=$(($h-2))
	xd=$(($x + w - 0))
	yt=$y
	while [ $t -lt $end ]; do
		yt=$(($yt + 1))
		echo -ne "$ansi$color$m$debut$yt$sep$x$fin|$debut$yt$sep$xd$fin|"
		t=$(($t + 1))
	done

	#Lettre
	#cx = centre x ; cy = centre y
	cx=$(($w / 2))
	cx=$(($cx + $x))
	cy=$(($h / 2))
	cy=$(($cy + $y))
	echo -ne "$ansi$color$m$debut$cy$sep$cx$fin$5"	

}

keyboard () {
	#place all the keys
	#First line
	tour=0
	move_y=$height
	echo Width touche space : $width_touche_space
	while [ $tour -lt 26 ]; do
		move_x=0
		if [ $tour = 0 ]; then
			tf=10
		elif [ $tour = 10 ]; then
			tf=20
		else
			tf=26
		fi
		while [ $tour -lt $tf ]; do
			touche $height_touche $width_touche_space $move_x $move_y ${lettre_dico[$tour]} 15
			move_x=$(($move_x + $width_touche))
			tour=$(($tour + 1))
		done
		move_y=$(($move_y + $height_touche))
	done
}

main () {
	init
	echo $height $width
	if [ $width -lt 33 ]; then
		echo Width is smaller than 33 COLUMNS
		exit
	elif [ $height -lt 9 ]; then
		echo Height is smaller than 9 LINES
		exit
	else
		height_touche=$(($height / 3))
		width_touche=$(($width / 10))
		width_touche_space=$(($width_touche - 2))
		echo Hauteur key : $height_touche
		echo Longueur key : $width_touche
		echo ${lettre_dico[3]}
		echo "$ansi$color$m"
		keyboard
		
		#Boucle key
		while [ true ]; do
			#touche $height_touche $width_touche 0 $height A 10	
			
			read -n 1 -s c
			tt=0
			p=0
			for i in ${lettre_dico[@]};do
				tt=$(($tt + 1))
				if [ $i = ${c^^} ]; then
					p=$tt
					xx=$(($tt % 10 - 1))
					if [ $xx = $((1 - 2)) ];then
						xx=9
					fi
					xx=$(($xx * $width_touche))
					yy=$(($tt / 11))
					if [ $p = 21 ]; then
						yy=2
					fi
					yy=$(($yy * $height_touche))
					yy=$(($yy + $height))
				fi	
			done
			if [ $p != 0 ]; then
				touche $height_touche $width_touche_space $xx $yy ${lettre_dico[$(($p - 1))]} 10 
				touche $height_touche $width_touche_space $xx $yy ${lettre_dico[$(($p - 1))]} 15 

			fi
		done
		
	fi
	
	



} 
main
