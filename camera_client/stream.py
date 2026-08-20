import time
import cv2
from camera_client.camera import CameraHandler
from camera_client.sender import NetworkSender

# Կարգավորումներ
API_URL = "http://127.0.0.1:8000/vision/process-frame"
SEND_INTERVAL = 3  # Task 1.2: Rate Limiting (3 վայրկյանը 1 անգամ)

def main():
    camera = CameraHandler(camera_index=0)
    sender = NetworkSender(api_url=API_URL)

    if not camera.start():
        print("❌ Սխալ. Տեսախցիկը հասանելի չէ:")
        return

    print("🎥 Տեսախցիկը միացված է:")
    last_send_time = 0

    try:
        while True:
            raw_frame, image_bytes = camera.get_processed_frame()

            if raw_frame is None:
                time.sleep(0.5)
                continue

            current_time = time.time()

            # Task 1.2: Rate Limiting logic
            if current_time - last_send_time >= SEND_INTERVAL:
                if image_bytes:
                    success = sender.send_frame(image_bytes)
                    if success:
                        last_send_time = current_time

            # Էկրանին ցույց տալ տեսախցիկի պատուհանը
            cv2.imshow("Smart Classroom Camera", raw_frame)

            # 'q' սեղմելիս դուրս գալ
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.release()

if __name__ == "__main__":
    main()