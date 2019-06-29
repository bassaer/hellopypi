=========
pypidev
=========

.. image:: https://img.shields.io/pypi/v/pypidev.svg   :alt: PyPI

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
