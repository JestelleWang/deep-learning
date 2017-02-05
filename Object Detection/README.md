# Object Detection

## Faster R-CNN

Faster R-CNN is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector  that uses the proposed regions. The entire system is a single, unified network for object detection.

### Region Proposal Networks

A Region Proposal Network (RPN) takes an image as input and outpus a set of rectangular object proposals, each with an objectness score. 

**1. Anchors :**

At each sliding-window location, predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as *k*. The k proposals are param- eterized relative to k reference boxes, which we call *anchors*. An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio.

- Translation-Invariant
- Multi-scale addressed

> Anchor-based method is built on a pyramid of anchors, which is more cost-efficient. The method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios. It only relies on images and feature maps of a single scale, and uses filters (sliding win- dows on the feature map) of a single size. 

**2. Loss Function:**

Two kinds of anchors:

-  the anchor/anchors with the highest Intersection-over- Union (IoU) overlap with a ground-truth box
-  an anchor that has an IoU overlap higher than 0.7 with
any ground-truth box.

**3. Training RPNs:**

The RPN can be trained end-to-end by backpropagetion and stochastic gradient descent (SGD).

### Sharing Features for RPN and Fast R-CNN

Three ways for training networks with features shared:

- **Altenating traing.** First train RPN and use the proposals to train Fast T-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated.
- **Approximate joint training.** The RPN and Fast R-CNN networks are merged into one network during training. In each SGD iteration, the forward pass generates region proposals which are treated just like fixed, pre-computed proposals when training a Fast R-CNN detector. The backward propagation takes place as usual, where for the shared layers the backward propagated signals from both the RPN loss and the Fast R-CNN loss are combined. 
- **Non-approximate joint training.** Use an RoI pooling layer that is defferentiable w.r.t the box coordinates.

> TODO J. Dai, K. He, and J. Sun, “Instance-aware semantic segmenta- tion via multi-task network cascades,” arXiv:1512.04412, 2015.

