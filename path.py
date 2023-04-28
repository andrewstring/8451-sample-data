import pathlib

def abs_path(relative):
    return str(pathlib.Path().resolve()) + relative