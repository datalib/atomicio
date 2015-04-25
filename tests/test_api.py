import os
import pytest
from atomicio.api import atomic_write, transform


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


def test_atomic_write_with_reading(path):
    path.write('ha')

    with atomic_write(str(path)) as (r,w):
        for item in r:
            w.write(item)
            w.write(item)

    assert path.read() == 'haha'


def test_transform(path):
    path.write('ha')

    def func(r):
        for item in r:
            yield item
            yield item

    transform(str(path), func)
    assert path.read() == 'haha'
