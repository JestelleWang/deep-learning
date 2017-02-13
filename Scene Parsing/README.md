# Scene Parsing

Scene parsing, based on semantic segmentation, is a fundamental topic in computer vision. The goal is to assign each pixel in the image a category label. Scene parsing pro- vides complete understanding of the scene. It predicts the label, location, as well as shape for each element. This topic is of broad interest for potential applications of automatic driving, robot sensing, to name a few.  

> **Fully Convolutional Network**  
> J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. In CVPR, pages 3431– 3440, 2015  

## Pyramid Scene Parsing Network

**Several common issues for complex-scene parsing:**

- Mismatched Relationship
- Confusion Categories
- Inconspicuous Classes

### Pyramid Pooling Module

Propose an effective global prior representation to make networks sufficiently incorporate the momentous global scenery prior.  

The pyramid pooling module fuses features under four different pyramid scales. The output of different levels in the pyramid pooling module contains the feature map with varied sizes.  To maintain the weight of global feature, use 1×1 convolution layer after each pyramid level to reduce the dimension of context representation to 1/N of the original one if the level size of pyramid is N. Then upsample the low-dimension feature maps to get the same size feature as the original feature map via bilinear interpolation. Finally, different levels of features are concatenated as the final pyramid pooling global feature.

### Network Architecture

pyramid scene parsing network (PSPNet):

- 1. Input Image
- 2. Use a pretrained ResNet model with the dilated network stategy to extract the **feature map**
- 3. Use the **Pyramid Pooling Module** to gather context information
- 4. **Caoncatenate** the prior with the original feature map
- 5. Follow a convolution layer to generate the **final prediction** map

PSPNet provides an effective global contextual prior for pixel-level scene parsing. The pyramid pooling module can collect a few levels of informa- tion, more representative than global pooling. It is designed for end-to-end learning; thus the global pyramid pooling module and the local FCN feature can be optimized simultaneously.

> **ResNet**   
> K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. CoRR, abs/1512.03385, 2015