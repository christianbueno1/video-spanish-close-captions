## tips
```
pip install instaloader
pip install openai

git rm -r --cached env/


pip install gradio
#deprecated
#sudo dnf install python3-distutils-extra
pip install setuptools

pip install -r requirements.txt

```
## git
```
gcmsg, git commit -m
gcam, git commit -a -m
```

## env var
```
# without quotes
export OPENAI_API_KEY=hello
#source ~/.zshrc
zsh

```
## instaloader
```
# 
https://www.instagram.com/p/C2cFEl4CxYn/
instaloader -- -C2cFEl4CxYn
#
#save in the directory lazy
instaloader --dirname-pattern=videos/lazy -- -C2cFEl4CxYn
```

## video
```
#play video with mpv
sudo apt install mpv
sudo dnf install mpv
mpv videos/lazy/2024-01-23_10-04-08_UTC.mp4
```

## audio
```
#audio, extract audio from video
ffmpeg -i videos/wordpress.mp4 audios/wordpress.mp3

#play mp3
ffplay audios/lazy.mp3
cvlc audios/lazy.mp3

```
