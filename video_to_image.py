# Extract frames from a video and save them as images
import cv2

# Extract frames from a video and save them as images
def extract_frames(video_path, output_folder='frames'):
    cap = cv2.VideoCapture(video_path)

    # capture the FPS rate
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame every 1 second
        if count % int(frame_rate) == 0:
            frame_name = f"{output_folder}/frame_{count}.jpg"
            cv2.imwrite(frame_name, frame)
        
        count += 1

    # Release the capture
    cap.release()
