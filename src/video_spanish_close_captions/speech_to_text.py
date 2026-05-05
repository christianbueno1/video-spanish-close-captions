# src/video_spanish_close_captions/speech_to_text.py (renombrado sin guiones)
from openai import OpenAI
from openai.types.audio import Transcription
from typing import Literal, TypedDict
# from typing import BinaryIO, Literal
import glob
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_openai_client():
    """Initialize and return OpenAI client."""
    return OpenAI()

def find_audio_files(pattern: str='*.mp3', audio_dir: str='./audios'):
    """Find audio files matching the pattern."""
    mp3_files = glob.glob(f'{audio_dir}/{pattern}')
    print(f"Found {len(mp3_files)} audio files")
    return mp3_files

def transcribe_audio(client: OpenAI, file_path: str, response_format: Literal['json', 'srt', 'text'] ='json') -> Transcription | str:
    """Transcribe a single audio file."""
    with open(file_path, "rb") as audio_file:
        transcript: Transcription | str = client.audio.transcriptions.create(
            model="whisper-1",
            # model="gpt-4o-transcribe",
            file=audio_file,
            response_format=response_format
        )
    return transcript

def save_transcription(transcription: Transcription | str, output_path: str | Path):
    """Save transcription to file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        if isinstance(transcription, str):
            f.write(transcription)
        else:
            f.write(transcription.text)
    
    print(f"Transcription saved: {output_path}")

def process_audio_file(client: OpenAI, file_path: str, output_dir: str='transcriptions'):
    """Process a single audio file and save transcriptions."""
    print(f'Processing: {file_path}')
    
    base_name = Path(file_path).stem
    
    # Transcribe to SRT
    transcript_srt = transcribe_audio(client, file_path, 'srt')
    srt_path = Path(output_dir) / f'{base_name}.srt'
    save_transcription(transcript_srt, srt_path)
    
    # Transcribe to text
    transcript_text = transcribe_audio(client, file_path, 'text')
    txt_path = Path(output_dir) / f'{base_name}.txt'
    save_transcription(transcript_text, txt_path)

    # Transcribe to JSON
    transcript_json = transcribe_audio(client, file_path, 'json')
    json_path = Path(output_dir) / f'{base_name}.json'
    save_transcription(transcript_json, json_path)
    
    return srt_path, txt_path, json_path

class ProcessingResult(TypedDict):
    audio: str
    srt: Path
    txt: Path
    json: Path
    status: str

class ErrorResult(TypedDict):
    audio: str
    status: str
    error: str

def main(audio_pattern: str='audio.mp3', audio_dir: str='./audios', output_dir: str='transcriptions') -> list[ProcessingResult | ErrorResult]:
    """Main function to process all matching audio files."""
    client = get_openai_client()
    audio_files = find_audio_files(audio_pattern, audio_dir)
    
    results: list[ProcessingResult | ErrorResult] = []
    for file_path in audio_files:
        try:
            srt_path, txt_path, json_path = process_audio_file(client, file_path, output_dir)
            results.append({
                'audio': file_path,
                'srt': srt_path,
                'txt': txt_path,
                'json': json_path,
                'status': 'success'
            })
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            results.append({
                'audio': file_path,
                'status': 'error',
                'error': str(e)
            })
    
    return results

if __name__ == "__main__":
    # main()
    main(audio_pattern='dios-esta-de-moda.mp3', audio_dir='./audios', output_dir='transcriptions')