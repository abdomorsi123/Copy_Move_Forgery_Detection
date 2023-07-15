# Sampling

This folder contains the scripts, datasets, and trained models related to the sampling method for copy move forgery detection.

## Dataset

The sampling method utilizes a dataset consisting of the following:

1. **DEFACTO Copy-Move Dataset**: This dataset includes 3,200 images and their corresponding masks. The images have been tampered with using the copy-move forgery technique, specifically created for copy move forgery detection tasks.

2. **Flickr Image Dataset**: This dataset comprises 3,200 original images randomly selected from the Flickr Image Dataset. These images serve as the source of original samples for the copy move forgery detection system.

## Sampling Method Steps

The sampling method follows the following steps:

1. **Data Sampling**: Samples are extracted from the images, with each sample being a 64x64 region. Two types of samples are created:

   - **Forgery Samples**: These samples contain at least 20% forgery region and 20% original region, extracted from the DEFACTO Copy-Move Dataset.
   - **Original Samples**: These samples are randomly selected from the original images in the Flickr Image Dataset.

2. **Data Preparation**: The sampled data is prepared for training by resizing the images to the appropriate dimensions and normalizing the pixel values.

3. **Model Training**: The data is then used to train the classification models, including the custom model, VGG16, ResNet50, and MobileNetV2.

## Results

The sampling method achieved the following results:

- **Custom Model Accuracy**: The custom model trained on the sampled data achieved an accuracy of 95%.
- **Transfer Learning Models Accuracy**: The transfer learning models (VGG16, ResNet50, MobileNetV2) trained on the sampled data achieved an accuracy of 70%.
