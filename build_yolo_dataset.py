import os
import shutil
import yaml

def build_yolo_dataset(train_img_folder, test_img_folder, txt_folder, output_folder):
    print("Starting YOLO dataset build process...")
    
    # 1. Define and create the YOLO folder structure
    dirs = {
        'train_img': os.path.join(output_folder, 'train', 'images'),
        'train_lbl': os.path.join(output_folder, 'train', 'labels'),
        'val_img': os.path.join(output_folder, 'val', 'images'),
        'val_lbl': os.path.join(output_folder, 'val', 'labels')
    }
    
    for d in dirs.values():
        os.makedirs(d, exist_ok=True)
        
    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    train_pairs = []
    val_pairs = []
    
    # 2. Collect Training images (Takes 1, 2, 3, 4, 5)
    if os.path.exists(train_img_folder):
        # CORRECTED: os.listdir instead of os.path.listdir
        for img in os.listdir(train_img_folder):
            if img.lower().endswith(valid_extensions):
                base_name = os.path.splitext(img)[0]
                txt_name = f"{base_name}.txt"
                
                # Add only if the corresponding .txt label file exists
                if os.path.exists(os.path.join(txt_folder, txt_name)):
                    # Store the source folder to know exactly where to copy the image from
                    train_pairs.append((train_img_folder, img, txt_name))
                
    # 3. Collect Validation/Test images (Take 6)
    if os.path.exists(test_img_folder):
        # CORRECTED: os.listdir instead of os.path.listdir
        for img in os.listdir(test_img_folder):
            if img.lower().endswith(valid_extensions):
                base_name = os.path.splitext(img)[0]
                txt_name = f"{base_name}.txt"
                
                if os.path.exists(os.path.join(txt_folder, txt_name)):
                    val_pairs.append((test_img_folder, img, txt_name))
                    
    # 4. Updated helper function to copy files
    def copy_files(pairs, dest_img_dir, dest_lbl_dir):
        for source_img_dir, img, txt in pairs:
            # Copy the image from its specific original folder
            shutil.copy2(os.path.join(source_img_dir, img), os.path.join(dest_img_dir, img))
            # Copy the label from the shared txt folder
            shutil.copy2(os.path.join(txt_folder, txt), os.path.join(dest_lbl_dir, txt))

    # Execute the physical file copy
    copy_files(train_pairs, dirs['train_img'], dirs['train_lbl'])
    copy_files(val_pairs, dirs['val_img'], dirs['val_lbl'])
    
    # 5. Automatically generate the data.yaml file
    yaml_content = {
        'path': os.path.abspath(output_folder),
        'train': 'train/images',
        'val': 'val/images',
        'nc': 3, 
        'names': ['base', 'body', 'hat'] 
    }
    
    yaml_path = os.path.join(output_folder, 'data.yaml')
    with open(yaml_path, 'w') as yaml_file:
        yaml.dump(yaml_content, yaml_file, sort_keys=False)
        
    print("-" * 50)
    print("Dataset successfully created!")
    print(f"Output folder: {output_folder}")
    print(f"Total images processed: {len(train_pairs) + len(val_pairs)}")
    print(f"Training set (Takes 1-5): {len(train_pairs)} images")
    print(f"Validation set (Take 6): {len(val_pairs)} images")
    print(f"Created data.yaml at: {yaml_path}")

# --- EXECUTION ---
# Now we pass two distinct image folders: train_val_frames and test_frames
build_yolo_dataset('train_val_frames', 'test_frames', 'yolo_labels', 'yolo_dataset_v3')