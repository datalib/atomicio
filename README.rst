atomicio
========

.. image:: https://travis-ci.org/datalib/atomicio.svg?branch=master
    :target: https://travis-ci.org/datalib/atomicio

A library for making atomic file writes. Basically it guarantees
that the data is not partially written to the file (hence corrupting
it in case an exception is raised) by writing to a temporary file
that gets renamed and deleted after writing.

.. code-block:: python

    from atomicio.api import atomic_write
    with atomic_write(path) as (r,w):
        for item in r:
            w.write(process(item))

There are many other libraries that provide this functionality in
Python. This library's approach and API is inspired by `fatomic`_
and `python-atomicwrites`_ respectively.


.. _fatomic: https://github.com/abarnert/fatomic
.. _python-atomicwrites: https://github.com/untitaker/python-atomicwrites
