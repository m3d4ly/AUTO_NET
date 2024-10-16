import paramiko
from colorama import Fore
import colorama

colorama.init(autoreset=True)






	


def connect_to():
	ROUTER_IP = input(f"\n{Fore.YELLOW}Enter the router ip  {Fore.RED}-> {Fore.GREEN}")
	USERNAME =  input(f"{Fore.YELLOW}Enter your username  {Fore.RED}-> {Fore.GREEN}")
	PASSWORD =  input(f"{Fore.YELLOW}Enter your password  {Fore.RED}-> {Fore.GREEN}")
	
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=ROUTER_IP,username=USERNAME,password=PASSWORD)
	
	return ssh
	
