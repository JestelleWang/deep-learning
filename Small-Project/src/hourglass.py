import torch.nn as nn

conv = nn.SpatialConvolution.SpatialConvolution
batchnorm = nn.SpatialBatchNormalization.SpatialBatchNormalization
relu = nn.ReLU.ReLU

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
        .add(nn.ConcatTable()                                   \
            .add(convBlock(numIn, numOut))                      \
            .add(skiplayer(numIn, numOut)))                     \
        .add(nn.CAddTable(True))

# Hourglass
def hourglass(n, f, inp):
    # Upper branch
    up1 = inp
    for i in range(nModules):
        up1 = Residual(f, f)(up1)
    low1 = nn.SpatialMaxPooling(2,2,2,2)(inp)
    for i in range(nModules):
        low1 = Residual(f,f)(low1)

    if n > 1:
        low2 = hourglass(n-1, f, low1)
    else:
        low2 = low1
        for i in range(nModules):
            low2 = Residual(f,f)(low2)

    low3 = low2
    for i in range(nModules):
        low3 = Residual(f,f)(low3)
    up2 = nn.SpatialUpSamplintNearest(2)(low3)

    return nn.CaddTable()([up1, up2])
