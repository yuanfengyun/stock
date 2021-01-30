#!/bin/bash

cd /home/test/stock/database/

python3 cash_statement.py

sleep 10s

python3 balance_sheet.py

sleep 10s

python3 income_statement.py
