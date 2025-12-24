import requests
import re
import os
import sys
from itertools import islice

#from datetime import datetime
counter = 0

#d8 = datetime.today().strftime("-%d-%B-%Y_%H-%M-%S")

with open("C:/Users/arch/Desktop/burp_GG/counter","rt") as temp:
    start = int(temp.read().strip())
print("startuję na lini",start)
start_copy = start




with open("C:/Users/arch/Desktop/burp_GG/GG_names","rt", encoding="utf-8", errors="replace") as INplik:
    for linia in islice(INplik, start, None):
        nr_gg = linia[:9]
        counter+=1
        if(nr_gg.startswith("\"")):
            nr_gg = nr_gg[1:]
        else:
            nr_gg=nr_gg[:-1]
       
        print(nr_gg)
        if(os.path.isfile ("C:/Users/arch/Desktop/burp_GG/profilowe/"+nr_gg)):
            continue
        obraz = requests.get("https://avatars.gg.pl/user,"+nr_gg+"/s,1000x1000")
        if(obraz.content):
            with open("C:/Users/arch/Desktop/burp_GG/profilowe/"+nr_gg+".jpeg","bw") as OUTplik:
                OUTplik.write(obraz.content)
    print("ostatnia linia to", str(start_copy+counter))
    with open("C:/Users/arch/Desktop/burp_GG/counter","wt") as konczymy:
        konczymy.write(str(counter+start_copy))
