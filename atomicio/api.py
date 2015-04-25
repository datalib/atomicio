import os
import errno
from contextlib import contextmanager
from .core import AtomicWriter


def touch(fname):
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        fp = os.open(fname, flags)
    except OSError as e:
        if e.errno == errno.EEXIST:
            return
        raise


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
