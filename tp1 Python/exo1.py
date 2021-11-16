
def anneeBissextile(A):
    a_l=str(A)
    if a_l[2]!=0:
        if a_l[3]!=0:
            if A%4==0:
                return (True)
    if A%400==0:
        return (True)
    else:
        return (False)

def nombreJours(mois):
    A=int(input("annee: "))
    anneeBissextile(A)
    nbreJours=0
    if mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12:
        nbreJours+=31
        return (nbreJours)
    if mois==4 or mois==6 or mois==9 or mois==11:
        nbreJours+=30
        return (nbreJours)
    if mois==2:
        if anneeBissextile(A)==True:
            nbreJours+=29
        elif anneeBissextile==False:
            nbreJours+=28
    return (nbreJours)

def dateValide(jour,mois,annee):
    if nombreJours (mois) - jour >=0:
        return(True)
    else:
        return(False)
        
def principal(j):
    j=int(input("Jour: "))
    m=int(input("Mois: "))
    a=int(input("Année: "))
    if dateValide(j,m,a)==True:
        return ("date valide")
    else:
        return ("date non valide")
    
        

    

    
        