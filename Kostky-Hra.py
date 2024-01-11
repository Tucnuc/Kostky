import time
import random

loc = ["magic"]
hozenaCisla = []

def postText(text, zpozdeni=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
    print()
def postText2(text, zpozdeni=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(zpozdeni)
def postInput(prompt, zpozdeni=0.04):
    postText2(prompt, zpozdeni)
    user_input = input()
    return user_input

# postText("\033[1mVítejte!\033[0m")
# time.sleep(0.8)
# postText("Děkujeme za zakoupení naší kostkové hry.")
# time.sleep(0.8)
# postText("Doufáme, že si ji užijete a přejeme vám \033[1mhodně štěstí\033[0m ve vašich budoucích hodech.")
# time.sleep(1)
# print("")
# startInput1 = postInput("Nejdříve vyberte, kolik chcete hráčů \033[1m[1 - ∞]\033[0m: ")
# time.sleep(0.8)
# print("")
# postText(" ̶̰̮̾͆̕ ̶̢͇̣́͌ ̸͉̖̲̻̩̟̙͖͊E̴̛̛͚̼͓̔̍̎̏͗͘r̵̟̼͎͆̊̆͂̽r̷̗̓̏̏̓̄o̴̠̔̒͂̕r̴̛̬̭̯͎̳̗͊̈́̑̈́ ̴̮̭̭̤̌͘͝o̸̢̰͉͎̹͖̞̓̉͑̋̇͜c̵̱͇̳̻̪̿́̌͋c̵̢̛̤̠͔͇͕͕̍̓̓͝͝ự̴͕͔̰̪̫̝́͑̀̾͠ṛ̴͚̖͓̭̱̿͌̎̈́ͅe̴̢̮̞̞͔̔͌̀d̵̝̤̃́̒̐͆ ̴̨͎̹̪͉̲̗̹̿́̍̔̊̎̚͠ ̷̨̝̬̩̤͋͐̍̽ ̸̧͎͇̳̍̈͜ͅ",0.02)
# time.sleep(1)
# print("")
# postText2("Nyní začneme hru pro")
# time.sleep(0.5)
# postText2(" . . . ", 0.1)
# time.sleep(0.5)
# postText("1 hráče.")
# time.sleep(1)
# print("")
# loc.append("hod")

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

if "magic" in loc:
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