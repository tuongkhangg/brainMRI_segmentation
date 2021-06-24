# Using Deep Learning to segment a tumor in a Brain MR image.

Authors:
1.  Duong Le Tuong Khang
2.  La Truong Hai

This github includes preprocessing algorithms, segmentation models and post-processing method

## Dataset:
We use dataset from a paper: Association of genomic subtypes of lower-grade gliomas with shape features automatically extracted by a deep learning algorithm

## Preprocessing
We implement CLAHE to image and resize it to common frame (256x256). 

## Segmentation Models
We compare some models like Unet, Unet++ and analysis advantages and drawbacks between them. Furthermore, we distinguish a number of loss functions: BCE-Dice loss, tversky loss, focal tversky loss and Jaccard Loss. Also, in this project, we study about how adam and sgd optimization affected model and provide a summary about them.

## Post-processing
When we had a model, we recognized some drawbacks. Initially, some holes and small regions emerged in masks. To solve this problem, we apply a algorithms that it finds a connected components and deletes follow to a threshold.

