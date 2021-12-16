import sys, os
print(os.path.join(os.path.abspath('.'), "utils/box/ext/rbbox_overlap_cpu"))
sys.path.append(
    os.path.join(os.path.abspath('.'), "utils/box/ext/rbbox_overlap_gpu"))

from pprint import pprint
pprint(sys.path)

from rbbox_overlap import rbbox_overlaps as rbbox_iou
from rbbox_overlap import rotate_gpu_nms as rbbox_nms