# BeeTrack
This is a work in progress. We are trying to track bees with CNNs.

Currently, we are unsure if we want to track physically unmarked bees or not. We think we will try the first, because it is a harder problem.

The problem with that is we literally don't have a dataset. We are labeling bees on our own. It is estimated to take +5 minutes per image (according to Mr. Ho)

So we don't have a dataset actually. However, we are gratefull for the bee videos sent to us from the Biorobotics Lab at the Free University of Berlin. Here are the videos:

https://drive.google.com/drive/folders/1Mx3yAJn2YVNs1iivuREKL6HTq9hkssqH

Originally, we were going through the process of implementing this model:

![alt image](model_plot.png)


Now we are using Ternaus.

# Getting Started
* [demo.ipynb](demo.ipynb) This code clones the Ternaus Net repo and run an image such as this one:

![alt image](TernausNet/the_smaller_image.png)

Running the code is simple:
1) Use pip or anaconda with the requirements.txt to install requirements.
2) Run the demo.ipynb
(Open/run the jupyter notebook.)

Here is an output:

![alt image](output.png)
