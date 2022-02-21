#Coded by BiMathAx
read -p "Link : " link
read -p "Start (at 00:00) : " start
read -p "End (Stop after 00:00) : " end
read -p "Name OutPut file : " name
youtube-dl --youtube-skip-dash-manifest -g "$link" > youtubedownload
declare -a link_all
while read line; do
	link_all+=("$line")
done < youtubedownload
echo ${link_all[@]}
ffmpeg -ss "$start" -i  "${link_all[0]}" -ss "$start" -i  "${link_all[1]}" -map 0:v -map 1:a -ss 30 -t "$end" -c:v libx264 -c:a aac "$name.mp4"
rm -rf youtubedownload

