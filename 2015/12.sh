cat 12.txt | tr '{}' '\n' | grep -v red | tr -Cs '0-9-' '+' | sed 's/+$//' | sed 's/^+//' > tmp.txt
echo 'with open("tmp.txt", "r") as f:
    line = f.read() 
    print(eval(line))' > tmp.py
python tmp.py
rm tmp.py
rm tmp.txt

echo 'import json
with open("12.txt", "r") as f:
    data = json.load(f)
    for d in data.items():
        print(d)' > tmp.py
python tmp.py
rm tmp.py
