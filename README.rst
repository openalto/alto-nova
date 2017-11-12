CLI Wrapper of NOVA Network Abstraction Tool
============================================

A CLI Wrapper of NOVA for Unicorn Resource Query Response.

Require Python 3.

Dependencies:

* PuLP

Installation:

.. code-block:: bash

    $ python3 setup.py install

Quickly try it without install:

.. code-block:: bash

    $ pip3 install -r requirements.txt
    $ PYTHONPATH=. bin/nova '{"anes": [{"availbw": 3}, {"availbw": 7}, {"availbw": 3}], "ane-matrix": [[{"flow-id": "0"}, {"flow-id": "1"}], [{"flow-id": "1"}, {"flow-id": "2"}], [{"flow-id": "2"}]]}'
    {"anes": [{"availbw": 3}, {"availbw": 3}], "ane-matrix": [[{"flow-id": "0"}, {"flow-id": "1"}], [{"flow-id": "2"}]]}
