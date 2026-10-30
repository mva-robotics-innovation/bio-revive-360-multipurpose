from ultralytics import YOLO
model = YOLO('yolov8n.pt')
results = model(frame)
for r in results:
    for box in r.boxes:
        cls = model.names[int(box.cls)]
        if cls == 'cell phone': print("MOBILE DISTRACTION - FLASH")
        if cls == 'person' and 'hardhat' not in labels: print("HELMET MISSING")
