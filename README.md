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
# OPENAI API
export OPENAI_API_KEY=hello
#source ~/.zshrc
zsh

```
## instaloader yt-dlp
```
 
https://www.instagram.com/p/C2cFEl4CxYn/
instaloader -- -C2cFEl4CxYn
#
#save in the directory lazy
instaloader --dirname-pattern=videos/lazy -- -C2cFEl4CxYn

# f40 v2024.07.09-1
sudo dnf install yt-dlp

#
# https://x.com/elonmusk/status/1748094375869993228
# m3u8
# -o "%(title)s.%(ext)s"
# --cookies
# --cookies-from-browser firefox::none
# title
yt-dlp -o "~/Downloads/%(id)s.%(ext)s" "URL" --cookies-from-browser firefox::none
#
yt-dlp -o "~/Downloads/%(id)s.%(ext)s" "https://x.com/onlypanasec/status/1813232133655159278"


```

## video
```
#play video with mpv
sudo apt install mpv
sudo dnf install mpv
mpv videos/lazy/2024-01-23_10-04-08_UTC.mp4

# run flatpak mpv
/var/lib/flatpak/exports/bin/io.mpv.Mpv audios/prueba3-1.mp3
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

## Update
```
# Run the following command to update all packages to their latest versions:
pip install --upgrade -r requirements.txt

# After updating, you can regenerate the requirements.txt file with the updated package versions by running:
pip freeze > requirements.txt

```

## Convert to Poetry
```
# Initialize in your current directory/project
poetry init
# Add dependencies from requirements.txt
poetry add $(cat requirements.txt | grep -v '^\-e' | cut -d = -f 1 | xargs)
# or
poetry add $(cat requirements.txt | awk -F '==' '{print $1}')
#
# Update pyproject.toml with specific versions
# Install dependencies
poetry install

# dependencies problems
Because no versions of pydantic match >2.10.6,<2.11.0a1 || >2.11.0a1,<2.11.0a2 || >2.11.0a2,<3.0.0
 and pydantic (2.11.0a1) depends on pydantic-core (2.28.0), pydantic (>2.10.6,<2.11.0a2 || >2.11.0a2,<3.0.0) requires pydantic-core (2.28.0).
And because pydantic (2.11.0a2) depends on pydantic-core (2.29.0)
 and pydantic (2.10.6) depends on pydantic-core (2.27.2), pydantic (>=2.10.6,<3.0.0) requires pydantic-core (2.27.2 || 2.28.0 || 2.29.0).
So, because video-spanish-close-captions depends on both pydantic (^2.10.6) and pydantic-core (^2.30.0), version solving failed.

```

## Poetry commands
```
# run video-spanish-close-captions/speech-to-text.py
poetry run python video-spanish-close-captions/speech-to-text.py

```