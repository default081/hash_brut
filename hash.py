import hashlib

def md5_brut(hash, pwfile):
	try:
		descript = open(pwfile, "r", encoding='utf-8', errors='ignore')
	except:
		print("Словарь не сушествует или файл не найден!")
		exit()
		

	for password in descript:
		fileemd5 = hashlib.md5(password.encode().strip()).hexdigest()
					
		if (hash == fileemd5):
			print("\n Бинго. \n Пароль => %s" % password)
			break
		else:
			pass

hash = input("-> Введите хешь: ")
pwfile = input("-> Введите путь до словаря: ")

md5_brut(hash, pwfile)




