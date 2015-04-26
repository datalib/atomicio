import os
import pytest
from atomicio.api import atomic_write


@pytest.fixture
def path(tmpdir):
    return tmpdir.join('something')


@pytest.mark.parametrize('exist', [True, False])
def test_atomic_write(path, exist):
    if exist:
        path.write('')

    with atomic_write(str(path)) as (r,w):
        w.write('haha')

    assert path.read() == 'haha'


@pytest.fixture
def existent_path(path):
    path.write('ha')
    return path


def test_atomic_write_with_reading(existent_path):
    with atomic_write(str(existent_path)) as (r,w):
        for item in r:
            w.write(item)
            w.write(item)
    assert existent_path.read() == 'haha'
