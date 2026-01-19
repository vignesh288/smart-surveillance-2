import cv2

bg_subtractor = cv2.createBackgroundSubtractorMOG2()

def detect_motion(frame):
    fg_mask = bg_subtractor.apply(frame)
    motion_pixels = cv2.countNonZero(fg_mask)
    threshold = 5000  # Adjust based on needs
    return motion_pixels > threshold