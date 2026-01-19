import cv2

class VideoCamera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise ValueError("Unable to open camera")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def display_frame(self, frame):
        cv2.imshow('Smart Surveillance', frame)
        cv2.waitKey(1)

    def exit_requested(self):
        return cv2.waitKey(1) & 0xFF == ord('q')

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()