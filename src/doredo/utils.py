import pyglet
import numpy as np


class CumClock(pyglet.clock.Clock):

    def __init__(self, *args, **kwargs):
        super(CumClock, self).__init__(*args, **kwargs)
        self.cumtime = 0.

    def tick(self, *args, **kwargs):
        to_return = super(CumClock, self).tick(*args, **kwargs)
        self.cumtime += to_return
        return to_return


def add_depth(verts, depth=0.):
    vv = np.array(verts, dtype=float).reshape(-1, 2)  # Make a n x 2 array of vertices
    vv = np.hstack((vv, depth * np.ones((vv.shape[0], 1))))  # Add a third column of zeros: that's its depth.
    return vv.ravel()

cumclock = CumClock()
pyglet.clock.schedule(cumclock.tick)