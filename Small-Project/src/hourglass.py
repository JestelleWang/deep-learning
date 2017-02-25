#!/usr/bin/env python
import time

import numpy as np 
from scipy.io import loadmat
import cv2

import torch
import torch.nn as nn

# DEFINE ENVIRONMENT VARIABLES
ANNOTATION_PATH = '../data/Annotations_Part'
PERSON_LIST = '../data/person_category.txt'
IMAGE_PATH = '../data/Images'
TRAIN_EPOCH = 1000
LR = 0.1


conv = nn.SpatialConvolution.SpatialConvolution
batchnorm = nn.SpatialBatchNormalization.SpatialBatchNormalization
relu = nn.ReLU.ReLU

# define person segmention. You can define it according to your demands.
# To simplify the problem I just define five organs.
classes = {
    'head' : 0, 
    'llarm': 1, 
    'luarm': 1,
    'lhand': 1,
    'rlarm': 2,
    'ruarm': 2,
    'rhand': 2, 
    'llleg': 3,
    'lrleg': 3,
    'lfoot': 3, 
    'rlleg': 4,
    'ruleg': 4,
    'rfoot': 4
}


# Main convlutional block
def convBlock(numIn, numOut):
    return nn.Sequential()                                      \
        .add(batchnorm(numIn))                                  \
        .add(relu(True))                                        \
        .add(conv(numIn, numOut / 2, 1, 1))                     \
        .add(batchnorm(numOut / 2))                             \
        .add(relu(True))                                        \
        .add(conv(numOut / 2, numOut / 2, 3, 3, 1, 1, 1, 1))    \
        .add(batchnorm(numOut / 2))                             \
        .add(relu(True))                                        \
        .add(conv(numOut / 2, numOut, 1, 1))


# Skip layer
def skipLayer(numIn, numOut):
    if numIn == numOut:
        return nn.Identity()
    else:
        return nn.Sequential().add(conv(numIn, numOut, 1, 1))


# Residual block
def Residual(numIn, numOut):
    return nn.Sequential()                                      \
        .add(nn.ConcatTable()
            .add(convBlock(numIn, numOut))
            .add(skipLayer(numIn, numOut)))                     \
        .add(nn.CAddTable(True))


# Hourglass
def hourglass(n, numIn, numOut, inp):
    up1 = Residual(numIn, 256)(inp)
    up2 = Residual(256, 256)(up1)
    up4 = Residual(256, numOut)(up2)

    pool = nn.SpatialMaxPooling(2, 2, 2, 2)(inp)
    low1 = Residual(numIn, 256)(pool)
    low2 = Residual(256, 256)(low1)
    low5 = Residual(256, 256)(low2)
    low6 = hourglass(n - 1, 256, numOut, low5) if n > 1 else Residual(256, numOut)(low5)

    low7 = Residual(numOut, numOut)(low6)
    up5 = nn.SpatialUpSamplingNearest(2)(low7)

    return nn.CaddTable()([up4, up5])


def lin(numIn, numOut, inp):
    # Apply 1x1 convolution, stide 1, no padding
    l_ = nn.SaptialConvolution(numIn, numOut, 1, 1, 1, 1, 0, 0)(inp)
    return nn.ReLU(True)(nn.SpatialBatchNormalization(numOut)(l_))


def createModel():
    inp = nn.Identity()()

    # Initial processing of the image
    cnv1_ = nn.SpatialConvolution(3, 64, 7, 7, 2, 2, 3, 3)(inp)
    cnv1 = nn.ReLU(True)(nn.SpatialBatchNormalization(64)(cnv1_))
    r1 = Residual(64, 128)(cnv1)
    pool = nn.SpatialMaxPooling(2, 2, 2, 2)(r1)
    r4 = Residual(128, 128)(pool)
    r5 = Residual(128, 128)(r4)
    r6 = Residual(128, 256)(r5)

    # First hourglass
    hg1 = hourglass(4, 256, 512, r6)

    # Linear layers to produce first set of predictions
    l1 = lin(512, 512, hg1)
    l2 = lin(512, 256, l1)

    # First predicted heatmaps
    out1 = nn.SpatialConvolution(256, outputDim[1][1], 1, 1, 1, 1, 1, 0, 0)(l2)
    out1_ = nn.SpatialConvolution(outputDim[1][1], 256 + 128, 1, 1, 1, 1, 0, 0)(out1)

    # Concatenate with previous linear features
    cat1 = nn.JoinTable(2)([l2, pool])
    cat1_ = nn.SpatialConvolution(256 + 128, 256 + 128, 1, 1, 1, 1, 0, 0)(cat1)
    int1 = nn.CaddTable()([cat1_, out1_])

    # Second hourglass
    hg2 = hourglass(4, 256 + 128, 512, int1)

    # Linear layers to produce predictions again
    l3 = lin(512, 512, hg2)
    l4 = lin(512, 512, l3)

    # Output heatmaps
    out2 = nnlib.SpatialConvolution(512, outputDim[2][1], 1, 1, 1, 1, 0, 0)(l4)

    # Final Model
    model = nn.gModule([inp], [out1, out2])

    return model


# load the annotations
def loadAnno(number):
    filename = ANNOTATION_PATH + str(number) + '.mat'
    data = loadmat(filename)
    persons = filter(lambda x: x['class'] == 'person', data['anno']['objects'][0][0][0])
    annotations = np.zeros(5)
    for person in persons:
        parts = person['parts'][0]
        for part in parts:
            part_name =  part['part_name'][0]
            if part_name in classes:
                if annotations[part_time] == 0:
                    annotations[classes[part_name]] = part['mask']
                else:
                    annotations[classes[part_name]] += part['mask']
    return annotations


# load the images
def loadImage(number):
    filename = IMAGE_PATH + str(number) + '.jpg'
    img = cv2.imread(filename)
    res = cv2.resize(img, (256, 256))
    return torch.from_numpy(res).float()


def train(number, model, criterion, optimizer, epoch):
    start = time.time()

    # load data
    anno = loadAnno(number)
    img = loadImage(number)

    input_var = torch.autograd.Variable(img)
    target_var = torch.autograd.Variable(anno)

    # compute output
    output = model(input_var)
    loss = criterion(output, target_var)

    # compute gradient and do SGD step
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    end = time.time()
    print "Training Epoch: %s Image: %s Time: %s\n" % (epoch, number, end - start)


def adjust_learning_rate(optimizer, epoch):
    """sets the learning rate to the initial LR decayed by 10 every 30 epochs"""
    lr = LR * (0.1 ** (epoch // 30))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr


def main():
    person_file = open(PERSON_LIST, 'r')
    persons = person_file.readlines()

    model = createModel()

    # define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), LR)

    for epoch in TRAIN_EPOCH:
        adjust_learning_rate(optimizer, epoch)
        for person in persons:
            number = person[:-1]
            train(number, model, criterion, optimizer, epoch)
   