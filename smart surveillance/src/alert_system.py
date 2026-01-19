import cv2
import datetime

def raise_alert(frame):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"alert_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Alert image saved: {filename}")