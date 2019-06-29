=========
pypidev
=========

.. image:: https://badge.fury.io/py/pypidev.svg
    :target: https://badge.fury.io/py/pypidev

pypidev is a pypi sample

-------
install
-------

.. code-block:: sh

    ❯ pip install pypidev


-------
example
-------

.. code-block:: python

    >>> from pypidev import Hello
    >>> hello = Hello("hoge")
    >>> hello.get()
    'Hello, hoge!'


---
cli
---

.. code-block:: sh

    ❯ pypidev -n hoge
    Hello, hoge!
