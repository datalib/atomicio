import os
from contextlib import contextmanager
from .core import AtomicWriter


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


@contextmanager
def atomic_write(filename, mode='w', read_mode='r'):
    touch(filename)
    writer = AtomicWriter(filename, mode=mode)
    with writer.context() as w:
        with open(filename, mode=read_mode) as r:
            yield r, w
