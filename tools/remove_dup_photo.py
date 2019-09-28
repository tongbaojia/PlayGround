"""Remove duplicated iphone photo in a folder."""

import os
imgs = os.listdir(".")
r_list = []
for i in imgs:
    if (".jpg" in i) and ("2019" in i) and i.replace(".jpg", "-1.jpg") in imgs:
        print(i)
        r_list.append(i)
print(len(r_list))

for i in r_list:
	os.remove(i)
