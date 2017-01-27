from __future__ import absolute_import, division, print_function

import pandas as pd

from ggplotx import ggplot, aes, geom_crossbar

n = 4
df = pd.DataFrame({
        'x': [1]*n,
        'ymin': range(1, 2*n+1, 2),
        'y': [i+0.1+i/10 for i in range(1, 2*n+1, 2)],
        'ymax': range(2, 2*n+2, 2),
        'z': range(n)
    })


def test_aesthetics():
    p = (ggplot(df, aes(y='y', ymin='ymin', ymax='ymax')) +
         geom_crossbar(aes('x'), size=2) +
         geom_crossbar(aes('x+1', alpha='z'),
                       fill='green', width=0.2, size=2) +
         geom_crossbar(aes('x+2', linetype='factor(z)'), size=2) +
         geom_crossbar(aes('x+3', color='factor(z)'), size=2) +
         geom_crossbar(aes('x+4', size='z'))
         )

    assert p == 'aesthetics'
