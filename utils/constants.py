from utils.Singleton import Singleton


@Singleton
class Constant(object):

    IMAGE_WIDTH = 227
    IMAGE_HEIGHT = 227

    MAX_ITERATOR = 40000

    WORKSPACE = ""

    def set_workspace(self, workspace):
        self.WORKSPACE = workspace

    def get_workspace(self):
        return self.WORKSPACE