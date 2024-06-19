print("Словари")
my_dict = {"Messi": "Inter Miami", "Ronaldo": "Al Nassr", "Vinicius Jr.": "Real Madrid"}
print("Исходный словарь:", my_dict)
print("Существующее значение:", my_dict["Messi"])
print("Несуществующее значение:", my_dict.get("Haaland"))
my_dict.update({"De Bruyne": "Manchester City", "Casemiro": "Manchester United"})
a = my_dict.pop("Ronaldo")
print("Удаленное значение:", a)
print("Обновленный словарь:", my_dict)

print()
print("Множества")
my_set = {54, 1, 6, 3.5, 1, "Tomato", 6, 3.5, "Tomato"}
print("Исходное множество:", my_set)
my_set.add("Carrot")
my_set.add(550)
my_set.remove("Tomato")
print("Обновленное множество:", my_set)
