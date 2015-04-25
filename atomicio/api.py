import os
from contextlib import contextmanager
from .core import AtomicWriter


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


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
