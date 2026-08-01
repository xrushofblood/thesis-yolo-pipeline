from ultralytics import YOLO

def export_for_sentis():
    print("Loading the trained weights...")
    # Make sure the path points to your training weights
    model = YOLO("../runs/detect/runs/pilot_test-4/weights/best.pt") 

    print("Exporting to ONNX with unlocked confidence...")
    exported_path = model.export(
        format="onnx",
        imgsz=640,
        half=True,     
        simplify=True,   
        opset=15,        # Natively supported by Unity Sentis
        conf=0.01        # CRITICAL: Prevents ONNX from filtering out low-scoring results
    )
    
    print("-" * 50)
    print(f"ONNX model ready for Unity: {exported_path}")

if __name__ == "__main__":
    export_for_sentis()