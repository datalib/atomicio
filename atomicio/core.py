"""
    atomicio.core
    ~~~~~~~~~~~~~

    Implements the low level object API.
"""

import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile


class AtomicWriter(object):
    """
    Helper class for performing atomic writes.

    :param path: Path to the file.
    :param mode: Mode to open the file with.
    """

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def commit(self, writer):
        """
        Commits the changes atomically (if it
        fails then no changes are committed at
        all) by renaming the temporary file.
        """
        writer.flush()
        os.rename(writer.name,
                  self.path)

    def rollback(self, writer):
        """
        Cleans up the temporary resources.
        """
        os.unlink(writer.name)

    def get_stream(self):
        """
        Get a temporary file to use.
        """
        return NamedTemporaryFile(delete=False, mode=self.mode)

    @contextmanager
    def transaction(self):
        """
        Context manager that opens the temporary file
        and yields it to the caller. Changes are then
        committed if no exceptions are raised or else
        they are simply dropped.
        """
        with self.get_stream() as writer:
            try:
                yield writer
                self.commit(writer)
            except:
                self.rollback(writer)
                raise
