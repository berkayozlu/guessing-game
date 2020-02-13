import random
import time
while True:
	print ("""**************************
****SAYI TAHMIN OYUNU****
*************************""")
	sayac = 0
	gerceksayi = random.randint(1,100)
	while True:
		sayial = int(input("Sayi tahmininiz:\n"))
		print ("Kontrol ediliyor..")
		time.sleep(0.7)
		if sayial > gerceksayi:
			print("Girdiginiz sayi olan {} gizli sayidan daha buyuk.".format(sayial))
		elif sayial == gerceksayi:
			print ("Tebrikler ! dogru bildiniz gizli sayi {} idi".format(gerceksayi))
			print ("{} Denemede bildiniz!".format(sayac))
			break
		else:
			print("Girdiginiz sayi olan {} gizli sayidan daha kucuk".format(sayial))
		sayac += 1