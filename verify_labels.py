import cv2
import os

# Define your classes in the exact same order as labeled in LabelMe
classes = ['base', 'body', 'hat', 'mr_potato']

# Bounding box colors (B, G, R format)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]

def draw_yolo_boxes(image_dir, label_dir, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Grab the first 10 text files for a quick visual sanity check
    txt_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')][:10]
    
    if not txt_files:
        print("Error: No .txt files found in the labels directory!")
        return

    for txt_file in txt_files:
        img_name = txt_file.replace('.txt', '.jpg')
        img_path = os.path.join(image_dir, img_name)
        
        if not os.path.exists(img_path):
            continue
            
        img = cv2.imread(img_path)
        h, w, _ = img.shape
        
        with open(os.path.join(label_dir, txt_file), 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])
            
            # Convert normalized coordinates back to absolute pixel coordinates
            x1 = int((x_center - width / 2) * w)
            y1 = int((y_center - height / 2) * h)
            x2 = int((x_center + width / 2) * w)
            y2 = int((y_center + height / 2) * h)
            
            # Draw the bounding box and class label on the image
            color = colors[class_id % len(colors)]
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, classes[class_id], (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            
        # Save the annotated image to the verification directory
        cv2.imwrite(os.path.join(output_dir, img_name), img)
    
    print(f"Verification complete! Check the output images in: '{output_dir}'")

# Run the verification process
draw_yolo_boxes("train_val_frames", "yolo_labels", "visualized_checks")