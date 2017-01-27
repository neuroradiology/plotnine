from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

from ggplotx import ggplot, aes, geom_density

n = 6  # Some even number greater than 2

# ladder: 0 1 times, 1 2 times, 2 3 times, ...
df = pd.DataFrame({'x': np.repeat(range(n+1), range(n+1)),
                   'z': np.repeat(range(n//2), range(3, n*2, 4))})

p = ggplot(df, aes('x', fill='factor(z)'))


def test_gaussian():
    p1 = p + geom_density(kernel='gaussian', alpha=.3)
    assert p1 == 'gaussian'


def test_gaussian_trimmed():
    p2 = p + geom_density(kernel='gaussian', alpha=.3, trim=True)
    assert p2 == 'gaussian-trimmed'


def test_triangular():
    p3 = p + geom_density(kernel='triangular', alpha=.3)  # other
    assert p3 == 'triangular'
