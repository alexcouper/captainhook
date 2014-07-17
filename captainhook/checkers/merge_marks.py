# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .grep import grep

DEFAULT = 'off'


def run(files, temp_folder, arg=None):
    files = ' '.join(files)
    return grep('"^<<<<<<<\|^>>>>>>>"', files).value()
