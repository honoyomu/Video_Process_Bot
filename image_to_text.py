# import pipeline to use the image-to-text model
from transformers import pipeline

# import os to get the path to the images
import os

# import OrderedDict to sort the results
from collections import OrderedDict

# define the pipeline
pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Define a custom sorting key function
def sort_key(filename):
    # Extract the frame number from the filename
    frame_number = int(filename.split('_')[1].split('.')[0])
    return frame_number

def process_video_frames(folder_path):
    results = OrderedDict()  # Use OrderedDict to maintain order
    # Use the custom sort_key function for sorting
    for filename in sorted(os.listdir(folder_path), key=sort_key):
        if filename.startswith("frame_") and filename.endswith(".jpg"):
            frame_number = int(filename.split('_')[1].split('.')[0])
            res = pipe(os.path.join(folder_path, filename))
            results[frame_number] = res
    return results