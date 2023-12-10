# Overview:  
This project aims to develop a cutting-edge video processing bot, leveraging libraries and APIs  from Hugging Face and OpenAI. Despite the scarcity of open-source Large Language Models (LLMs) that  directly convert video to text, this bot adopts a novel approach to tackle the challenge.  
  
# Methodology:  
Videos are fundamentally a blend of images (frames) and audio. Recognizing this, the bot dissects  
the user-uploaded video into its constituent frames and audio segments. Subsequently, it applies  
image-to-text and audio-to-text conversion techniques on these extracted elements. This bifurcated  
approach enables efficient processing of video content.  

Integration with OpenAI:  
In the final step, the bot enriches its functionality by integrating user-provided prompts. It  
aggregates the extracted text from images and audio with the user's prompt into a cohesive message  
object. This object is then seamlessly relayed to OpenAI's powerful GPT-3.5 Turbo model via the  
OpenAI API. The model interprets this amalgamated data to generate a comprehensive and contextually  
relevant response.

# APIs & Models Used:  
Huggingface  
pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")  
pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")  

OpenAI  
GPT3.5 Turbo  

# Libraries Used
cv2 to clip the video  
transformers to perform the ML part  
videofileclip to extract the audip  
os & time to import files and record the time  