atomicio
========

Library for making atomic file writes. It is based on the principle
of providing two streams: one reader stream and a writer stream.
The reader stream is to be read and processed by the caller/user,
and the results of processing written to the writer stream.
Simple example of appending to a file:


.. code-block:: python

    >>> from atomicio.api import transform
    >>> def append_lines(stream):
    ...     for item in stream:
    ...         yield item + '\n'
    ...     yield 'hi!\n'
    ...     yield 'message\n'
    ...
    >>> transform('file.txt', append_lines)
