import os
import sys

import numpy as np
import pytest

path = os.path.dirname(os.path.abspath(__file__))
path, _ = os.path.split(path)
path = os.path.join(path, 'src')

sys.path.insert(len(sys.path), path)

from sequence import Sequence


def test_stabelize():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.stabilize([0.5, 0.65, 0.7, 0.85], 7, True)
    s.save()

def test_reamp():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.ramp([0.5, 0.65, 0.7, 0.85])


test_stabelize()
# test_reamp()