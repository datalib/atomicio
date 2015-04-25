import os
from contextlib import contextmanager
from tempfile import NamedTemporaryFile


class AtomicWriter(object):
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def commit(self, writer):
        os.rename(writer.name,
                  self.path)

    def rollback(self, writer):
        os.unlink(writer.name)

    def get_streams(self):
        r = open(self.path, mode=self.mode)
        w = NamedTemporaryFile(delete=False)
        return r, w

    @contextmanager
    def context(self):
        reader, writer = self.get_streams()
        try:
            yield reader, writer
            self.commit(writer)
        except:
            self.rollback(writer)
            raise
        finally:
            reader.close()
            writer.close()
