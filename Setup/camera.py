import cv2
from picamera2 import Picamera2
import time

def test_rpi_camera():
    # Initialize the PiCamera2 object
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (640, 480)})
    picam2.configure(config)
    picam2.start()
    time.sleep(2)

    frame = picam2.capture_array()
    cv2.imshow("RPi Camera Test", frame)
    print("Press any key to exit the test")
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    picam2.stop()

if __name__ == "__main__":
    test_rpi_camera()
