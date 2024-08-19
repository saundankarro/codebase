#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    
    ltrs = s.split()
    sorted_list = item for items, c in Counter(a).most_common() for item in [items] * c