#!/bin/bash

cd /home/test/stock/database/

echo "python3 data_info.py"
python3 daily_price.py

sleep 3

python3 daily_zhuli_dongfang.py
