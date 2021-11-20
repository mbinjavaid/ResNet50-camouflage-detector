import config
from imutils import paths
import random
import shutil
import os

# get the paths to all input images in the input folder
# and shuffle them
imagePaths = list(paths.list_images(config.ORIG_INPUT_DATASET))
random.seed(2614)
random.shuffle(imagePaths)

# calculate the training and testing split
i = int(len(imagePaths) * config.TRAIN_SPLIT)
trainPaths = imagePaths[:i]
testPaths = imagePaths[i:]

# use some of the training data for validation
i = int(len(trainPaths) * config.VAL_SPLIT)
valPaths = trainPaths[:i]
trainPaths = trainPaths[i:]

# define the datasets to build
datasets = [("training", trainPaths, config.TRAIN_PATH),
            ("validation", valPaths, config.VAL_PATH),
            ("testing", testPaths, config.TEST_PATH)]

# loop over the individual datasets
for (dType, imagePaths, baseOutput) in datasets:
    print("[INFO] building '{}' split".format(dType))
    if not os.path.exists(baseOutput):
        print("[INFO] 'creating {}' directory".format(baseOutput))
        os.makedirs(baseOutput)
    # loop over the input image paths
    for inputPath in imagePaths:
        # extract the filename of the input image along with its
        # corresponding class label
        filename = inputPath.split(os.path.sep)[-1]
        label = inputPath.split(os.path.sep)[-2]
        # build the path to the label directory
        labelPath = os.path.sep.join([baseOutput, label])
        # if the label output directory does not exist, create it
        if not os.path.exists(labelPath):
            print("[INFO] 'creating {}' directory".format(labelPath))
            os.makedirs(labelPath)
        # construct the path to the destination image and then copy
        # the image
        p = os.path.sep.join([labelPath, filename])
        shutil.copy2(inputPath, p)

