cd  data\contract

echo "get contracts ..."

python contract.py
cd ..\..\
echo "get contracts success ..."

echo "get dayanglu egg price"
cd data\price
python dayanglu.py
cd ..\..\
echo "get dayanglu egg price success ..."

pause...

