import os
import shutil
import tempfile


def before_scenario(context, scenario):
    context.test_directory = tempfile.mkdtemp()
    os.chdir(context.test_directory)


def after_scenario(context, scenario):
    shutil.rmtree(context.test_directory)
