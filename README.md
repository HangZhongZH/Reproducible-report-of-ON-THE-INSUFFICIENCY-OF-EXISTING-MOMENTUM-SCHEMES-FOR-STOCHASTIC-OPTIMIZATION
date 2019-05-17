# Reproducible-report-of-ON-THE-INSUFFICIENCY-OF-EXISTING-MOMENTUM-SCHEMES-FOR-STOCHASTIC-OPTIMIZATION

In this repository, we provide the source code of ‘Reproducible report of ON THE INSUFFICIENCY OF EXISTING MOMENTUM SCHEMES FOR STOCHASTIC OPTIMIZATION’. 



In folder ’linear regression’, ‘DT.ipynb’ and ‘GB.ipynb’ generate the results of discrete distributed and Gaussian distributed data-sets with SGD, HB, NAG and AccSGD. ‘gridsearch_DT’ and ‘gridsearch_GB’ do the grid search of SGD, HB, NAH and ASGD.


In folder ’deep auto-encoder’, ‘Choose_ASGD.ipynb’, ‘Choose_SGD.ipynb’, ‘Choose_HB.ipynb’ and ‘Choose_NAG.ipynb’ choose the optimal parameters for each of these methods. ‘compare_MNISTsize1.ipynb’ and ‘compare_MNISTsize64.ipynb’ compare the 4 methods with their optimal parameters when batch size is 1 and 64 with the MNIST dataset. ‘compare_FashionMNISTsize1.ipynb’ and ‘compare_FashionMNISTsize64.ipynb’ compare the 4 methods with their optimal parameters when batch size is 1 and 64 with the FashionMNIST dataset.

In foler ‘deep ResNet for Cifar10’, the name of the file shows the setting of parameters. For example, hb120128l means the HB method when batch size 128 and epoch 120 with learning rate decayed.
ASG8_40 means ASGd method for batchsize8 and 40 epoch. And this is the main code.
for running the main code, just run cmd. for example
--asg8_40.py cifar10 --data cifar10 --learning_rate 0.033 --epoch 40 batch_size 8

the resnet code is referenced from https://github.com/D-X-Y/ResNeXt-DenseNet and we modify the code based on that.
 
