import numpy
import torch

def numpy_squares(k):
  """return (1, 4, 9, .., k'2) as a numpy array"""
  # your code here
  arr = numpy.arange([x**2 for x in range(1, k+1, 1)])
  return arr

def torch_squares(k):
  """return (1, 4, 9, •.., k'2) as a torch array"""
  # your code here
  arr = torch.arange(1, k+1, 1)**2
  return arr
