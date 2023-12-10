from moviepy.editor import VideoFileClip
from transformers import pipeline

# audio pipeline
audio_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")

# Extract audio from video
def extract_audio_from_video(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

# Audio pipeline
def process_video_audio(audio_path):
    # initialize the results dictionary
    results = {}

    # get the text from the audio
    results['audio_text'] = audio_pipe(audio_path)

    # add the result to the dictionary
    return results
