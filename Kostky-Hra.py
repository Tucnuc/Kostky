import time
import random

# Listy
loc = []
hozenaCisla = []
postupka  = [1,2,3,4,5,6]
pi = set()
dvojice = set()

# Proměnné počtu bodů
mainPoints = 0
secondaryPoints = 0

# Textové funkce
def postText(text, zpozdeni=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
    print()
def postText2(text, zpozdeni=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
def postInput(prompt, zpozdeni=0.05):
    postText2(prompt, zpozdeni)
    user_input = input()
    return user_input

# Funkce na kontrolováni počtu stejných čísel
def pocetCisel(gamma, delta, points):   # gamma - jaké číslo hledáme, delta - kolik jich hledáme, points - body
    global mainPoints
    global hozenaCisla
    if hozenaCisla.count(gamma) == delta:
        for _ in range(delta):
            hozenaCisla.remove(gamma)
        mainPoints += points
        return True
    else:
        return False
def secondaryPocet(fi, ro, points2):    # Úplně to samé jak předchozí funkce, jen trochu poupravená, aby správně fungovalo sčítání zbylých bodů
    global mainPoints
    global hozenaCisla
    count_fi = hozenaCisla.count(fi)
    if count_fi >= ro:
        for _ in range(ro):
            hozenaCisla.remove(fi)
        mainPoints += points2 * ro
        return True
    else:
        return False


postText("\033[1mVítejte!\033[0m")
time.sleep(0.8)
postText("Děkujeme za zakoupení naší kostkové hry.")
time.sleep(0.8)
postText("Doufáme, že si ji užijete a přejeme vám \033[1mhodně štěstí\033[0m ve vašich budoucích hodech.")
time.sleep(1)
print("")
startInput1 = postInput("Nejdříve vyberte, kolik chcete hráčů \033[1m[1 - ∞]\033[0m: ")
time.sleep(0.8)
print("")
postText(" ̶̰̮̾͆̕ ̶̢͇̣́͌ ̸͉̖̲̻̩̟̙͖͊E̴̛̛͚̼͓̔̍̎̏͗͘r̵̟̼͎͆̊̆͂̽r̷̗̓̏̏̓̄o̴̠̔̒͂̕r̴̛̬̭̯͎̳̗͊̈́̑̈́ ̴̮̭̭̤̌͘͝o̸̢̰͉͎̹͖̞̓̉͑̋̇͜c̵̱͇̳̻̪̿́̌͋c̵̢̛̤̠͔͇͕͕̍̓̓͝͝ự̴͕͔̰̪̫̝́͑̀̾͠ṛ̴͚̖͓̭̱̿͌̎̈́ͅe̴̢̮̞̞͔̔͌̀d̵̝̤̃́̒̐͆ ̴̨͎̹̪͉̲̗̹̿́̍̔̊̎̚͠ ̷̨̝̬̩̤͋͐̍̽ ̸̧͎͇̳̍̈͜ͅ",0.015)
time.sleep(1)
print("")
postText2("Nyní začneme hru pro")
time.sleep(0.5)
postText2(" . . . ")
time.sleep(0.5)
postText("1 hráče.")
time.sleep(1)
print("")
loc.append("hod")

# Házecí proces
if "hod" in loc:
    postText("Je čas házet kostkami.")
    time.sleep(0.8)
    check = postInput("Zmáčkněte Enter pro hození kostek: ")
    if check.strip() == "":
        time.sleep(0.2)
        print("")
        loc.remove("hod")
        loc.append("magic")
    else:
        postText2("Na shledanou.")
        loc.remove("hod")

# Procesy sčítání bodů
if "magic" in loc:

    # Dramatický text
    for _ in range(6):
        cislo = random.randint(1,6)
        hozenaCisla.append(cislo)
    postText2("Vezmeš kostky. ")
    time.sleep(0.8)
    postText2("Napřáhneš se a hodíš. ")
    time.sleep(0.8)
    postText2("Po bližším prozkoumání si zjistil že")
    time.sleep(0.5)
    postText2(" . . . ")
    time.sleep(0.5)
    alfa = ', '.join(str(cislo) for cislo in hozenaCisla[:])
    postText(f"si hodil \033[1m{alfa}\033[0m.")
    time.sleep(1)
    print("")

    # Jedničky
    pocetCisel(1,6,8000)
    pocetCisel(1,5,4000)
    pocetCisel(1,4,2000)
    pocetCisel(1,3,1000)
    
    # Trojice
    pocetCisel(2,3,200)
    pocetCisel(3,3,300)
    pocetCisel(4,3,400)
    pocetCisel(5,3,500)
    pocetCisel(6,3,600)
    
    # Čtveřice
    pocetCisel(2,4,400)
    pocetCisel(3,4,600)
    pocetCisel(4,4,800)
    pocetCisel(5,4,1000)
    pocetCisel(6,4,1200)
    
    # Pětice
    pocetCisel(2,5,800)
    pocetCisel(3,5,1200)
    pocetCisel(4,5,1600)
    pocetCisel(5,5,2000)
    pocetCisel(6,5,2400)
    
    # Šestice
    pocetCisel(2,6,1600)
    pocetCisel(3,6,2400)
    pocetCisel(4,6,3200)
    pocetCisel(5,6,4000)
    pocetCisel(6,6,4800)
    
    # Tři dvojice
    for omega in hozenaCisla:
        if omega in pi:
            dvojice.add(omega)
        else:
            pi.add(omega)
    if len(dvojice) == 3:
         mainPoints += 1000
         hozenaCisla.clear()
    
    # Postupka
    if sorted(hozenaCisla) == sorted(postupka):
        mainPoints += 1500
        hozenaCisla.clear()
    
    # Přesunutí na druhé sčítání
    loc.clear()
    loc.append("secondary")

while True:

    # Sčítání zbylých čísel
    if "secondary" in loc:
        if secondaryPocet(1,1,100):
            continue
        elif secondaryPocet(5,1,50):
            continue
        break

# Toto se musí ještě vyžehlit jak stará košile ty vole
postText2("Sčítáme")
time.sleep(0.25)
postText("...",0.25)
time.sleep(0.8)
postText("Sčítání bylo úspěšně dokončeno.")
time.sleep(0.8)
print("")
postText2("Získali jste celkem")
time.sleep(0.5)
postText2(" . . . ")
time.sleep(0.8)
postText(f"\033[1m{mainPoints} bodů\033[0m.")
time.sleep(1)
postText2(f"Špatně jste hodil \033[1m{str(len(hozenaCisla))} kostek\033[0m. ")
time.sleep(0.8)
nevimUz = ', '.join(str(cislo3) for cislo3 in hozenaCisla[:])
postText(f"Zbyli na nich čísla: \033[1m{nevimUz}\033[0m")

















