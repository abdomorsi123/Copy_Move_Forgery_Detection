import os
import cv2
import glob

mask_dir = "data/masks"
label_dir = "data/labels"
class_id = 0


if not os.path.exists(label_dir):
    os.makedirs(label_dir)

for i, mask_file in enumerate( os.listdir(mask_dir)):
    mask_path = os.path.join(mask_dir, mask_file)
    mask_img = cv2.imread(mask_path)

    # Convert the mask image into binary format
    gray_img = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
    binary_img = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)[1]

    # Find the contours of the forged region in the binary image
    contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])

    # Calculate the normalized bounding box coordinates
    img_height, img_width, _ = mask_img.shape
    x_center = (x + w / 2) / img_width
    y_center = (y + h / 2) / img_height
    width = w / img_width
    height = h / img_height

    # Write the YOLO format label file
    label_path = os.path.join(label_dir, os.path.splitext(mask_file)[0] + ".txt")
    with open(label_path, "w") as f:
        f.write("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(class_id, x_center, y_center, width, height))

    if i % 1000 == 0 :
        print(f"{i} labels are generated")

