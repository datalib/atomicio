import os
from contextlib import contextmanager
from .core import AtomicWriter


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


@contextmanager
def atomic_write(filename, mode='w'):
    writer = AtomicWriter(filename, mode=mode)
    with writer.context() as wr:
        yield wr


def transform(filename, function, mode='w', read_mode='r'):
    touch(filename)
    with atomic_write(filename, mode) as w:
        with open(filename, mode=read_mode) as r:
            for line in function(r):
                w.write(line)
