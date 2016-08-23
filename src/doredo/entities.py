from pyglet import graphics
import pyglet.gl as gl


class Entity(object):

    dynamic = False

    def __init__(self, verts, x=0., y=0., color=(255, 255, 255)):
        self.verts = verts
        self.color = color
        self.x = x
        self.y = y
        self._vertex_list = None

    @property
    def dynamic(self):
        return False

    @property
    def vertex_list(self):
        if type(self._vertex_list) != type(None):
            return self._vertex_list
        else:
            n_verts = int(len(self.verts) / 2)
            update_mode = 'dynamic' if self.dynamic else 'static'
            self._vertex_list = graphics.vertex_list(3, #int(n_verts),
                                                     ('v2f/{}'.format(update_mode), self.verts),
                                                     ('c3B', self.color * n_verts)
                                                     )
            return self._vertex_list


    def draw(self, mode=gl.GL_TRIANGLES):
        self.vertex_list.draw(mode=mode)


    def update(self, dt):
        pass

class AnimatedEntity(Entity):

    dynamic = True

    def __init__(self, *args, anim_fun=None, anim_args=tuple(), **kwargs):
        super(AnimatedEntity, self).__init__(*args, **kwargs)
        self.anim_fun = anim_fun
        self.anim_args = tuple(anim_args)


    def update(self, dt):
        super(AnimatedEntity, self).update(dt)
        if self.anim_fun:
            self.vertex_list.vertices[:] = self.anim_fun(self.vertex_list.vertices, *self.anim_args)




