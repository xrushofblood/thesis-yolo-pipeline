import cv2
import os
import glob

def batch_extract(source_dir, output_dir, fps_target=1):
    print(f"\n--- In progress: {source_dir} -> {output_dir} ---")
    
    # Create output directiory if it doesn't exist 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Find all mp4 file in the specified folder 
    videos = glob.glob(os.path.join(source_dir, "*.mp4"))
    
    if not videos:
        print(f"Warning: no video found in {source_dir}")
        return

    for video_path in videos:
        video_name = os.path.basename(video_path).split('.')[0]
        vidcap = cv2.VideoCapture(video_path)
        fps_source = round(vidcap.get(cv2.CAP_PROP_FPS))
        # Calculate every how many frames to extract to get the fps_target
        interval = max(1, fps_source // fps_target)
        
        count = 0
        saved = 0
        while True:
            success, image = vidcap.read()
            if not success: break
            
            if count % interval == 0:
                # Salva il frame
                cv2.imwrite(f"{output_dir}/{video_name}_f{saved:04d}.jpg", image)
                saved += 1
            count += 1
        vidcap.release()
        print(f"Video '{video_name}': {saved} frame extracted.")

# --- EXECUTION ---
# 1. Extraction for Training & Validation
batch_extract("train_val_raw", "train_val_frames")

# 2. Extraction for Test Set
batch_extract("test_raw", "test_frames")

print("\nSuccess!")