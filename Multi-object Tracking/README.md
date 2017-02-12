# Multi-Object Tracking

**Background:**
Online-learning, the learning method conducting learning during tracking, is able to utilize features based on the status and the history of the target. However, there are no ground truth annotations available for supervision so that the method is likely to learn from incorrect training examples if there are errors in the tracking results and these errors can be accumulated and result in *tracking drift*.

## Online Multi-Object Tracking Framework

### Markov Decision Process

- **States** 
	- Active
	- Tracked
	- Inactive
	- Lost
- **Actions and Transition Function**  
	- Active -> Tracked
	- Active -> Inactive
	- Tracked -> Tracked
	- Tracked -> Lost
	- Lost -> Lost
	- Lost -> Tracked
	- Lost -> Inactive 
- **Reward Function** (not given but learned from training data)

### Policy

In MDP, a policy is a mapping from the state space to the action space. The goal of  policy learning is to find a policy which maximizes the total rewards obtained.  

#### Policy in an Active State

Train a binary Support Vector Machine offline to classify a detection into tracked or inactive using a normalized 5D feature vector (2D coordinates, width, height and score of the detection)

#### Policy in a Tracked State

As long as the target is not occluded and is in the camera’s field of view, we should keep tracking it. Otherwise, it should be marked as lost. 

> **TLD tracker** Z.Kalal,K.Mikolajczyk,andJ.Matas.Tracking-learning-detection. TPAMI, 34(7):1409–1422, 2012.

**Template Representation** Whenever an object detection is transferred to a tracked target, initialize the target template with the detection bounding box.  

**Template Tracking** Compute the optical flow and the mean bounding box overlap for the past *K* tracked frames to make the decision.  

> **iterative Lucas-kanade method with pyramids**  
> J.-Y. Bouguet. Pyramidal implementation of the affine lucas kanade feature tracker description of the algorithm. Intel Corporation, 5:1– 10, 2001

**Template Updating** Adopt a "Lazy" updating rule and resort to the object detector in preventing tracking drift. Specifically, the template used in tracking remains unchanged if it is able to track the target. Whenever the template fails to track the tar- get due to appearance change, the MDP transfers the target into a lost state. The “tracking” template is replaced by the associated detection when the target transitions from lost to tracked. Meanwhile, store K templates as the history of the target being tracked.  

#### Policy in a Lost State

In a Lost state, the MDP needs to decide whether to keep the target as lost, transition it to a tracked state, or mark it as inactive. We simply mark a lost target as inactive and terminate the tracking if the target has been lost for more than `T_Lost` frames. The challenging case is to make the decision between tracking the target and keeping it as lost. We treat it as a data association problem: in order to transfer a lost target into a tracked state, the target needs to be asso- ciated with one of the detections from the object detector, otherwise, the target is kept as lost.  

### Multi-Object Tracking with MDPs

After learning the policy/reward of the MDP, we apply it to the multi-object tracking problem. We dedicate a MDP for each object, and the MDP follows the learned policy to track the object. Given a new input video frame, targets in tracked states are processed first to determine whether they should stay as tracked or transfer to lost states. Then we compute pairwise similarity between lost targets and ob- ject detections which are not covered by the tracked targets, where non-maximum suppression based on bounding box overlap is employed to suppress covered detections, and the similarity score is computed by the binary classifier for data association. After that, the similarity scores are used in the Hungarian algorithm to obtain the assignment between detections and lost targets. According to the assignment, lost targets which are linked to some object detections are transferred to tracked states. Otherwise, they stay as lost. Finally, we initialize a MDP for each object detection which is not covered by any tracked target.
