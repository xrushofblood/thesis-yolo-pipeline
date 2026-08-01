import os

def generate_background_labels(image_folder, labels_folder):
    # Valid image extensions recognized by YOLO
    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    # Get the list of all images present in the image folder
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
    
    created_count = 0
    
    # Create the labels folder if it doesn't exist yet
    if not os.path.exists(labels_folder):
        os.makedirs(labels_folder)
        print(f"Created destination folder: {labels_folder}")

    for img_name in images:
        # Get the file name without extension (e.g., "frame_001")
        base_name = os.path.splitext(img_name)[0]
        txt_name = f"{base_name}.txt"
        txt_path = os.path.join(labels_folder, txt_name)
        
        # If the corresponding .txt file does NOT exist, create an empty one
        if not os.path.exists(txt_path):
            with open(txt_path, 'w') as f:
                pass  # Writing nothing creates a 0-byte (empty) file
            created_count += 1
            print(f"Created empty background file for: {img_name} -> {txt_name}")
            
    print("-" * 50)
    print("Process completed!")
    print(f"• Empty .txt files created for backgrounds: {created_count}")
    print(f"• Total images analyzed in the folder: {len(images)}")

# --- EXECUTION ---
# Ensure your folder names match exactly.
# Change them below if needed:
generate_background_labels('train_val_frames', 'yolo_labels')