import cv2

class CameraHandler:
    def __init__(self, camera_index=0, width=640, height=480, quality=75):
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.quality = quality
        self.cap = None

    def start(self):
        """Միացնում է տեսախցիկը"""
        self.cap = cv2.VideoCapture(self.camera_index)
        return self.cap.isOpened()

    def get_processed_frame(self):
        """Կարդում է կադրը, փոքրացնում է և սեղմում JPEG ֆորմատով"""
        if not self.cap or not self.cap.isOpened():
            return None, None

        ret, frame = self.cap.read()
        if not ret:
            return None, None

        # Task 1.3: Frame Preprocessing (Resize & JPEG Compression)
        resized_frame = cv2.resize(frame, (self.width, self.height))
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), self.quality]
        success, encoded_image = cv2.imencode('.jpg', resized_frame, encode_param)

        if not success:
            return frame, None

        return frame, encoded_image.tobytes()

    def release(self):
        """Անջատում է տեսախցիկը"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()