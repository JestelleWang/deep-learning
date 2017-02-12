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

**Template Tracking** 
