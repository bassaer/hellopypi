=========
hellopypi
=========

hellopypi is a pypi sample

-------
install
-------

.. code-block:: text
    pip install hellopypi


-------
example
-------

.. code-block:: python
>>> from hellopypi import Hello
>>> hello = Hello("hoge")
>>> hello.get()
'Hello, hoge!'


---
CLI
---

.. code-block:: text
    ❯ hellopypi -n hoge
    Hello, hoge!
