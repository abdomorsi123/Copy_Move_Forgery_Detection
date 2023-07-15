# Object Detection

This folder contains the scripts, datasets, and trained models related to the object detection method for copy move forgery detection.

![Example of CMFD using YOLO v7](https://github.com/abdomorsi123/Copy_Move_Forgery_Detection/Detection_YOLO/runs/detect/test/0_000000040813.jpg)

## Dataset

The object detection method utilizes a dataset consisting of the following:

1. **DEFACTO Copy-Move Dataset**: This dataset includes images specifically created for copy move forgery detection tasks. It comprises a collection of forged images along with their corresponding masks, totaling 18,000 images.

## Object Detection Method Steps

The object detection method follows the following steps:

1. **Data Preprocessing**: The data preprocessing subfolder includes scripts to prepare the forged images and their corresponding masks for training the object detection model. This step involves resizing the images, generating YOLO labels, and checking the correctness of these labels. Additionally, the data can be split into training and testing sets.

2. **Model Training**: The object detection model, specifically YOLO (You Only Look Once), is trained on the prepared data. The model learns to detect the presence of copy move forgery in the images.

3. **Evaluation**: The trained model is evaluated using standard metrics for object detection, including mean Average Precision (mAP), precision, recall, and F1 score. These metrics provide an assessment of the model's performance in detecting copy move forgery.

## Results

The object detection method achieved the following results:

- **mAP@0.5**: The object detection model achieved a mean Average Precision of 83.9% at an Intersection over Union (IoU) threshold of 0.5.

## CMFD Web App

The CMFD web app subfolder includes the necessary scripts and files to deploy a web application for copy move forgery detection. Detailed documentation for the web app can be found within the subfolder itself, providing information on installation, usage, and other relevant details.

## Setup

```shell
git clone https://github.com/abdomorsi123/Copy_Move_Forgery_Detection.git
cd Detection YOLO
```

- **Before install the modules, make sure that you have python3.9 version and run the model on it.**

- After that, you have to install some python libraries by run the following command:

```shell
pip install -r requirements.txt
```

- Now you can run YOLOv7 model successfully, but it will run over the CPU, so if you want to run it over GPU, install PyTorch by this command:

```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

## Getting Started

```shell
python detect.py --source image.jpg --weights runs/train/yolov7_custom_v3/weights/best.pt --conf 0.25
```
