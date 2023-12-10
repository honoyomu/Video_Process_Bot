# Import the necessary libraries
import os
from image_to_text import process_video_frames
from video_to_audio_to_text import extract_audio_from_video, process_video_audio
from video_to_image import extract_frames
import time
import key

# import OpenAI API
import openai
from openai import OpenAI
client = OpenAI()

# import streamlit
import streamlit as st

# Initialize OpenAI API
os.environ["OPENAI_API_KEY"]=key.OPENAI_API_KEY
openai.api_key = key.OPENAI_API_KEY

# Streamlit app
st.title('Video Processing Chatbot')

# Text input for the user's prompt
user_prompt = st.text_input("Enter your prompt")

# File uploader
uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if st.button('Process Request'):
    if uploaded_file is not None:
        # Save the uploaded video to a temporary file
        video_path = "example_video.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the video
        extract_frames(video_path, output_folder='images')

        # Process frames for image-to-text
        image_text_results = process_video_frames('images')

        # Process video for audio-to-text
        audio_path = "audio_output.mp3"
        extract_audio_from_video(video_path, audio_path)
        audio_text_results = process_video_audio(audio_path)

        # Convert the results into OpenAI chatbot format
        image_text_content = "Image-to-Text Results:\n"
        for frame, texts in image_text_results.items():
            image_text_content += f"Frame {frame}: {texts[0]['generated_text']}\n"
        audio_text_content = f"Audio-to-Text Results:\n{audio_text_results['audio_text']['text']}"

        # Create the messages for the chatbot
        messages = [
            {"role": "system", "content": "You are a knowledgeable assistant analyzing video content. Provide detailed and confident insights based on the image and audio information extracted from the video."},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": "Image-to-Text Analysis:"},
            {"role": "assistant", "content": image_text_content},
            {"role": "assistant", "content": "Audio-to-Text Analysis:"},
            {"role": "assistant", "content": audio_text_content}
        ]

        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Clean up temporary files
        time.sleep(2)
        os.remove(video_path)
        time.sleep(2)
        os.remove(audio_path)
        time.sleep(2)

        # Display the GPT response
        st.subheader("Response:")
        st.write(response.choices[0].message.content)