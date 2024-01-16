import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

primary_fur_color_list = data["Primary Fur Color"].unique()
# print(primary_fur_color_list)

color_dict = {
    "Fur Color" : primary_fur_color_list,
    "Count" : []
}

for color in primary_fur_color_list:
    if color == primary_fur_color_list[0]:
        continue
    color_dict["Count"].append((data["Primary Fur Color"] == color).sum())

print(color_dict)
color_pandas = pandas.DataFrame(color_dict)

color_pandas.to_csv("color_pandas.csv")