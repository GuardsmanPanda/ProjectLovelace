import csv, re
table = {}

with open('periodic_table.csv') as csvfile:
    periodic_table_reader = csv.reader(csvfile, delimiter=',')
    for t in periodic_table_reader:
        table[t[0]] = float(t[1])


def molecular_mass(chemical_formula):
    return sum(table[x[0]] * int(x[1] or '1') for x in re.findall(r'([A-Z][a-z]*)([0-9]*)', chemical_formula))