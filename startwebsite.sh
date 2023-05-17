#!/bin/bash

chrome='Google Chrome'
website='http://127.0.0.1:4999/'

python3 main.py & open -a "$chrome" "$website"

