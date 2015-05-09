"""
    atomicio.api
    ~~~~~~~~~~~~

    Implements the functional API over the lower
    level, more verbose class machinery.
"""

import os
from contextlib import contextmanager
from .core import AtomicWriter


def touch(fname, times=None):
    """
    Create *fname* if it doesn't exist, else modifies
    the last accessed *times* like the unix ``touch``
    utility.

    :param *fname*: Name of the file.
    :param times: The access and modified times, or
        None for the current time.
    """
    with open(fname, 'a'):
        os.utime(fname, times)


@contextmanager
def atomic_write(filename, mode='w', read_mode='r'):
    """
    Given a *filename*, yields a pair of readable and
    writable opened with *read_mode* and *write_mode*
    (respectively) file streams.

    :param filename: A string filename
    :param mode: Mode to open the writer stream with.
    :param read_mode: Mode to open the reader stream with.
    """
    touch(filename)
    writer = AtomicWriter(filename, mode=mode)
    with writer.transaction() as w:
        with open(filename, mode=read_mode) as r:
            yield r, w
