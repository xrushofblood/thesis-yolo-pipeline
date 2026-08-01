import os
from ultralytics import YOLO

def main():
    print("Starting local YOLO26 training process...")
    
    # Initialize the cutting-edge base model (YOLO26 nano)
    model = YOLO("yolo26n.pt") 

    print("Initiating pilot training phase...")
    
    # 1. TRAINING PHASE
    model.train(
        data="yolo_dataset_v3/data.yaml",
        epochs=50,
        imgsz=640,
        device=0,
        batch=16,
        project="runs",
        name="thesis_training_v3"
    )
    
    print("\nTraining completed. Proceeding with ONNX export for Unity XR...")
    
    # 2. EXPORT PHASE
    # The 'model' object ALREADY contains the weights of 'best.pt' in memory. 
    # No need to search for the local path, we can export directly!
    exported_path = model.export(
        format="onnx",
        imgsz=640,
        half=True,       # FP16: halves the model weight (crucial for Meta Quest performance)
        simplify=True,   # Simplifies the graph structure to be fully compatible with Unity Sentis
        opset=15,         # The exact ONNX opset version natively supported by Sentis
        conf=0.01           # CRITICAL: Prevents ONNX from filtering out low-scoring results
        # NOTE: YOLO26 is natively NMS-free, so no extra NMS logic is needed in export!
    )
    
    print("Process finished successfully.")
    print(f"Your ONNX model is ready and saved at: {exported_path}")

if __name__ == "__main__":
    main()