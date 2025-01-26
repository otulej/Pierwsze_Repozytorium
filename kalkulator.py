print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")
opcja = input("Wybierz operacje: ")

if opcja not in ('1', '2', '3', '4'):
	print("Podano zla opcje")
else:
	x = float(input("Podaj pierwsza liczbe: "))
	y = float(input("Podaj druga liczbe: "))

	print("Wynik:")

	match opcja:
		case "1":
			print(x+y)
		case "2":
			print(x-y)
		case "3":
			print(x*y)
		case "4":
			print(x/y)
