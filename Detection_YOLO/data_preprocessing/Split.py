import os
import shutil
import random

train_path1 = 'data/train/images'
train_path2 = 'data/train/labels'

val_path1 = 'data/val/images'
val_path2 = 'data/val/labels'

test_path1 = 'data/test/images'
test_path2 = 'data/test/labels'

if not os.path.exists(val_path1):
    os.makedirs(val_path1)

if not os.path.exists(val_path2):
    os.makedirs(val_path2)

if not os.path.exists(test_path1):
    os.makedirs(test_path1)

if not os.path.exists(test_path2):
    os.makedirs(test_path2)

train_files = os.listdir(train_path1)
val_files = random.sample(train_files, 1500)


remaining_train_files = [elem for elem in train_files if elem not in val_files]
test_files = random.sample(remaining_train_files, 1500)


# move val images and labels to val dir

for file in val_files:
    source_path1 = os.path.join(train_path1, file)
    destination_path1 = os.path.join(val_path1, file)
    shutil.move(source_path1, destination_path1)


for file in val_files:
    source_path2 = os.path.join(train_path2, os.path.splitext(file)[0]) + ".txt"
    destination_path2 = os.path.join(val_path2, os.path.splitext(file)[0]) + ".txt"
    shutil.move(source_path2, destination_path2)

# move test images and labels to test dir

for file in test_files:
    source_path3 = os.path.join(train_path1, file)
    destination_path3 = os.path.join(test_path1, file)
    shutil.move(source_path3, destination_path3)


for file in test_files:
    source_path4 = os.path.join(train_path2, os.path.splitext(file)[0]) + ".txt"
    destination_path4 = os.path.join(test_path2, os.path.splitext(file)[0]) + ".txt"
    shutil.move(source_path4, destination_path4)
    