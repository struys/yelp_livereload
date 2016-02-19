import os


def get_port():
    LIVERELOAD_DEFAULT_PORT = 35729
    return os.environ.get('LIVERELOAD_PORT', LIVERELOAD_DEFAULT_PORT)
