# Copy Move Forgery Detection (CMFD) Project

This project aims to address the problem of copy move forgery detection, which involves identifying manipulated images where a portion of the image is copied and pasted onto another region within the same image. The objective of this project is to develop an efficient and accurate forgery detection system using different methodologies.

## Objective

The main objective of this project is to detect instances of copy move forgery in digital images. The project focuses on exploring three different methods for forgery detection: classification, sampling, and object detection. By leveraging these methods, the project aims to improve the accuracy and reliability of forgery detection algorithms.

## Methodologies Used

The project utilizes the following methodologies to tackle the copy move forgery detection problem:

1. **Classification Method**: In this approach, original and forged images are used to train custom models, including VGG16, ResNet50, and MobileNetV2. The models are trained to classify images as either genuine or manipulated. The overall accuracy achieved with this method was approximately 70%.

2. **Sampling Method**: This method involves extracting samples from the images, with each sample being a 64x64 region. The samples are divided into two classes: forgery samples containing at least 20% forgery region and 20% original region, and original samples randomly selected from the original images. The classification models used in the classification method are trained on these samples. The custom model achieved an accuracy of 95%, while the transfer learning models achieved an accuracy of 70%.

3. **Object Detection Method**: In this approach, only the forged images with their corresponding masks are used to train a YOLO (You Only Look Once) model. The model is trained to detect the presence of forgery within the images. This method yielded the best results, with a mean Average Precision (mAP) of 83.9% at an Intersection over Union (IoU) threshold of 0.5.

## Folder Structure

The CMFD main folder contains the following subfolders:

1. **Classification**: This folder contains the scripts, and trained models related to the classification method. It includes the code used to train the custom model, VGG16, ResNet50, and MobileNetV2, on the original and forged images. Additionally, it provides the classification results, including the confusion matrix, classification report, and accuracy for each model.

2. **Sampling**: This folder contains the scripts, and trained models related to the sampling method. It includes the code used to extract samples from the images and train the classification models using these samples. The folder also provides the sampling results, including the confusion matrix, classification report, and accuracy for each model.

3. **Object Detection**: This folder contains the scripts, and trained models related to the object detection method. It includes the code used to train the YOLO model on the forged images and their corresponding masks. The folder also provides the object detection results, including the mean Average Precision (mAP), precision, recall, and F1 score. It also includes a web app for copy move forgery detection, located in the subfolder 'cmfd_web_app'. Please refer to the documentation within the 'cmfd_web_app' subfolder for details on installation, usage, and other relevant information

## Usage

To use this project, follow the steps below:

1. Clone the repository:

```shell
git clone https://github.com/abdomorsi123/Copy_Move_Forgery_Detection.git
```

2. Navigate to the desired subfolder (e.g., Classification, Sampling, or Object Detection) to access the specific implementation and documentation for each method.

3. Follow the instructions provided in each subfolder to run the code, train the models, and evaluate the results.

## Contributing

Contributions to this project are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or submit a pull request. Your contributions can help improve the project and make it more robust.

## License

This project is licensed under the [MIT License](LICENSE).
