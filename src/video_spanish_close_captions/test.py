import os

transcription_filename_srt = os.path.basename('file').split('.')[0] + '.srt'
transcription_filepath_srt = os.path.join('transcriptions', transcription_filename_srt)

print(transcription_filename_srt)
print(transcription_filepath_srt)