# Dog-Breeds-Recognition

### Demo: https://youtu.be/CbxXV22Bjvs

## 1. Introduction
Image Recognition is one of the thriving fields in machine learning and deep learning. Based on image recognition, people can do image caption, object segmentation and other exciting and impressive researches. These techniques can then construct as machine learning foundations and develop into real-world applications that are used globally on all devices and platforms.

I’d like to train a neural network that recognizes and segments different breeds of dogs. After the neural network model is established, I put together the predicting model with an interface that enables users to upload their pictures of dogs, and shows some interesting facts and information about the dog breeds that are predicted. I look forward to the project as the inputs are vivid (and adorable!) images of dogs and puppies and the process should bring a lot of fun.

## 2. Dataset
The dataset I use can be found here: https://www.kaggle.com/jessicali9530/stanford-dogs-dataset.

The Stanford Dogs dataset contains images of 120 breeds of dogs from around the world. This dataset has been built using images and annotation from ImageNet for the task of fine-grained image categorization. It was originally collected for fine-grained image categorization, a challenging problem as certain dog breeds have near identical features or differ in colour and age.

The dataset contains 120 categories and 20,580 images of dogs and puppies in different colors and ages. The original data source is found here and contains additional information on the train/test splits and baseline results.

The dataset is cited on the following papers:
Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao and Li Fei-Fei. Novel dataset for Fine-Grained Image Categorization. First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.
J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li and L. Fei-Fei, ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and Pattern Recognition (CVPR), 2009.

## 3. Usage
Before you start, download the model file (https://drive.google.com/open?id=1nHb_lOX0gtEZXRQDLo9KhkD3YeKdZ_7Y) and place it in gui/.

After cloning the project from Github:
```
python3 csce636_finalproject_vgg16.py
```
Running this python code will automatically generate train / validation / test datasets.
The following code trains and tests a CNN model based on VGG 16 with input images from the datasets.

To activate the application with GUI, after downloading the model file from Google Drive, go to gui/ and execute gui.py:
```
cd gui/
python3 gui.py
```
