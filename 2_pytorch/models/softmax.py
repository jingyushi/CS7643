import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F


class Softmax(nn.Module):
    def __init__(self, im_size, n_classes):
        '''
        Create components of a softmax classifier and initialize their weights.

        Arguments:
            im_size (tuple): A tuple of ints with (channels, height, width)
            n_classes (int): Number of classes to score
        '''
        super(Softmax, self).__init__()
        #############################################################################
        # TODO: Initialize anything you need for the forward pass
        #############################################################################
        #pass
        self.num_inputs = im_size[0]*im_size[1]*im_size[2]
        #self.l1=nn.Linear(self.num_inputs,int(self.num_inputs/2))
        self.l1=nn.Linear(self.num_inputs,n_classes)
        #self.l2=nn.Linear(int(self.num_inputs/2),int(self.num_inputs/4))
        #self.l3=nn.Linear(int(self.num_inputs/4),int(self.num_inputs/8))
        #self.l4=nn.Linear(int(self.num_inputs/8),n_classes)
        self.softmax = nn.Softmax()
        #############################################################################
        #                             END OF YOUR CODE                              #
        #############################################################################

    def forward(self, images):
        '''
        Take a batch of images and run them through the classifier to
        produce a score for each class.

        Arguments:
            images (Variable): A tensor of size (N, C, H, W) where
                N is the batch size
                C is the number of channels
                H is the image height
                W is the image width

        Returns:
            A torch Variable of size (N, n_classes) specifying the score
            for each example and category.
        '''
        scores = None
        #############################################################################
        # TODO: Implement the forward pass. This should take very few lines of code.
        #############################################################################
        #pass
        images = images.view(-1,images.shape[1]*images.shape[2]*images.shape[3])
        scores = self.l1(images)
        #scores = self.l2(scores)
        #scores = self.l3(scores)
        #scores = self.l4(scores)
        scores = self.softmax(scores)
        #############################################################################
        #                             END OF YOUR CODE                              #
        #############################################################################
        return scores
