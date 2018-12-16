# BeeTrack
This is (was?) a work in progress. We were trying to track bees with CNNs.

The problem we had was the lack of a labeled dataset. However, we are grateful for the bee videos sent to us from the Biorobotics Lab at the Free University of Berlin. Here are the videos:

https://drive.google.com/drive/folders/1Mx3yAJn2YVNs1iivuREKL6HTq9hkssqH

https://github.com/BioroboticsLab/

![alt image](bee_train180.png)

Here are the weights for epoch 180.

https://drive.google.com/open?id=167kpM5VTyNSJoeaRiNRPEmNfMq--36hj

We tried to track both physically unmarked and marked bees.

Originally, we were going through the process of implementing this model:

![alt image](model_plot.png)


Then we were going to use TernausNet.

Now we are using Mask RCNN.

# Getting Started
* Todo

Look below for legacy stuff

* [demo.ipynb](demo.ipynb) This code clones the Ternaus Net repo and run an image such as this one:

![alt image](the_smaller_image.png)

Running the code is simple:
1) Use pip or anaconda with the requirements.txt to install requirements.
2) Run the demo.ipynb
(Open/run the jupyter notebook.)
