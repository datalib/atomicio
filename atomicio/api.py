from contextlib import contextmanager
from .core import AtomicWriter, touch


@contextmanager
def atomic_write(filename, mode='r'):
    touch(filename)
    writer = AtomicWriter(filename, mode=mode)
    with writer.context() as streams:
        yield streams


def transform(filename, function, mode='r'):
    with atomic_write(filename, mode) as (r, w):
        for segment in function(r):
            w.write(segment)
