import os
import glob
import shutil

min_width_height = 0.0099
label_dir = "data/labels"
image_dir = "data/images"
counter1 = 0 
counter2 = 0

for file_path in  glob.glob(os.path.join(label_dir, '*.txt')):
    with open(file_path, 'r') as f:
        content = f.read()
        class_id, x_center, y_center, width, height = map(float, content.split())

    if width < min_width_height and height < min_width_height:
        try:
            os.remove(file_path)
            counter1 +=1 
        except PermissionError:
            print(f'Could not remove file: {file_path}. File is currently in use.')
            continue
print(f'\n\n{counter1} labels deleted!')



# Get a list of all image files in the image directory
image_files = [os.path.splitext(file_name)[0] for file_name in os.listdir(image_dir)]

# Get a list of all label files in the label directory
label_files = [os.path.splitext(file_name)[0] for file_name in os.listdir(label_dir)]


# Loop over all image files and delete those whose names don't exist in the label directory
for image_file in image_files:
    if image_file not in label_files:
        image_path = os.path.join(image_dir, image_file + ".jpg")
        try:
            os.remove(image_path)
            counter2 +=1 
        except PermissionError:
            print(f'Could not remove file: {file_path}. File is currently in use.')
            continue

print(f'\n\n{counter2} images deleted!')