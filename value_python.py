#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:38:15 2023
@author: michael chukwuka
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
values = np.arange(1,10) 
prob = (0.111111, 0.111111, 0.111111, 0.111111, 0.111111, 0.111111, 0.111111, 0.111111, 0.111111) # probabilities must sum to 1
custm = stats.rv_discrete(values=(values, prob))

for i in range(10000):
    print(custm.rvs())
