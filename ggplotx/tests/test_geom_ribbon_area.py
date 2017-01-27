from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd

from ggplotx import (ggplot, aes, geom_area, geom_ribbon,
                     scale_x_continuous)

n = 4            # No. of ribbions in a vertical stack
m = 100          # Points
width = 2*np.pi  # width of each ribbon
x = np.linspace(0, width, m)

df = pd.DataFrame({
        'x': np.tile(x, n),
        'ymin': np.hstack([np.sin(x)+2*i for i in range(n)]),
        'ymax': np.hstack([np.sin(x)+2*i+1 for i in range(n)]),
        'z': np.repeat(range(n), m)
    })


def test_ribbon_aesthetics():
    p = (ggplot(df, aes('x', ymin='ymin', ymax='ymax',
                        group='factor(z)')) +
         geom_ribbon() +
         geom_ribbon(aes('x+width', alpha='z')) +
         geom_ribbon(aes('x+2*width', linetype='factor(z)'),
                     color='black', fill=None, size=2) +
         geom_ribbon(aes('x+3*width', color='z'),
                     fill=None, size=2) +
         geom_ribbon(aes('x+4*width', fill='factor(z)')) +
         geom_ribbon(aes('x+5*width', size='z'),
                     color='black', fill=None) +
         scale_x_continuous(
             breaks=[i*2*np.pi for i in range(7)],
             labels=['0'] + ['${}\pi$'.format(2*i) for i in range(1, 7)])
         )

    assert p == 'ribbon_aesthetics'


def test_area_aesthetics():
    p = (ggplot(df, aes('x', 'ymax+2', group='factor(z)')) +
         geom_area() +
         geom_area(aes('x+width', alpha='z')) +
         geom_area(aes('x+2*width', linetype='factor(z)'),
                   color='black', fill=None, size=2) +
         geom_area(aes('x+3*width', color='z'),
                   fill=None, size=2) +
         geom_area(aes('x+4*width', fill='factor(z)')) +
         geom_area(aes('x+5*width', size='z'),
                   color='black', fill=None) +
         scale_x_continuous(
             breaks=[i*2*np.pi for i in range(7)],
             labels=['0'] + ['${}\pi$'.format(2*i) for i in range(1, 7)])
         )

    assert p == 'area_aesthetics'
