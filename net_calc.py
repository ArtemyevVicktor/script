# coding: utf8
import sys

print ("(0-255).(0-255).(0-255).(0-255)")
i = 1
ip=''
while i !=5:
	print("Oktet",i)
	oktet = input('')
	while oktet == "":
		print("Oktet",i)
		oktet = input('')
	oktet = int(oktet)
	while oktet > 255 or oktet <= -1:
		print ("oktet",i,"0-255")
		oktet = int(input(''))
	if i == 4:
		ip = ip+str(oktet)
	else:
		ip = ip+str(oktet)+'.'
	i=i+1	
print (ip)
