
#Runs test

# Usage: $python runs_test.py

# Author: Valeria Guerra de la O [A01705318]
# Date: 31/august/2022
# Class: Metodos cuantitativos y simulacion

#Import
import math

#Variables
rachas = list()
n_signos=0
t_runs=1 


#Read values from file 
file = open('runs_data.txt','r')
contents = file.readlines()
n = len(contents)

#Get rachas and runs 
before = contents[0]
for i in range(n):
    if i!=0:
        if(contents[i] >= before):
            rachas.append('+')
        else:
            rachas.append('-')
        before= contents[i]

#Get total signs
n_signos=len(rachas)

#Get total runs   
for i in range(n_signos-1):
    if (rachas[i] != rachas[i+1]):
        t_runs=t_runs+1
        
#Get Mui
mui=round(((2*n_signos)-1)/3,4)

#Get sigma
sigma2=((16*n_signos)-29)/90
sigma=round(math.sqrt(sigma2),5)

#Get zscore (numero de rachaz-mui / sigma)
zscore=round((t_runs-mui)/sigma,6)


#Output
print('Generated signs:')
print(*rachas)
print('total signs:', n_signos)
print('total runs:', t_runs)
print('Statistics')
print('Mui', mui)
print('Sigma', sigma)
print('Zscore', zscore)

print('H0: Appereance of the numbers is random')
print('H1: Appereance of the numbers is not random')


#|zsccore| > Z a/2 (is rejected)
if(abs(zscore) > zet):
    print('Since |' ,zscore, '| > |' , zet, '| H0 is rejected')
else:
    print('Since |' ,zscore, '| < |' , zet, '| H0 is not rejected')



