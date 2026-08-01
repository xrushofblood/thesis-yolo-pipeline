import os

# 1. WRITE THE EXACT NAMES OF YOUR 7 BACKGROUND FRAMES HERE (without .jpg extension)
background_frames = [
    "Take_3_1_Base_f0000",  # Replace with the actual name of the 1st frame of Take 3
    "Take_3_1_Base_f0001",  # 2nd frame
    "Take_3_1_Base_f0002",  # 3rd frame
    "Take_3_1_Base_f0003",  # 4th frame
    "Take_3_1_Base_f0004",  # 5th frame
    "Take_3_1_Base_f0005",  # 6th frame
    "Take_3_1_Base_f0006",  # 7th frame (
    "Take_3_1_Base_f0007",  # 8th frame 
]

labels_folder = 'yolo_labels'

# Create the destination directory if it doesn't exist yet
if not os.path.exists(labels_folder):
    os.makedirs(labels_folder)

# Create only the 7 targeted empty files
created_count = 0
for frame in background_frames:
    txt_name = f"{frame}.txt"
    txt_path = os.path.join(labels_folder, txt_name)
    
    with open(txt_path, 'w') as f:
        pass  # Writing nothing creates a 0-byte (empty) file
    created_count += 1
    print(f"Created empty background file: {txt_name}")

print("-" * 40)
print(f"Done! Created {created_count} background files successfully.")