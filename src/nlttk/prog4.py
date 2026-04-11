def display4():
    code = '''import pandas as pd
df = pd.read_excel(r"Z:\\MMD Programs\\prg4.xlsx")
def mapper(data):
    mapped_data = []
    for city in data['City']:
        mapped_data.append((city,1))
    return mapped_data
def reducer(mapped_data):
    result = {}
    for city, count in mapped_data:
        if city in result:
            result[city] += count
        else:
            result[city] = count
    return result
mapped = mapper(df)
reduced = reducer(mapped)
print("Total Trips per city:")
for city,trips in reduced.items():
    print(city,":",trips)'''
    print(code)
