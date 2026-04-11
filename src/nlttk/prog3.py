def display3():
    code = '''import pandas as pd
df= pd.read_excel(r"Z:\\MMD Programs\\prg3.xlsx")
def mapper(data):
    mapped_data =[]
    for age in data['Age']:
        if not pd.isna(age):
            mapped_data.append((age,1))
    return mapped_data
def reducer(mapped_data):
    total_age =0
    count =0
    for age, c in mapped_data:
        total_age += age
        count += c
    return total_age/count

mapped = mapper(df)
average_age=reducer(mapped)

print("Average Age of Titanic Passengers:",round(average_age,2))'''
    print(code)
