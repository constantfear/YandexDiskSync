#!/bin/bash

line=$(cat .TOKEN)

source .venv/bin/activate
python script.py $line $2 $1 
deactivate

