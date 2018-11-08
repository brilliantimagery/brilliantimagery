import os
import sys

import numpy as np
import pytest

path = os.path.dirname(os.path.abspath(__file__))
path, _ = os.path.split(path)
path = os.path.join(path, 'src')

sys.path.insert(len(sys.path), path)

from sequence import Sequence


def test_sequence():
    s = Sequence('E:\\Pictures\\2016\\2016-12-19')
    s.stabilize_sequence([0.5, 0.65, 0.7, 0.85], 7, True)
    s.save()

test_sequence()