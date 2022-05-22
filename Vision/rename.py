
import os,sys
i = 1
path = "./training_set/Y"
for filename in os.listdir(path):
    os.rename(path+"/"+filename, path+"/"+'Y_'+str(i)+'.jpg')
    i += 1
