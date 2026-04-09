def display2():
    code = '''import pandas as pd
print("<.......23BDA012........>")
file_path=r"z:\\mmd\\excelwork.xlsx"
df=pd.read_excel(file_path)
map=[]
for _,row in df.iterrows():
    year=int(row["year"])
    consumption=int(row["consumption"])
    map.append((year,consumption))
print("Mapped Output:")
print(map)
reducer={}
for year,consumption in map:
    if year in reducer:
        reducer[year]=max(reducer[year],consumption)
    else:
        reducer[year]=consumption
print("maximum consumption per year:")
for year,consumption in sorted(reducer.items()):
    print(f"year:{year},max consumption:{consumption}")'''
    print(code)
