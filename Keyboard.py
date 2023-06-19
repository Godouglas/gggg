Text = input("Enter a phrase: ")
Question = input("Would your like to enter a faulty key? Y/N: ")
Broken = []
while Question == "Y":
    Brokenletter = input("Enter faulty key: ")
    Broken.append(Brokenletter)
    Question = input("Would your like to enter a faulty key? Y/N: ")
if Question == "N":
    for char in Broken:
        if char in Text:
            print("false")
            break
    print(Text)
