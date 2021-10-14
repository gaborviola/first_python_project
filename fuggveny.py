def hello_funcions():
    print("Hello Functions!")

def add_params(param1, param2):
    return param1+param2

def number_of_spaces(text):
    result=0
    for c in text:
        if c==" ":
            result += 1
    return result

def average(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum += i
    return sum/len(list_of_numbers)

def magangangzo_szam(text):
    count=0
    maganhangzok = "aAáÁeEéÉiIíÍoOöÖőŐuUúÚüÜűŰ"
    for c in text:
        if c in maganhangzok:
            count += 1
    return count


hello_funcions()
print(add_params(1,4))
print(number_of_spaces("ez egy szoveg"))
print(average([3, 5, 1]))
print(magangangzo_szam("Árvíztűrő"))
