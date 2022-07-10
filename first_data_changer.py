import unicodecsv

filename = "data_2.csv"
with open(filename, "rb") as file:
    reader = unicodecsv.DictReader(file)
    data = list(reader)

for line in data:
    line["ada"] = line["Ada"]
    line["parsel"] = line["Parsel"]
    line["ada_parsel"] = line["ada"]+"/"+line["parsel"]
    del line["Ada"]
    del line["Parsel"]

ada_parsel_list = []
for line in data:
    ada_parsel_list.append(line["ada_parsel"])

set_list = set()
for line in data:
    x = line["ada_parsel"]
    set_list.add(x)

final = {}
for element in set_list:
    count = ada_parsel_list.count(element)
    final[element] = count
    #print("Ada/Parsel:", element,"Adet:",count)

for x, y in final.items():
    x_ada_parsel = x.split("/")
    x_ada = x_ada_parsel[0]
    x_parsel = x_ada_parsel[1]
    print(x_ada,x_parsel, y)

    what is the matrix ?
