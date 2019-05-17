import torch

#import models

# =============================================================================
# #sgd16model = torch.load('sgd8model.pth.tar',map_location='cpu')
# sgd16check = torch.load('sgd128check.pth.tar',map_location='cpu')
# #nag16_10model = torch.load('nag16_10model.pth.tar',map_location='cpu')
# nag16_10check = torch.load('nag8_40check.pth.tar',map_location='cpu')
# #hb16_10check = torch.load('hb16_10check.pth.tar',map_location='cpu')
# hb16_10check = torch.load('hb8_40check.pth.tar',map_location='cpu')
# #asgd16_10model = torch.load('asgd16_10model.pth.tar',map_location='cpu')
# asg16_10check = torch.load('asg8_40check.pth.tar',map_location='cpu')
# 
# =============================================================================
sgd128check = torch.load('sgd8_40lcheck.pth.tar',map_location='cpu')
#nag16_10model = torch.load('nag16_10model.pth.tar',map_location='cpu')
nag128_120check = torch.load('nag8_40lcheck1.pth.tar',map_location='cpu')
#hb16_10check = torch.load('hb16_10check.pth.tar',map_location='cpu')
hb128_120check = torch.load('hb8_40lcheck1.pth.tar',map_location='cpu')
#asgd16_10model = torch.load('asgd16_10model.pth.tar',map_location='cpu')
asg8_40check1 = torch.load('asg8_40lcheck1.pth.tar',map_location='cpu')
asg128_120check1k = torch.load('asg128_120lcheck1k.pth.tar',map_location='cpu')