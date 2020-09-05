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

If you use NOVA, please cite the [conference paper](https://ieeexplore.ieee.org/abstract/document/7969117) using the following BibTex entry:

.. code-block:: bibtex

    @inproceedings{NOVA2017,
        author = {Kai Gao and Qiao Xiang and Xin Wang and Yang, Yang Richard and Jun Bi},
        booktitle = {2017 IEEE/ACM 25th International Symposium on Quality of Service (IWQoS)},
        doi = {10.1109/IWQoS.2017.7969117},
        isbn = {978-1-5386-2704-4},
        month = {jun},
        pages = {1--10},
        publisher = {IEEE},
        title = {NOVA: Towards on-demand equivalent network view abstraction for network optimization},
        url = {http://ieeexplore.ieee.org/document/7969117/},
        year = {2017}
    }
