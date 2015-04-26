import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile


class AtomicWriter(object):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def commit(self, writer):
        writer.flush()
        os.rename(writer.name,
                  self.path)

    def rollback(self, writer):
        os.unlink(writer.name)

    def get_stream(self):
        return NamedTemporaryFile(delete=False, mode=self.mode)

    @contextmanager
    def context(self):
        with self.get_stream() as writer:
            try:
                yield writer
                self.commit(writer)
            except:
                self.rollback(writer)
                raise
