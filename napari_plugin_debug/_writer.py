"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

from typing import Any, Dict, Optional
from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_writer():
    pass


@napari_hook_implementation
def napari_write_image():
    pass


@napari_hook_implementation
def napari_write_tracks(path: str, data: Any, meta: Dict) -> str:
    with open(path, mode='w') as f:
        for row in data:
            row = [str(elem) for elem in row]
            f.write(','.join(row) + '\n')
    return path
