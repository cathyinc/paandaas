def display1():
    code = '''def with_conc(item,lst):
    return lst +[item]
def without_conc(item,lst):
    return [lst,item]
print(with_conc(3,[1,2]))
print(without_conc(3,[1,2]))'''
    print(code)
