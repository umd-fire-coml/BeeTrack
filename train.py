import os
os.chdir('Mask_RCNN')

import skimage.io
import skimage

import sys
import random
import math
import numpy as np
import cv2

import xml.etree.ElementTree

# Root directory of the project
ROOT_DIR = os.path.abspath("./")

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library

from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))  # To find local version
import coco

class BeeDataset(utils.Dataset):

    def load_bee(self, subset):
        """Load a subset of the Balloon dataset.
        dataset_dir: Root directory of the dataset.
        subset: Subset to load: train or val
        """
        # Add classes. We have only one class to add.
        self.add_class("bee", 1, "bee")

        # Train or validation dataset?
       # assert subset in ["train", "val"]
        
        image_dir = "bee_data/bee_data/Images"
        annot_dir = subset

        # do something for each xml file in annotation dir
        for file in os.listdir(annot_dir):

          path = os.path.join(annot_dir, file)

          if os.path.isfile(path) and file.endswith('.xml'):
            
            print(file)

            #assert file.endswith('.xml')
            
            # parse
            eTree = xml.etree.ElementTree.parse(path)
            root = eTree.getroot()

            # trust the hardcode, hope MIT label me does not change
            filename = root[0].text
            #height = int(root[3][0].text)
            #width = int(root[3][1].text)
            width = int(root[3][0].text)
            height = int(root[3][1].text)
            
            polygons = []

            # trust the hardcode, hope MIT label me does not change
            # the first four are metadata
            for obj in root[4:]:
              shape_attr = {
                  'all_points_x': [],
                  'all_points_y': []}
              # polygon is the last element, first one is metadata
              for point in obj[-1][1:]:
                #if int(point[1].text) >= width:
                #    print(point[1].text)
                shape_attr['all_points_x'].append(min(width, int(point[1].text)))
                shape_attr['all_points_y'].append(min(height, int(point[0].text)))
              polygons.append(shape_attr)
            
            #print(height)
            #print(width)
            #print(polygons)

            self.add_image(
                "bee",
                image_id=filename,  # use file name as a unique image id
                path=os.path.join(image_dir, filename),
                width=width, height=height,
                polygons=polygons)

    def load_mask(self, image_id):
        """Generate instance masks for an image.
       Returns:
        masks: A bool array of shape [height, width, instance count] with
            one mask per instance.
        class_ids: a 1D array of class IDs of the instance masks.
        """
        # If not a balloon dataset image, delegate to parent class.
        image_info = self.image_info[image_id]
        if image_info["source"] != "bee":
            return super(self.__class__, self).load_mask(image_id)

        # Convert polygons to a bitmap mask of shape
        # [height, width, instance_count]
        info = self.image_info[image_id]
        mask = np.zeros((info["height"], info["width"], len(info["polygons"])),
                        dtype=np.uint8)
        #print(mask.shape)
        for i, p in enumerate(info["polygons"]):
            # Get indexes of pixels inside the polygon and set them to 1
            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
            mask[rr, cc, i] = 1

        # Return mask, and array of class IDs of each instance. Since we have
        # one class ID only, we return an array of 1s
        return mask.astype(np.bool), np.ones([mask.shape[-1]], dtype=np.int32)

    def image_reference(self, image_id):
        """Return the path of the image."""
        info = self.image_info[image_id]
        if info["source"] == "bee":
            return info["path"]
        else:
            super(self.__class__, self).image_reference(image_id)

#%matplotlib inline 

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "images")

# COCO Class names
class_names = ['BG', 'bee']

# Model Configuration Settings
class TrainConfig(coco.CocoConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    
    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # background + bee
    
    STEPS_PER_EPOCH = 4

config = TrainConfig()
config.display()

# Create model in training mode
model = modellib.MaskRCNN(mode="training", config=config,
                          model_dir=MODEL_DIR)

# Which weights to start with?
init_with = "last"  # imagenet, coco, or last

# Which weights to start with?
#init_with = "coco"  # imagenet, coco, or last

if init_with == "imagenet":
    model.load_weights(model.get_imagenet_weights(), by_name=True)
elif init_with == "coco":
    # Load weights trained on MS COCO, but skip layers that
    # are different due to the different number of classes
    # See README for instructions to download the COCO weights
    model.load_weights(COCO_MODEL_PATH, by_name=True,
                       exclude=["mrcnn_class_logits", "mrcnn_bbox_fc", 
                                "mrcnn_bbox", "mrcnn_mask"])
elif init_with == "last":
    # Load the last model you trained and continue training
    model.load_weights(model.find_last(), by_name=True)
	
# Training dataset
dataset_train = BeeDataset()
dataset_train.load_bee("bee_data/train")
dataset_train.prepare()

# Training dataset
dataset_val = BeeDataset()
dataset_val.load_bee("bee_data/val")
dataset_val.prepare()

#this is meant to train the final terminal layers
#assert init_with == "coco"

# Train the head branches
# Passing layers="heads" freezes all layers except the head
# layers. You can also pass a regular expression to select
# which layers to train by name pattern.
model.train(dataset_train, dataset_val, 
            learning_rate=config.LEARNING_RATE, 
            epochs=60,
            layers=r"(mrcnn_class_logits)|(mrcnn_bbox_fc)|(mrcnn_bbox)|(mrcnn_mask)")