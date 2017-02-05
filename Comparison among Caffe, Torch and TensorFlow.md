# Comparison among Caffe, Torch and TensorFlow

As we know there are several most famous deep learning software frameworks, and I take a try to make a comparison among three of them: Caffe, Torch and TensorFlow.  

## Caffe

Caffe is a strong image classifer framework and seems to remain stagnant. Though the fact that it has been stoped at version1.0 RC3 for over 1 year and its founder has left the project， caffe still has good convolution network imaage recognition and good support for Nvidia CUDA GPU.  

Caffe has a command line, Python and Matlab interface, it relies on ProtoText file to define its model and solver. Caffe defines the network layer by layer in its own model pattern. The network is defined from the input data to the missing entire model. When data and derived data traverse the network in forward and backward directions, the Caffe stores, communicates, and manipulates information as blobs (Binary Large Objects) and internally as N-dimensional arrays stored in C-contiguous form (representing rows that are stored in contiguous Of the memory block, as in the C language). Blob in Caffe, such as Tensor of TensorFlow.  

The layer performs operations on blobs and forms the components of the Caffe model. Layer convolution filter, execution pool, internal product, application of non-linearity (such as rectification of linear and sigmoidal and other elemental aspects of transformation), normalization, loading of data and calculation of losses such as softmax and hinges.  

Caffe has proved its sufficiency but its time seems to have been gone.

## Torch

Torch is an open source machine learning library, and a script language based on the Lua programming language. It provides a wide range of algorithms for deep machine learning, and uses the scripting language LuaJIT, and an underlying C implementation.  

As Torch is based on LuaJIT, it maybe hard to get start. The other days, Facebook release PyTorch so that more and more people can use python to use this library without learning Lua.  

## TensorFlow

TensorFlow, Google's portable machine learning and neural network library, performs well and scales well, although it's a little harder to learn. TensorFlow has a wide variety of models and algorithms that attach great importance to deep learning and have excellent performance on hardware with GPU (for training) or Google TPU (for production-scale prediction). It also has good support for Python, good documentation and good software for displaying and understanding the data flow graph TensorBoard that describes its calculations.  

The nodes in the data flow graph represent mathematical operations, and the edges of the graph represent multidimensional data arrays (tensors) flowing between them. This flexible architecture allows you to deploy computing to one or more CPUs or GPUs in the desktop, server, or mobile device without rewriting the code.   

The primary language used with TensorFlow is Python, although limited support for C ++. TensorFlow provides tutorials that include handwritten numbers. Image recognition, word embedding, recurrent neural networks, sequence-to-sequence models for machine translation, natural language processing and PDE-based simulation.   

TensorFlow can easily handle a variety of neural networks, including the depth of CNN and LSTM recursive models in the rapidly changing image recognition and language processing field. The code used to define the layer may be fan, but you can easily but not in detail, you can use any of the three optional depth learning interfaces to repair it. While debugging an asynchronous network solver can be trivial, the TensorBoard software can help you visualize the graph.



