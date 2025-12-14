import os
import time
import platform
import psutil
import keyboard

def plat():
	osms = platform.system()
	if osms == "Windows":
		vb = int(input('''\nваша система виндоус,
	для большей информации нажмите 1 или 0 для выхода, для перехода в главное меню нажмите 2:  '''))
		if vb == 1:
			print("система:", platform.system())
			print("версия системы:", platform.version())
			print("процессор:", platform.processor())
			print("архитектура:", platform.machine())
			plat()
		elif vb == 0:
			exit()
		elif vb == 2:
			print('''\nперемещение в главное меню''')
			mein()
		else:
			print('''выбери правильный номер''')
			plat()
	elif osms == "Linux":
		vb = int(input('''\nваша система линукс,
	для большей информации нажмите 1 или 0 для выхода, для перехода в главное меню нажмите 2:   '''))
		if vb == 1:
			print("система:", platform.system())
			print("версия системы:", platform.version())
			print("процессор:", platform.processor())
			print("архитектура:", platform.machine())
			plat()
		elif vb == 0:
			exit()
		elif vb == 2:
			print('''\nперемещение в главное меню''')
			mein()
		else:
			print('''выбери правильный номер''')
			plat()
	elif osms == "Darwin":
		vb = int(input('''\nваша система макОС,
	для большей информации нажмите 1 или 0 для выхода, 2 для выхода в главное меню:  '''))
		if vb == 0:
			exit()
		elif vb == 1:
			print("система:", platform.system())
			print("версия системы:", platform.version())
			print("процессор:", platform.processor())
			print("архитектура:", platform.machine())
			plat()
		elif vb == 2:
			print('''\nперемещение в главное меню''')
			mein()
		else:
			print('''выбери правильный номер''')
			plat()

def menu():
 print('''\nвыбери что нужно:
  1. - скачать все зависимости
  2. - не скачивать
  3. - выйти''')
 mens = int(input(":  "))
 if mens == 1:
  os.system('''sudo apt install sensors''')
  os.system("sudo get sensors")
  mein()
 elif mens == 2:
  print("выбрано")
  mein()
 elif mens == 3:
  exit()
 else:
  print('''выбери сущестующий номер''')
  menu()
def infomac():
	print("информация о системе:")
	os.system("system_profiler SPSoftwareDataType")
	print("версия системы:")
	os.system("sw_vers")
	mein()
def infowin():
	print("информация о системе:")
	os.system('''powershell "systeminfo | Select-String -Pattern \\"исправление\\", \\"исправления\\", \\"KB\\", \\"HotFix\\", \\"Update\\", \\"пакет\\", \\"загор\\", \\"горяч\\" -NotMatch > info.txt"''')
	os.system("powershell cat info.txt")
	os.system("powershell rm info.txt")
	mein()
def infolin():
 print("информация о системе:")
 os.system("uname -a")
 print("оперативная память:")
 os.system("free -h")
 print("диск:")
 os.system("df -h")
 print("процессор:")
 os.system('''grep "model name" /proc/cpuinfo | head -1''')
 os.system('''grep "cpu cores" /proc/cpuinfo | head -1''')
 os.system("cat /proc/cpuinfo")
 print("максимальная частота процессора:")
 os.system('''cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq''')
 print("текущая частота процессора:")
 os.system('''cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq''')
 print("температура:")
 os.system("sensors")
 print("аудио:")
 os.system("aplay -l")
 mein()
  
# quickquit
def qq():
  	osms = platform.system()
  	if osms == "Linux":
  		print("\n")
  	elif osms == "Darwin":
  		print("\n")
  	elif osms == "Windows":
  			try:
  				if keyboard.is_pressed("tab"):
  					exit()
  			except :
  					print('''ошибка, возрат в меню''')
  					mein()
 
def realtime():
	osms = platform.system()
	print('''\nизмерение в реальном времени''')
	try:
		if osms == "Windows":
			os.system("cls")
		else:
			os.system("clear")
		cpc = psutil.cpu_stats()
		nty = psutil.net_io_counters()
		opr = psutil.virtual_memory().percent
		cp = psutil.cpu_freq(percpu = True)
		cpu = psutil.cpu_percent(
		interval=0.6)
		print('''процент загруженности процессора: ''', cpu, '''\nтекущая частота процессора:''', cp, '''\nстатистика процессора:''', cpc, '''\nоперативная память: ''', opr, '''\nсеть: ''', nty)
		time.sleep(0.3)
	except PermissionError as perm:
		print(f"\nошибка прав: {perm}")
		print("\nвозращение в меню")
		mein()
	except ImportError as imp:
		print("ошибка импорта: {imp}")
		print("возращение в меню")
		mein()
	while True:
		nty = psutil.net_io_counters()
		opr = psutil.virtual_memory().percent
		cp = psutil.cpu_freq(percpu = True)
		cpu = psutil.cpu_percent(
		interval=0.6)
		qq()
		print('''процент загруженности процессора: ''', cpu, '''\nтекущая частота процессора:''', cp, '''статистика процессора:''', cpc, '''оперативная память: ''', opr, '''сеть''', nty)
		time.sleep(0.3)
	
def mein():
	osms = platform.system()
	print("\nГлавное Меню")
	print("By NYA18")
	qq()
	print('''\n1. - базовая информация\n2. - подробная информация\n3. - зависимости(linux only)\n4. - метрики в реальном времени\n5. - выход''')
	mei = int(input(":  "))
	if mei == 1:
		plat()
	elif mei == 2:
		if osms == "Windows":
			infowin()
		elif osms == "Linux":
			infolin()
		elif osms == "Darwin":
			infomac()
		else:
			print("ошибка!")
			mein()
	elif mei == 3:
		menu()
	elif mei == 4:
		qq()
		realtime()
	elif mei == 5:
		exit()
	else:
		print('''выбери существующий номер''')
		mein()
		
mein()
