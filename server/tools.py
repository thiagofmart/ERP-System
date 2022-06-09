from ._database import schemas, crud, utils
from datetime import date
import os
from string import Template
import base64

PATH_ROOT = os.path.dirname(os.path.abspath(__name__))

def convert_to_base64(path_file):
    with open(path_file, "rb") as img_file:
        bs64_string = base64.b64encode(img_file.read())
    return bs64_string.decode('utf-8')
