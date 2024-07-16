from openai import OpenAI
import glob
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()
language = 'es'
transcription_text = 'reporter-combustible-p1.txt'
# transcription_text = '*.mp3'

# remember after edit the key use zsh or bash
# print(openai_api_key)

transcriptions_files = glob.glob(f'./transcriptions/{transcription_text}')
print(f"transcriptions_files: {transcriptions_files}")

for file in transcriptions_files:
    print(file)
    print(f'Creating the speech for the file: {file}')
    audio_file= open(file, "rb")
    
    # text to speech
    with open(file, 'r') as f:
        text = f.read()
        print(text)
        response = client.audio.speech.create(
            model="tts-1",
            # voice="alloy",
            voice="echo",
            # voice="shimmer",
            input=text
        )

        # Save the audio file in the 'audios' directory
        print(f"creating the audio directory")
        audio_filename = f'{os.path.basename(file).split('.')[0]}-{language}.aac' 
        # audio_filename = 'wp-themes-es.aac'
        audio_filepath = os.path.join('audios', audio_filename)

        with open(audio_filepath, 'wb') as f:
            f.write(response.content)
            # response.stream_to_file(audio_filepath)
            # response.write_to_file(f)

        print(f"Audio file saved at: {audio_filepath}")