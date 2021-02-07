cat 12.txt | tr '{}' '\n' | grep -v red | tr -Cs '0-9-' '+' | sed 's/+$//' | sed 's/^+//' > tmp.txt
echo 'with open("tmp.txt", "r") as f:
    line = f.read() 
    print(eval(line))' > 12.py
python 12.py
rm 12.py
rm tmp.txt
