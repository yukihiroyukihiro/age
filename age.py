driving = input('請問你有沒有開過車(Y/N)：')
if driving != 'Y' and driving != 'N' and driving != 'y' and driving != 'n':
	print('只能輸入Y or N, 程式即將離開.')
	raise SystemExit


age = (input('請輸入你的年紀：'))
#print(age.isdigit()) #判斷age是否為數字
if age.isdigit() != True:
	print('只能輸入整數數字, 程式即將離開.')
	raise SystemExit


age = int(age)
if driving == 'Y' or driving == 'y':
	if age >= 18:
		print('你超過18歲，有通過駕照考試')
	else:
		print('奇怪！你怎麼開過車！')
elif driving == 'N' or driving == 'n':
	if age >= 18:
		print('你可以去考駕照了！')
	else:
		print('你沒有開過車，等你滿18歲就可以去考了！')