#!/bin/bash

sudo python3 monitor.py > log.txt
python3 add_mac.py
mon=$(sudo cat sweep.txt)
ntfy -t "Network Device Update" send "$mon"
