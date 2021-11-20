# ResNet50-camouflage-detector
Transfer learning to detect general camouflaged objects in images, using ResNet50 pre-trained on ImageNet

In short: we chop off the fully connected head, and train a new FC head on top. The purpose is to classify images into two categories: those with a camouflaged object (animal, person, pretty much anything utilizing camouflage to hide against the background), and those without a camouflaged object in the image. The CAMO-COCO dataset (https://sites.google.com/site/vantam/camo-1) was used for training, with a test-validation split as defined in config.py. I didn't use the segmentation masks provided in the dataset, so you have to delete those/move them elsewhere after downloading so they don't interfere with the model training.

To train the model, download the CAMO-COCO dataset, first copy it into the program directory. Since the dataset_builder.py assumes a certain format, organize the folder as follows: "CAMO-COCO-1.0-DATA/Camouflage" should contain all camouflage images (no matter whether originally test or train images), and "CAMO-COCO-1.0-DATA/Non-Camouflage" should likewise contain all non-camouflage images. Then run dataset_builder.py to create a nicely organized directory of the training and validation split which will later be used in training. You may need to change the ORIG_INPUT_DATASET value in config.py to the name of the folder containing the original dataset (in my case it was CAMO-COCO-1.0-DATA).

The obtained result (accuracy and loss) metrics over epochs are depicted in progress.png.
