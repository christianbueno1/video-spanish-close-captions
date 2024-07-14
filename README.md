## tips
```
# linux virtual environment
python -m venv env
source ./env/bin/activate

pip install instaloader
pip install openai

git rm -r --cached env/


pip install gradio
#deprecated
#sudo dnf install python3-distutils-extra
pip install setuptools

pip install -r requirements.txt



# limit 4096 characters

```
## git
```
gcmsg, git commit -m
gcam, git commit -a -m
```

## env var
```
# store here your key
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

# convert aac to mp3
# f40
ffmpeg -i audios/gpu-for-video-editing-es.aac -c:v copy -c:a libmp3lame -q:a 2 gpu-for-video-editing-es.mp3
# or simple
ffmpeg -i audios/gpu-for-video-editing-es.aac audios/gpu-for-video-editing-es.mp3

#play mp3
ffplay audios/lazy.mp3
cvlc audios/lazy.mp3

```
