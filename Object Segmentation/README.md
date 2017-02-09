# Object Segmentation

**Instance-aware semantic segmentation** task can be decomposed into three different and related sub-tasks:

- Defferentiating instances
- Estimating masks
- Categorizing objects

## Multi-task Network Cascades

### proposing box-level instances

**Input:** an image of arbitrary size  
**Output:** bounding box locations and objectness scores  

Region Proposal Networks (RPNs)

> see this in Object Detection

### regressing mask-level instances

**Input:** shared convolutional features and stage-1 boxes  
**Output:** a pixel-level segmentation mask for each box proposal

Given a box predicted by stage 1, extract a feature of box by Region-of-Interest (RoI) pooling, which producing a fixed-size feature from an arbitrary box.

Two extra fully-connected (fc) layers after this feature for each box:

- First reduces the dimension to 256
- Second regress a pixel-wise mask

### categorizing each instance

**Input:** the shared convolutional features, stage-1 boxes, and stage-2 masks  
**Output:** category scores for each instance  

Concatenate mask-based and box-based pathways and use a softmax classifier of N+1 ways to predict N categories plus one background category.  

#### mask-based pathway

Given a box predicted by stage 1, extract a fea- ture by RoI pooling. This feature map is then “masked” by the stage-2 mask prediction, inspired by the feature mask- ing strategy. This leads to a feature focused on the foreground of the prediction mask.

#### box-based pathways

See this here.

> B. Hariharan, P. Arbela ́ez, R. Girshick, and J. Malik. Simul-