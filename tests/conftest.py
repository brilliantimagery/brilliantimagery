from pathlib import Path

import pytest


@pytest.fixture()
def data_folder_path():
    path = Path.cwd()

    while 'brilliantimagery' not in path.name.lower():
        path = path.parent

    return path / 'tests' / 'data'
