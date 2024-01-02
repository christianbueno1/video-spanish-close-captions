from openai import OpenAI
import glob
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')

# client = OpenAI(api_key=openai_api_key)
mp3_files = glob.glob('./audios/*.mp3')

print(mp3_files, openai_api_key)

# audio_file= open("/path/to/file/audio.mp3", "rb")
# transcript = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )

