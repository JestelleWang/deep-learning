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

### Layer Implementation

