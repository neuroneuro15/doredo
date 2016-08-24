import pyglet

class CumClock(pyglet.clock.Clock):

    def __init__(self, *args, **kwargs):
        super(CumClock, self).__init__(*args, **kwargs)
        self.cumtime = 0.

    def tick(self, *args, **kwargs):
        to_return = super(CumClock, self).tick(*args, **kwargs)
        self.cumtime += to_return
        return to_return


cumclock = CumClock()
pyglet.clock.schedule(cumclock.tick)