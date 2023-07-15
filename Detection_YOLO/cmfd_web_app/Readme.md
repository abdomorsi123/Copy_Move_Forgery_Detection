# CMFD Web App

I built a Flask web application for the Copy Move Forgery Detection (CMFD) project. You can use this web app for object detection instead of dealing with the command prompt.

You can also use this web app with any YOLOv7 project by simply replacing the `best.pt` file with your own model file.

## Setup

To get started with the CMFD web app, follow the steps below:

1. Clone the repository:

```shell
git clone https://github.com/abdomorsi123/Copy_Move_Forgery_Detection.git
```

2. Navigate to the cloned directory:

```shell
cd Detection YOLO/cmfd_web_app

```

3. Before installing the required modules, ensure that you have Python 3.9 version and run the model on it.

4. Install the necessary Python libraries by running the following command:

```shell
pip install -r requirements.txt

```

Note: If you want to run the model on a GPU, install PyTorch with GPU support using the following command:

```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

## Getting Started

To start using the CMFD web app, run the following command:

```shell
python app.py
```

This command will start the web application, and you can access it through your web browser.
