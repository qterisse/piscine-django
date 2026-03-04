#!/bin/bash

pip3 --version
if pip3 install path.py --target ./local_lib/ --upgrade --log .log ; then
    python3 ./my_program.py -m ./local_lib/
else
    echo "Install command failed; could not execute my_program.py"
fi
