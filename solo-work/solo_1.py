# zadanie 1.1
hello = "Hello"
student = "Ola"
# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("{} {}".format(hello,student))

# zadanie 1.2
student = input("Wpisz swoje imie: ")
print("Hello "+student)

# zadanie 1.3 - policz liczbe studentow w tablicy studenci 
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci 
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: ", liczba_studentow)

# zadanie 1.4 - za pomoca petli i print przywitaj sie z kazdym studentem z tabeli studenci osobno
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
for x in range(liczba_studentow):
    print("Hello "+studenci[x])

# zadanie 1.5

liczba = 3
potega = 4

wynik = pow(liczba,potega)

print("Wynik wynosi: ",wynik)