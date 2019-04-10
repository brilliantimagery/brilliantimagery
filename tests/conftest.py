from pathlib import Path

import pytest


@pytest.fixture()
def data_folder_path():
    path = Path.cwd()

    while path.name.lower() != 'brilliantimagery':
        path = path.parent

    return path / 'tests' / 'data'
