# src/video_spanish_close_captions/__init__.py
"""Video Spanish Close Captions package."""

from .speech_to_text import (
    get_openai_client,
    transcribe_audio,
    process_audio_file,
    main
)

__all__ = [
    'get_openai_client',
    'transcribe_audio', 
    'process_audio_file',
    'main'
]