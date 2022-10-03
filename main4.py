import os.path

from feat import Detector
from PIL import Image
import matplotlib.pyplot as plt

face_model = "retinaface"
landmark_model = "mobilenet"
au_model = "rf"
emotion_model = "resmasknet"
detector = Detector(face_model = face_model, landmark_model = landmark_model, au_model = au_model, emotion_model = emotion_model)

test_image = os.path.join("frame0.jpg")

f, ax = plt.subplots()
im = Image.open(test_image)
ax.imshow(im)

image_prediction = detector.detect_image(test_image)

image_prediction

image_prediction.plot_detections()

