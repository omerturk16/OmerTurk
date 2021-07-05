# Fill in this file with the code from parsing JSON exercise

import json

dosya=open("ömertürk.json","r")

json_dosya=json.load(dosya)

for anahtar in json_dosya:
	if anahtar == "kimlik":
		print("Adım    : ", json_dosya[anahtar][0]["Ad"])
		print("Soyadım : ", json_dosya[anahtar][0]["Soyad"])

dosya.close()


