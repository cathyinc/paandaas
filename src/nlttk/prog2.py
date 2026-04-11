def display2():
    code = '''def cel_to_ft(celsius):
    return(celsius*1.8)+32
celsius=float(input("Enter temp in C:"))
farenheit=cel_to_ft(celsius)
if farenheit<32:
    print(f"{celsius}Celsius equivalent to {farenheit:.2f} and Farenheit is below freezing.")
else:
    print(f"{celsius}Celsius equivalent to {farenheit:.2f}and Farenheit is not below freezing.")'''
    print(code)
