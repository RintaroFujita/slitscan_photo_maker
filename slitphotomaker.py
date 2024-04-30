from google.colab import drive
import os
import cv2
import numpy as np
drive.mount('/content/drive')
output_dir = '/content/drive/My Drive/slitscan_output_images/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
image = cv2.imread('/content/hackognition.png')
sample1_top, sample1_left = 100, 0
sample2_top, sample2_left = 150, 100
output_image = np.zeros_like(image)
slit_width = 10
hue_shift = 500
output_image_number = 1
for i in range(100):
    sample1_left += 20
    sample2_left += 20
    sample1 = image[sample1_top:sample1_top + 300, sample1_left:sample1_left + 300]
    sample2 = image[sample2_top:sample2_top + 500, sample2_left:sample2_left + 500]

    for sample, (top, left) in zip([sample1, sample2], [(0, 0), (50, 100)]):
        height, width, _ = sample.shape
        for y in range(height):
            for x in range(width):
                if x % slit_width == 0:
                    hue = (sample[y, x, 0] + hue_shift) % 50
                    saturation = sample[y, x, 1]
                    value = sample[y, x, 2]
                    output_image[top + y, left + x] = np.array([hue, saturation, value])
                else:
                    output_image[top + y, left + x] = sample[y, x]
    output_file_path = os.path.join(output_dir, 'output_image_{}.jpg'.format(output_image_number))
    cv2.imwrite(output_file_path, output_image)
    output_image_number += 1

