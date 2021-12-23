from config import CATEGORY_OBC as NAMES

from .dataset import DetDataset


class OBC(DetDataset):
    def __init__(self, root, image_sets, aug=None):
        super(OBC, self).__init__(root, image_sets, NAMES, aug)
