import cv2
import os
from google.colab import drive
drive.mount('/content/drive')
input_dir = '/content/drive/My Drive/slitscan_output_images/'
output_dir = '/content/drive/My Drive/slitscan_output_images/output_video/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_video_name = 'output_video.mp4'
image_files = sorted(file for file in os.listdir(input_dir) if file.endswith('.jpg'))
frame_width = 1920
frame_height = 1080
fps = 30
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(os.path.join(output_dir, output_video_name), fourcc, fps, (frame_width, frame_height))
for image_file in image_files:
    img_path = os.path.join(input_dir, image_file)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (frame_width, frame_height))
    out.write(img)
out.release()
