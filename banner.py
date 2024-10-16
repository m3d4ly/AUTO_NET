import sys
import time
from colorama import Fore, Style
import colorama , subprocess
colorama.init(autoreset=True) 






def banner():
	
	plt = sys.platform  
	
	if plt == "win32":
		subprocess.run("cls" , shell=True)  
	else:
		subprocess.run("clear" , shell=True)  
	
	
	print(f"{Fore.GREEN}+-------------------------------------------------------------+")     
	time.sleep(0.2  )                                      
	print(f"{Fore.GREEN}|         _____ _   _ _____ _____    _   _ _____ _____        |")
	time.sleep(0.2)
	
	print(f"{Fore.GREEN}|        |  _  | | | |_   _|  _  |  | \\ | |  {Fore.YELLOW}___|_   _|       |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|        | |_| | | | | | | | | | | {Fore.YELLOW} |  \\| | |__   | |         |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|        |  _  | | | | | |{Fore.YELLOW} | | | | {Fore.YELLOW} | .   |  __|  | |         |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|        | | | | {Fore.YELLOW}|_| | {Fore.YELLOW}| | | |_| | {Fore.YELLOW} | | \\ | |___  | |         |")
	time.sleep(0.2)
	print(f"{Fore.YELLOW}|        |_| |_|_____| |_| |_____| {Fore.YELLOW} |_| \\_|____/  |_|   {Fore.GREEN}V1.0{Fore.YELLOW}  |")
	time.sleep(0.2)
	print(f"{Fore.YELLOW}|                                                             |")                                                          
	time.sleep(0.2)
	print(f"{Fore.YELLOW}|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-{Fore.GREEN}+-+-+-+-+-+|")
	time.sleep(0.2)
	print(f"{Fore.YELLOW}|     NETWORK AUTOMATIOM TOOL {Fore.GREEN} By {Fore.YELLOW}MOHAMED ALY SIDI MOHAMED{Fore.GREEN}    |")
	time.sleep(0.2)
	# print(f"{Fore.YELLOW}|                                                        {Fore.GREEN}     |        ")
	time.sleep(0.2)
	print(f"{Fore.YELLOW}|+-+-+-+-+-+{Fore.GREEN}-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|")
	time.sleep(0.2)
	print(f"")
	print(f"	")






def config_banner(conf_name):
    
	print(f"{Fore.GREEN}+---------------------------------------------{Fore.RED}----------------+")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}   WELCOME TO {Fore.GREEN}{conf_name}{Fore.YELLOW} CONFIGURATION{Fore.RED}           |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}         LOGIN REMOTLY USING {Fore.GREEN}SSHv2{Fore.YELLOW}         {Fore.RED}         |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}+----------------------{Fore.RED}---------------------------------------+\n")
    
    
    
def wait():
	ts = 0.4
		
	for i in range(45):
		print(f"{Fore.GREEN}━", end="")
		time.sleep(ts)

# wait()
    
    
    
    
    
def copy_from_banner():
	print(f"{Fore.GREEN}+---------------------------------------------{Fore.RED}----------------+")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}   COPY CONFIGURATION FROM CISCO ROUTER {Fore.RED}           |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}         LOGIN REMOTLY USING {Fore.GREEN}SSHv2{Fore.YELLOW}         {Fore.RED}         |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}+----------------------{Fore.RED}---------------------------------------+\n")        
    
    
def copy_to_banner():
	print(f"{Fore.GREEN}+---------------------------------------------{Fore.RED}----------------+")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}   COPY CONFIGURATION TO CISCO ROUTER {Fore.RED}           |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}|         {Fore.YELLOW}         LOGIN REMOTLY USING {Fore.GREEN}SSHv2{Fore.YELLOW}         {Fore.RED}         |")
	time.sleep(0.2)
	print(f"{Fore.GREEN}+----------------------{Fore.RED}---------------------------------------+\n")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#f"{banner()}"
#config_banner("     OSPF    ")



# f"{banner()}"





#f = Figlet(font='doom')
#b = open("banner.txt" , "a")

#b.write(f.renderText('AUTO  NET'))

#+-------------------------------------------------------------+




# def banner():
# 	subprocess.run("cls" , shell=True)
# 	print(f"")
# 	print(f"{Fore.GREEN}+-------------------------------------------------------------+".center(120))     
# 	time.sleep(0.2  )                                      
# 	print(f"{Fore.GREEN}|         _____ _   _ _____ _____    _   _ _____ _____        |".center(120))
# 	time.sleep(0.2)
	
# 	print(f"{Fore.GREEN}|        |  _  | | | |_   _|  _  |  | \\ | |  {Fore.YELLOW}___|_   _|       |".center(125))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}|        | |_| | | | | | | | | | | {Fore.YELLOW} |  \\| | |__   | |         |".center(125))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}|        |  _  | | | | | |{Fore.YELLOW} | | | | {Fore.YELLOW} | .   |  __|  | |         |".center(129))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}|        | | | | {Fore.YELLOW}|_| | {Fore.YELLOW}| | | |_| | {Fore.YELLOW} | | \\ | |___  | |         |".center(135))
# 	time.sleep(0.2)
# 	print(f"{Fore.YELLOW}|        |_| |_|_____| |_| |_____| {Fore.YELLOW} |_| \\_|____/  |_|   {Fore.GREEN}V1.0{Fore.YELLOW}  |".center(135))
# 	time.sleep(0.2)
# 	print(f"{Fore.YELLOW}|                                                             |".center(120))                                                          
# 	time.sleep(0.2)
# 	print(f"{Fore.YELLOW}|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-{Fore.GREEN}+-+-+-+-+-+|".center(126))
# 	time.sleep(0.2)
# 	print(f"{Fore.YELLOW}|     NETWORK AUTOMATIOM TOOL {Fore.GREEN} By {Fore.YELLOW}MOHAMED ALY SIDI MOHAMED{Fore.GREEN}    |".center(135))
# 	time.sleep(0.2)
# 	# print(f"{Fore.YELLOW}|                                                        {Fore.GREEN}     |        ")
# 	time.sleep(0.2)
# 	print(f"{Fore.YELLOW}|+-+-+-+-+-+{Fore.GREEN}-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|".center(126))
# 	time.sleep(0.2)
# 	print(f"")
# 	print(f"	")


#---------------------------------------------------


# def config_banner(conf_name):
    
# 	print(f"{Fore.GREEN}+---------------------------------------------{Fore.RED}----------------+".center(125))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}|         {Fore.YELLOW}   WELCOME TO {Fore.GREEN}{conf_name}{Fore.YELLOW} CONFIGURATION{Fore.RED}           |".center(139))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}|         {Fore.YELLOW}         LOGIN REMOTLY USING {Fore.GREEN}SSHv2{Fore.YELLOW}         {Fore.RED}         |".center(139))
# 	time.sleep(0.2)
# 	print(f"{Fore.GREEN}+----------------------{Fore.RED}---------------------------------------+\n".center(125))
    

