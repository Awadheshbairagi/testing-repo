import os
from random import randint 
for i in range(randint(450,535)):
    for j in range(0,randint(1,5)):
        d=str(i) +'days ago'
        with open('file.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "commit"')
os.system('git push -u origin main')