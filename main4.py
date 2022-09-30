from feat.utils import get_test_data_path
from feat.plotting import imshow
import os

test_data_dir = get_test_data_path()

single_face_img_path = os.path.join(test_data_dir, "")

imshow(single_face_img_path)

