from ultralytics import YOLO

def run_inference():
    model = YOLO('models/best.pt')
    results = model.predict(source='data/test', save=True, conf=0.25)
    for r in results:
        print(r.boxes)

if __name__ == '__main__':
    run_inference()
