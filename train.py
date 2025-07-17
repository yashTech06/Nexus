from ultralytics import YOLO

def train_model():
    model = YOLO('yolov8n.yaml')
    model.train(data='scripts/config.yaml', epochs=50, imgsz=640)

if __name__ == '__main__':
    train_model()
