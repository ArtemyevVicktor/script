# -*- encoding: utf-8 -*-
#author: Artemyev Viktor
#date:11.05.2017
 
import os
import re

path = "C:\\temp\\" #Рабочая папка

def get_file_list():
#Получение списка файлов
 files = os.listdir(path)
 # for file in files:	
 return files

def remove_spaces(string):
 #Удаление пробелов из строки
 l = string.split() #Разбиваем строку на слова по пробелу
 string_spaces_remove = ''
 for i in l:
  string_spaces_remove += i + '_'
 string_spaces_remove = string_spaces_remove[:-1]
 return string_spaces_remove
 
#Переименование файла
def rename_file(file_name, new_file_name):
 i=1
 while i>-1:
    try:
        if i==1:
         os.rename(path+file_name,path+remove_spaces(new_file_name)+'.html')
        else:
         os.rename(path+file_name,path+remove_spaces(new_file_name)+"("+str(i)+")"+'.html')
    except:
        i=i+1
    else:
	    break		
def find_feature(file_name, type=1):
 #поиск строки признака в заданномом файле
 #1 Счёт
 #2 СЧЕТ-ФАКТУРА
 #3 ДЕТАЛИЗАЦИЯ СПУС
 #4 ЮЛ Акт сверки
 #5 Детализация МТР (без НДС)
 #6 Приложение к счету
 #7 АКТ сверки расчетов за оказанные услуги
 
 text_file = open(file_name,"r", encoding="utf-8")
 data = text_file.read()
 text_file.close()
 data = re.sub(r'(\<(/?[^>]+)>)', '', data) #убираем html
 
#1 Счёт
 if type == 1:
		result = data.find(r'Счет №')
		# print ( data[result:result+74].replace('\n', ' ').replace(r'Абонент:','') )
		return data[result:result+74].replace('\n', ' ').replace(r'Абонент:','')
#2 СЧЕТ-ФАКТУРА
 if type == 2:
		result = data.find(r'СЧЕТ-ФАКТУРА N')
		# print ( data[result:result+51] )
		return data[result:result+51].replace('/', '')
#3 ДЕТАЛИЗАЦИЯ СПУС
 if type == 3:
		result = data.find(r'СПУС исходящие соединения')
		# print ( "Детализация "+data[result:result+45] )
		return data[result:result+45].replace('\n', '')
#4 ЮЛ Акт сверки
 if type == 4:
		result = data.find(r'выполненных работ (оказанных услуг)')
		# print ( data[result-3:result+89].replace('\n', ' ') )
		return data[result-3:result+89].replace('\n', ' ')
#5 Детализация МТР (без НДС)
 if type == 5:
		result = data.find(r'Детализация МТР за ')
		# print ( data[result:result+52].replace('\n', ' ').replace(r':','').replace('/', '') )
		return data[result:result+52].replace('\n', ' ').replace(r':','').replace('/', '')
#6 Приложение к счету
 if type == 6:
		result = data.find(r'Приложение к счету № 654')
		# print ( data[result:result+64] )
		return data[result:result+64].replace('\n', ' ')
#7 АКТ сверки расчетов за оказанные услуги
 if type == 7:
		result = data.find(r'сверки расчетов за оказанные услуги')
		# print ( data[result-3:result+113].replace('\n', ' ').replace('№', '') )
		return data[result-3:result+113].replace('\n', '').replace('№', '').replace(r':','')
		
def find_document_and_rename():
	a=1
	name_file = get_file_list()
	while a<=7:
		i=0
		while i<len(name_file):
			resault = find_feature (path+name_file[i], a)
			if len(resault) > 2:
				rename_file(name_file[i], "ПАО Ростелеком "+resault) 
				print ( resault, len(resault) )
				del name_file[i] # удаляем уже найденный и переименованный файл из списка
			i=i+1
		a=a+1

find_document_and_rename()