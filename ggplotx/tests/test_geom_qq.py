from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

from ggplotx import ggplot, aes, geom_qq

prng = np.random.RandomState(1234567890)


def test_normal():
    df = pd.DataFrame({'x': prng.normal(size=100)})
    p = ggplot(df, aes(sample='x')) + geom_qq()
    # Roughly a straight line of points through the origin
    assert p == 'normal'
