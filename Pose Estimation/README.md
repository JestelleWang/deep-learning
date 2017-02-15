# Pose Estimation

Human 2D pose estimation, the problem of localizing anatomical landmarks or parts, has largely focused on finding parts of individuals. Inferring the pose of multiple people in images, especially socially engaged individuals, presents a unique set of challenges. One common approach is to divide and conquer the problem by employing a person detector and performing single-person pose estimation for each detection. These top-down approaches directly leverage exist- ing techniques for single-person pose estimation, but suffer from early commitment: if the person detector fails–as it is prone to do when people are in close proximity–there is no recourse to recovery. Furthermore, the runtime of these top-down approaches is proportional to the number of people: for each detection, a single-person pose estimator is run, and the more people there are, the greater the computational cost. In contrast, bottom up approaches are attractive as they offer robustness to early commitment and have the potential to decouple runtime complexity from the number of people detected in the image. Yet, bottom-up approaches do not benefit directly from global information, which is critical in utilizing contextual cues from other body parts and other people.  

## Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields

Divide the problem into two tasks: body part detection and part association.  

### Confidence Maps for Part Detection

Use the confidence map representation which models the part locations as Gaussian peaks in the map. Take the maximum of the confidence maps so that the precision of close-by peaks remain distinct.  

### Part Affinity Fields for Part Association

To assemble a set of detected body parts to form the full-body poses of an unknown number of people, we need a measurement of the confidence for each pair of two body part detections that they are associated from the same person. We present a novel feature representationwe call a part affinity field that preserves both location andorientation information required to perform body part as-sociation. 


