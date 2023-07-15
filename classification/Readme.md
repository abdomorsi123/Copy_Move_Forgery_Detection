# Classification

This folder contains the scripts, datasets, and trained models related to the classification method for copy move forgery detection.

## Dataset

The classification method utilizes two datasets:

1. **DEFACTO Copy-Move Dataset**: This dataset is a large-scale collection of images that have been tampered with using the copy-move forgery technique. It consists of over 19,000 images specifically created for copy move forgery detection tasks.

2. **Flickr Image Dataset**: This dataset comprises over 28,000 diverse images, along with their corresponding image tags and metadata. It can be used for various computer vision tasks and provides the original images for the copy move forgery detection system.

## Version 1 Classification Steps

In version 1 of the classification process, the following steps were taken:

1. **Import Libraries**: The necessary libraries were imported to facilitate the implementation of the classification process.

2. **Exploratory Data Analysis**: An exploratory data analysis was conducted on both fake and original images to gain insight into the dataset's characteristics.

3. **Data Preparation**: The train, validation, and test datasets were prepared for training by resizing the images to 128x128x3.

4. **Model Training**: The data was trained using three different models - a custom model, VGG16, and ResNet50 - to identify the most appropriate model for the classification task.

## Version 2 Classification Steps

In version 2 of the classification process, the same steps were followed as in version 1 with one difference:

1. **Custom Model Architecture**: Instead of using the same custom model architecture as in version 1, a different architecture was employed to improve the classification performance. The remaining steps were the same as in version 1.

## Version 3 Classification Steps

In version 3 of the classification process, the same steps were followed as in version 2 with one additional step:

1. **Model Training**: An extra model, MobileNetV2, was included in the training process along with the updated custom model architecture, VGG16, and ResNet50.

2. **Fine Tuning**: The models were fine-tuned by training some final layers from the main architecture, not just the top layers. The remaining steps were the same as in version 2.
