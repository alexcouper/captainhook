from os.path import dirname, join

test_dir = dirname(dirname(__file__))


def get_file(dummy_file):
    return join(test_dir, 'files', dummy_file)
