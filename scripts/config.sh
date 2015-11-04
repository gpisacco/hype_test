#!/bin/bash

# this files only pull the lastest version
cd /var/data/hype
git pull
/bin/bash /var/data/hype/scripts/install.sh
