# main.py
# Entry point for Smart Surveillance System

from video_capture import VideoCamera
from motion_detection import detect_motion
from human_detection import detect_human
from alert_system import raise_alert
from logger import log_event

def main():
    print("Starting Smart Surveillance System...")

    camera = VideoCamera()

    while True:
        frame = camera.get_frame()

        if frame is None:
            print("No frame received. Exiting...")
            break

        motion_detected = detect_motion(frame)

        if motion_detected:
            human_detected = detect_human(frame)

            if human_detected:
                print("Suspicious activity detected!")
                raise_alert(frame)
                log_event("Human detected with motion")

        camera.display_frame(frame)

        if camera.exit_requested():
            print("Stopping Surveillance System...")
            break

    camera.release()

if __name__ == "__main__":
    main()
