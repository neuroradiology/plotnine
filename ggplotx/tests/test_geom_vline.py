from __future__ import absolute_import, division, print_function

import pandas as pd
import pytest

from ggplotx import ggplot, aes, geom_vline, geom_point
from ggplotx.utils.exceptions import GgplotError

df = pd.DataFrame({
        'xintercept': [1, 2],
        'x': [0.5, 3],
        'y': [-1, 1],
        'z': range(2)
    })


def test_aesthetics():
    p = (ggplot(df) +
         geom_point(aes('x', 'y')) +
         geom_vline(aes(xintercept='xintercept'), size=2) +
         geom_vline(aes(xintercept='xintercept+.1', alpha='z'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.2',
                        linetype='factor(z)'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.3',
                        color='factor(z)'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.4', size='z')))

    assert p == 'aesthetics'


def test_aes_inheritance():
    with pytest.raises(GgplotError):
        p = (ggplot(df, aes('x', 'y', xintercept='xintercept')) +
             geom_point() +
             geom_vline(size=2))
        print(p)
