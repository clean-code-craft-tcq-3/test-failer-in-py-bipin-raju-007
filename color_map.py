from color_map_in_string import *

major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


def get_num_of_color_mappings():
    return len(major_colors) * len(minor_colors)


def get_color_map():
    color_map = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map = color_map + f'{i * 5 + j + 1} | {major} | {minor}' + "\n"
    return color_map
