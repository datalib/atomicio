import os
import pytest
from atomicio.core import AtomicWriter


@pytest.fixture
def atomic_writer(tmpdir):
    fileobj = tmpdir.join('test')
    fileobj.write('ha')
    return AtomicWriter(str(fileobj), mode='w')


def test_get_stream(atomic_writer):
    with atomic_writer.get_stream() as writer:
        ctx = [writer]
        assert writer.name
        assert not writer.closed

    writer = ctx[0]
    assert writer.closed


def test_context_peaceful(atomic_writer):
    with atomic_writer.transaction() as w:
        w.write('haha')

    assert open(atomic_writer.path).read() == 'haha'
    assert not os.path.exists(w.name)


def test_context_with_exception(atomic_writer):
    with pytest.raises(ValueError):
        with atomic_writer.transaction() as w:
            w.write('haha')
            raise ValueError

    assert open(atomic_writer.path).read() == 'ha'
    assert not os.path.exists(w.name)
