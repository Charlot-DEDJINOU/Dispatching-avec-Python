import csv
import random

Homme_1=[]
Femme_1=[]
Homme_2=[]
Femme_2=[]
Homme_3=[]
Femme_3=[]
Homme_4=[]
Femme_4=[]
Homme_5=[]
Femme_5=[]
Homme=[]
Femme=[]


c = 1
i = 0

with open('gala.csv', 'r') as f:

    obj = csv.reader(f)

    for ligne in obj:
        i+=1
        if ligne[2] == '1' and ligne[3] == 'M' and ligne not in Homme_1:
            Homme_1.append(ligne)
        elif ligne[2] == '1' and ligne[3] == 'F' and ligne not in Femme_1 :
            Femme_1.append(ligne)
        elif ligne[2] == '2' and ligne[3] == 'M' and ligne not in Homme_2:
            Homme_2.append(ligne)
        elif ligne[2] == '2' and ligne[3] == 'F' and ligne not in Femme_2 :
            Femme_2.append(ligne)
        elif ligne[2] == '3' and ligne[3] == 'M' and ligne not in Homme_3:
            Homme_3.append(ligne)
        elif ligne[2] == '3' and ligne[3] == 'F' and ligne not in Femme_3:
            Femme_3.append(ligne)
        elif ligne[2] == '4' and ligne[3] == 'M' and ligne not in Homme_4:
            Homme_4.append(ligne)
        elif ligne[2] == '4' and ligne[3] == 'F' and ligne not in Femme_4:
            Femme_4.append(ligne)
        elif ligne[2] == '5' and ligne[3] == 'M' and ligne not in Homme_5:
            Homme_5.append(ligne)
        elif ligne[2] == '5' and ligne[3] == 'F' and ligne not in Femme_5:
            Femme_5.append(ligne)
        
        if ligne[3] == 'M' and ligne not in Homme :
            Homme.append(ligne)
        if ligne[3] == 'F' and ligne not in Femme :
            Femme.append(ligne)

        

    fichier = open("gala.txt", "a")
    print(len(Homme)+len(Femme))
    
   

    for i in range(1,28) :
        groupe=[]
        num=0

        if Homme_1 :
            ligne=random.choice(Homme_1)
            groupe.append(ligne)
            Homme_1.remove(ligne)
            Homme.remove(ligne)
        if Homme_2 :
            ligne=random.choice(Homme_2)
            groupe.append(ligne)
            Homme_2.remove(ligne)
            Homme.remove(ligne)
        if Homme_3 :
            ligne=random.choice(Homme_3)
            groupe.append(ligne)
            Homme_3.remove(ligne)
            Homme.remove(ligne)
        if Homme_4 :
            ligne=random.choice(Homme_4)
            groupe.append(ligne)
            Homme_4.remove(ligne)
            Homme.remove(ligne)
        if Homme_5 :
            ligne=random.choice(Homme_5)
            groupe.append(ligne)
            Homme_5.remove(ligne)
            Homme.remove(ligne)
        if Femme_3 :
            ligne=random.choice(Femme_3)
            groupe.append(ligne)
            Femme_3.remove(ligne)
            Femme.remove(ligne)
        if Femme_4 :
            ligne=random.choice(Femme_4)
            groupe.append(ligne)
            Femme_4.remove(ligne)
            Femme.remove(ligne)
        if Femme_5 :
            ligne=random.choice(Femme_5)
            groupe.append(ligne)
            Femme_5.remove(ligne)
            Femme.remove(ligne)

        if len(groupe) < 8 :
            for j in range(len(groupe),8) :
                if j % 2 == 0 and Femme :
                    ligne=random.choice(Femme)
                    groupe.append(ligne)
                    Femme.remove(ligne)
                    if ligne in Femme_1 :
                        Femme_1.remove(ligne)
                    elif ligne in Femme_2 :
                        Femme_2.remove(ligne)
                    elif ligne in Femme_3 :
                        Femme_3.remove(ligne)
                    elif ligne in Femme_4 :
                        Femme_4.remove(ligne)
                    elif ligne in Femme_5 :
                        Femme_5.remove(ligne)

                elif Homme :
                    ligne=random.choice(Homme)
                    groupe.append(ligne)
                    Homme.remove(ligne)
                    if ligne in Homme_1 :
                        Homme_1.remove(ligne)
                    elif ligne in Homme_2 :
                        Homme_2.remove(ligne)
                    elif ligne in Homme_3 :
                        Homme_3.remove(ligne)
                    elif ligne in Homme_4 :
                        Homme_4.remove(ligne)
                    elif ligne in Homme_5 :
                        Homme_5.remove(ligne)
    
        j=0
        name_groupe="Groupe "+str(i)+"\n"
        fichier.write(name_groupe)
        for ligne in groupe :
            j+=1
            texte=str(j)+"-"+ligne[0]+" "+ligne[1]+"\n"
            fichier.write(texte) 
        fichier.write("\n")

    fichier.close()
    print(Homme)
    print(Femme)
        
        


