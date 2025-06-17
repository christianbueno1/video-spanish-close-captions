from openai import OpenAI
import glob
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()
audio_names = '2025-06-10-meet-2-part-2.mp3'
# audio_names = 'listening-1.mp3'
# audio_names = '*.mp3'

mp3_files = glob.glob(f'./audios/{audio_names}')
print(f"mp3_files: {mp3_files}")

for file in mp3_files:
    print(file)
    print(f'Creating the transcription for the file: {file}')
    audio_file= open(file, "rb")
    
    # srt
    transcript_srt = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="srt"
    )
    transcription_srt = transcript_srt

    # text
    transcript_text = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    transcription_text = transcript_text
    
    # print(type(transcript) )
    # print(transcript)
    print(transcription_srt)
    print(transcription_text)

    print(f"creating the transcription file name")
    transcription_filename_srt = os.path.basename(file).split('.')[0] + '.srt'
    transcription_filename_text = os.path.basename(file).split('.')[0] + '.txt'
    # print(transcription_filename_srt)
    
    # Create the 'transcriptions' directory if it doesn't exist
    print(f" creating the directory fi it doesn't exist")
    if not os.path.exists('transcriptions'):
        os.makedirs('transcriptions')

    transcription_filepath_srt = os.path.join('transcriptions', transcription_filename_srt)
    transcription_filepath_text = os.path.join('transcriptions', transcription_filename_text)
    
    # print(transcription_filepath_srt)

    print(f"writing the transcription to the file")
    with open(transcription_filepath_srt, 'w') as f:
        f.write(transcription_srt)

    with open(transcription_filepath_text, 'w') as f:
        f.write(transcription_text)

    print(f"Transcription file saved at: {transcription_filepath_srt}")
    print(f"Transcription file saved at: {transcription_filepath_text}")