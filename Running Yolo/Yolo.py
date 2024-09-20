import cv2
from ultralytics import YOLO

model = YOLO('../yolo-weights/yolov8l.pt')
results = model("images/1.jpg", show=True)
cv2.waitKey(0)
