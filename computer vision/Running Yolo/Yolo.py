from ultralytics import YOLO
import cv2

model = YOLO('../yolo-weigth/yolov8l.pt')
results = model("images/1.jpg", show=True)
cv2.waitKey(0)
