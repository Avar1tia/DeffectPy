import cv2

# Установка размеров захвата
width, height = 640, 480

video_path = "deff1.mp4"

video_capture = cv2.VideoCapture(video_path)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    ret, frame = video_capture.read()
    frame = cv2.resize(frame, (width, height))
    cv2.imshow('video', frame)
    k = cv2.waitKey(10)
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("Edge Detected Image", edges)
    if k == 27:
        break

video_capture.release()
cv2.destroyAllWindows()