atomicio
========

Library for making atomic file writes. It is based on the principle
of providing two streams: one reader stream and a writer stream.
The reader stream is to be read and processed by the caller/user,
and the results of processing written to the writer stream.
Simple example of replacing a file's contents:


.. code-block:: python

    from atomicio.api import transform

    def func(r):
        for line in r:
            yield process(line)

    transform('filename.txt', func)
