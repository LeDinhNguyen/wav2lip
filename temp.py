import os

a = os.listdir("./data_root/main/")

for t in a:
    b = os.listdir("./data_root/main/"+t)
    for i in b:
        with open(f"./filelists/{t}.txt", "a") as f:
            f.write("data_root/"+i+"\n")