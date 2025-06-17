## tips
```bash
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
```bash
gcmsg, git commit -m
gcam, git commit -a -m
```

## env var
```bash
# store here your key
# without quotes
# OPENAI API
export OPENAI_API_KEY=hello
#source ~/.zshrc
zsh

```
## instaloader yt-dlp
```bash
 
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
```bash
#play video with mpv
sudo apt install mpv
sudo dnf install mpv
mpv videos/lazy/2024-01-23_10-04-08_UTC.mp4

# run flatpak mpv
/var/lib/flatpak/exports/bin/io.mpv.Mpv audios/prueba3-1.mp3


# This is called a container remux — it's fast and lossless if your MKV already uses compatible codecs (like H.264 + AAC, which is typical for SimpleScreenRecorder).
# convert simplescreenrecorder-2025-06-16_21.08.35.mkv to mp4
ffmpeg -i simplescreenrecorder-2025-06-16_21.08.35.mkv -c copy simplescreenrecorder-2025-06-16_21.08.35.mp4
# ffmpeg -i simplescreenrecorder-2025-06-16_21.08.35.mkv -c:v copy -c:a copy output.mp4


# If the codecs aren’t compatible or you want to compress:
ffmpeg -i simplescreenrecorder-2025-06-16_21.08.35.mkv -c:v libx264 -c:a aac simplescreenrecorder-2025-06-16_21.08.35.mp4

```

## audio
```bash
#audio, extract audio from video
ffmpeg -i videos/wordpress.mp4 audios/wordpress.mp3
# extract audio from video from minute 32:44 to end
ffmpeg -i 2025-06-10-meet-2.mp4 -ss 00:32:44 -c copy 2025-06-10-meet-2-part-2.m4a

# convert aac to mp3
# f40
ffmpeg -i audios/gpu-for-video-editing-es.aac -c:v copy -c:a libmp3lame -q:a 2 gpu-for-video-editing-es.mp3
# or simple
ffmpeg -i audios/gpu-for-video-editing-es.aac audios/gpu-for-video-editing-es.mp3

#play mp3
ffplay audios/lazy.mp3
cvlc audios/lazy.mp3

# convert m4a to mp3
# ffmpeg -i audios/meet-part-1.m4a -c:a libmp3lame -q:a 2 audios/meet-part-1.mp3
ffmpeg -i 2025-06-10-meet-2-part-2.m4a -c:a libmp3lame -q:a 2 2025-06-10-meet-2-part-2.mp3

# for best quality use do not covnert before split
# split audio on equal parts of 10 minutes=600 seconds
ffmpeg -i audios/meet-part-1.m4a -f segment -segment_time 600 -c copy audios/meet-part-1-part%03d.m4a

# convert segments to mp3
for file in audios/meet-part-1-part*.m4a; do
    ffmpeg -i "$file" -c:a libmp3lame -q:a 2 "${file%.m4a}.mp3"
done

# convert one segment to mp3
ffmpeg -i audios/meet-part-1-part001.m4a -c:a libmp3lame -q:a 2 audios/meet-part-1-part001.mp3
```

## Update
```bash
# Run the following command to update all packages to their latest versions:
pip install --upgrade -r requirements.txt

# After updating, you can regenerate the requirements.txt file with the updated package versions by running:
pip freeze > requirements.txt

```

## Convert to Poetry
```bash
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
```bash
# run video-spanish-close-captions/speech-to-text.py
poetry run python video-spanish-close-captions/speech-to-text.py

```