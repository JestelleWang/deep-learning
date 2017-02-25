# Hourglass Network for Human Segmentation

The "stacked hourglasss" network captures and consolidates information across all scales of the image. Now I will introduce its architecture and apply it to *human segmentation*.  

## Network Architecture

> The Network Architecture is cited from  
> **Stacked Hourglass Networks for Human Pose Estimation**  
> arxiv:1603.06937v2 [cs.CV]

### Hourglass Design

The design of the hourglass is motivated by the need to capture information at every scale. The hourglass is a simple, minimal design that has the capacity to capture all of the features and bring them together to output pixel-wise predictions.  

The network use a single pipeline with skip layers to preserve spatial information at each resolution. The network reaches its lowest resolution at 4x4 pixels allowing smaller spatial filters to be applied that compare features across the entire space of the image.  

The hourglass is set up as follows: Convolutional and max pooling layers are used to process features down to a very low resolution. At each max pooling step, the network branches off and applies more convolutions at the original pre-pooled resolution. After reaching the lowest resolution, the network begins the top-down sequence of upsampling and combination of features across scales. The topology of the hourglass is symmetric, so for every layer present on the way down there is a corresponding layer going up.

## Data Access

Download the segmentation masks <a href="http://www.stat.ucla.edu/~xianjie.chen/pascal_part_dataset/pascal_part.html">here</a>. But it can't be used to train the network directly. You should preprecess it at first.  

At first, extract the **person category** images from <a href="http://host.robots.ox.ac.uk/pascal/VOC/voc2010/">PASCAL VOC 2010</a>. I write a script to handle this. It is at `script` folder and named `person_ctg.pl`. After modifying the file paths you print following command to run it:


```
perl person_ctg.pl
``` 

Then you will extract the person category images. I get a bit more than 1000 pictures which are well to train. Also I have got a list of this images, used in training code.  

Another troublesome problem is how to deal with annotations in `.mat` format. Because my code is written in `python`, so I use `scipy.io.loadmat` to read the file and load the annotations. The format transfered by `scipy` is strange, but I don't come up with more smart measure.