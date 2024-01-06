'''
    Clean functions for ipynb
'''
import sys 
import gc
import torch
import traceback
def clean_ipython_hist():
    # Code in this function mainly copied from IPython source
    if not 'get_ipython' in globals(): return
    ip = get_ipython()
    user_ns = ip.user_ns
    ip.displayhook.flush()
    pc = ip.displayhook.prompt_count + 1
    for n in range(1, pc): user_ns.pop('_i'+repr(n),None)
    user_ns.update(dict(_i='',_ii='',_iii=''))
    hm = ip.history_manager
    hm.input_hist_parsed[:] = [''] * pc
    hm.input_hist_raw[:] = [''] * pc
    hm._i = hm._ii = hm._iii = hm._i00 =  ''
    
def clean_tb():
    # h/t Piotr Czapla
    if hasattr(sys, 'last_traceback'):
        traceback.clear_frames(sys.last_traceback)
        delattr(sys, 'last_traceback')
    if hasattr(sys, 'last_type'): delattr(sys, 'last_type')
    if hasattr(sys, 'last_value'): delattr(sys, 'last_value')
    
    
def clean_mem():
    clean_tb()
    clean_ipython_hist()
    gc.collect()
    torch.cuda.empty_cache()
    
    
"""
How to initialize weights:

We have to scale our weight matrices exactly right so that the standard deviation 
of our activations stays at 1. We can compute the exact value to use mathematically, 
as illustrated by Xavier Glorot and Yoshua Bengio in ["Understanding the Difficulty 
of Training Deep Feedforward Neural Networks"](http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf). 
The right scale for a given layer is $1/\sqrt{n_{in}}$, where $n_{in}$ represents the number of inputs.

BUT when we use ReLU it doesn't work. Instead:

In ["Delving Deep into Rectifiers: Surpassing Human-Level Performance"](https://arxiv.org/abs/1502.01852) 
Kaiming He et al. show that we should use the following scale instead: 
$\sqrt{2 / n_{in}}$, where $n_{in}$ is the number of inputs of our model.
"""
# from math import sqrt

# def relu(x): return x.clamp_min(0.)

# x = torch.randn(200, 100)
# for i in range(50): x = x @ (torch.randn(100,100) * sqrt(1/100))
# x[0:5,0:5]

# x = torch.randn(200, 100)
# for i in range(50): x = relu(x @ (torch.randn(100,100) * sqrt(2/100)))
# x[0:5,0:5]

# def init_weights(m, leaky=0.):
#     if isinstance(m, (nn.Conv1d,nn.Conv2d,nn.Conv3d)): init.kaiming_normal_(m.weight, a=leaky)
# model.apply(init_weights)

# @inplace
# def transformi(b): b[xl] = [(TF.to_tensor(o)-xmean)/xstd for o in b[xl]]
# tds = dsd.with_transform(transformi)
# dls = DataLoaders.from_dd(tds, bs, num_workers=4)
# xb,yb = next(iter(dls.train))

"""
# See details in fastai/11_initializing.ipynb...

Initialize weights with mean = 0 and std = 1 
Use LeakyReLU activations
[All You Need is a Good Init](https://arxiv.org/pdf/1511.06422.pdf) introduces *Layer-wise Sequential Unit-Variance* (*LSUV*).
Use layer normalization or batch normalization - something like LSUV
Use dropout
"""

#Layer Normalization: [layer normalization](https://arxiv.org/abs/1607.06450)
# class LayerNorm(nn.Module):
#     def __init__(self, dummy, eps=1e-5):
#         super().__init__()
#         self.eps = eps
#         self.mult = nn.Parameter(tensor(1.))
#         self.add  = nn.Parameter(tensor(0.))

#     def forward(self, x):
#         m = x.mean((1,2,3), keepdim=True) #NCHW -> mean(C,H,W)
#         v = x.var ((1,2,3), keepdim=True)
#         x = (x-m) / ((v+self.eps).sqrt())
#         return x*self.mult + self.add