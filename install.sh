#!/bin/bash

echo 'Installing YandexDiskSync ...'

python -m venv .venv

source .venv/bin/activate

pip install yadisk
pip install requests

read -p "Enter your OAuth-Token: " token

echo $token > .TOKEN

echo 'YandexDiskSync successfully installed!'

