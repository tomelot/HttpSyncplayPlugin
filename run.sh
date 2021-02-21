#!/bin/bash
python3 syncplay/syncplayClient.py --no-gui -n Server -a syncplay.pl:8999 -r 8 --player-path http://127.0.0.1:5000/data
