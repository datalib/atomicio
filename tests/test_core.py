import pytest
from atomicio.core import AtomicWriter


@pytest.fixture
def atomic_writer(tmpdir):
    fileobj = tmpdir.join('test')
    fileobj.write('ha')
    return AtomicWriter(str(fileobj), mode='r')


def test_get_streams(atomic_writer):
    reader, writer = atomic_writer.get_streams()
    assert reader.read() == 'ha'
    assert 'w' in writer.mode


def test_context_peaceful(atomic_writer):
    with atomic_writer.context() as (r,w):
        for item in r:
            w.write(item)
            w.write(item)

    assert open(atomic_writer.path).read() == 'haha'
    assert r.closed
    assert w.closed


def test_context_with_exception(atomic_writer):
    with pytest.raises(ValueError):
        with atomic_writer.context() as (r,w):
            for item in r:
                w.write(item)
                raise ValueError

    assert open(atomic_writer.path).read() == 'ha'
    assert r.closed
    assert w.closed
