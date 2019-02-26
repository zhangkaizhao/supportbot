import os.path


def get_fixture_filepath(fname):
    return os.path.join(os.path.dirname(__file__), "fixtures", fname)
