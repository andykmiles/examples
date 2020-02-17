#!/bin/bash

# Useful tip to clear env
pip freeze > requirements.del
pip uninstall -y -r requirements.del

# git tip
git add -A && git commit -m "change this every time" && git push origin master

# tracing
python -m trace --trace script.py

