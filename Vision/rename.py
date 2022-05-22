import os


path = "./training_set/Y"
for i, filename in enumerate(os.listdir(path)):
    os.rename(path+"/"+filename, path+"/"+'Y_'+str(i)+'.jpg')
