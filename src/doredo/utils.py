import pyglet
import numpy as np
from . import resources
from .entities import Entity

class CumClock(pyglet.clock.Clock):

    def __init__(self, *args, **kwargs):
        super(CumClock, self).__init__(*args, **kwargs)
        self.cumtime = 0.

    def tick(self, *args, **kwargs):
        to_return = super(CumClock, self).tick(*args, **kwargs)
        self.cumtime += to_return
        return to_return

class BarClock(CumClock):

    def __init__(self, *args, bpm=120, beats=4, **kwargs):
        super(BarClock, self).__init__(*args, **kwargs)
        self._bps = bpm / 60.
        self.beats = beats

    @property
    def bpm(self):
        return self._bps * 60.

    @bpm.setter
    def bpm(self, value):
        return self._bps * 60

    @property
    def measure_len(self):
        return (1. / self._bps) * self.beats

    def tick(self, *args, **kwargs):
        """Return Percentage of Time through a measure."""
        super(BarClock, self).tick(*args, **kwargs)
        mlen = self.measure_len
        return (self.cumtime % mlen) / mlen


class BeatClock(CumClock):

    def __init__(self, *args, bpm=120, **kwargs):
        super(BeatClock, self).__init__(*args, **kwargs)
        self._bps = bpm / 60.

    @property
    def bpm(self):
        return self._bps * 60.

    @bpm.setter
    def bpm(self, value):
        return self._bps * 60

    def tick(self, *args, **kwargs):
        """Return Percentage of Time through a beat."""
        super(BeatClock, self).tick(*args, **kwargs)
        blen = 1. / self._bps
        return (self.cumtime % blen) / blen







def add_depth(verts, depth=0.):
    vv = np.array(verts, dtype=float).reshape(-1, 2)  # Make a n x 2 array of vertices
    vv = np.hstack((vv, depth * np.ones((vv.shape[0], 1))))  # Add a third column of zeros: that's its depth.
    return vv.ravel()

def gen_primitive_entity(prim_type='triangle', x=0., y=0., rot=0., scale=1., depth=0.):
    verts = getattr(resources, prim_type)
    verts = add_depth(verts, depth=depth)
    return Entity(verts=verts, x=x, y=y, rot=rot, scale=scale)



cumclock = CumClock()
pyglet.clock.schedule(cumclock.tick)