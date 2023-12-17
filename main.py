digits = ('0','1','2','3','4','5','6','7','8','9')
table = None
with open('Financials.csv', 'r') as file:
    table = file.readlines()

headers = table[0].replace(" ", "").split(",")
# print(headers)

table.pop(0)
countries = {}

for line in table:
    line = line.replace(" ","").split(",")
    print(line)
    print(line[20])
    
    # country = line[1]
    # year = line[20]
    # print(year)
    # profit = ""
    # for char in line[11]:
    #     if char in digits or char == '.':
    #         profit += char
    # profit = float(profit)
    # if country in countries:
    #     # print(country, "exists.")
    #     if year in countries[country]:
    #         countries[country][year] += profit
    #     else:
    #         countries[country][year] = 0
    #         countries[country][year] += profit
    # else:
    #     countries[country] = {}
    #     countries[country][year] = 0
    #     countries[country][year] += profit

# print(countries)       