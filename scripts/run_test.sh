#!/bin/bash

#run the test scripts
cd /var/data/hype
source local/env/bin/activate
export CONFIG=../config/test.conf
py.test -v -s api/test_hype_container.py