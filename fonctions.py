from auto_connect import *
import time
import sys
import os
import platform
from banner import *
import platform
from scp import SCPClient 

	
	
def successful_conf(conf_name):
    conf_name1 = conf_name.strip()
	
    print(f"\n{Fore.GREEN}{conf_name1} configaration complited successfuly *_* \n")
    print(f"\n{Fore.GREEN}[1]  " ,end="")
    time.sleep(0.15)
    print(f"{Fore.YELLOW}Reconfigure {conf_name1}")
    time.sleep(0.2)
    print(f"{Fore.GREEN}[2]  " ,end="")
    time.sleep(0.15)
    print(f"{Fore.YELLOW}exit\n")
		
    choice1 = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
	
    while choice1 not in [1,2]:
        print(F"{Fore.RED}\nWRONG CHOICE!\n ")
        choice1 = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
        print(f"{Style.RESET_ALL}")

    return choice1
	
	



def config_setup(conf_name,conf_type):
    
    config_banner(conf_name)
    conf_name1 = conf_name.strip()
    cont_d = {"Configure":conf_name1,"Show":conf_type,"Exit":" "}
    i = 1
    
    for x,y in cont_d.items():
        print(f"\n{Fore.GREEN}[{i}]  " ,end="")
        time.sleep(0.15)
        print(f"{Fore.YELLOW}{x} {y}",end="")
        i += 1
    
    choice = int(input(f"\n{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
    return choice
	



def wrong_choice(conf_name):
    conf_name1 = conf_name.strip()
    print(F"{Fore.RED}\nWRONG CHOICE!\n ")

    print(f"{Fore.GREEN}[1]  " ,end="")
    time.sleep(0.15)
    print(f"{Fore.YELLOW}Reconfigure {conf_name1}")
    time.sleep(0.2)
    print(f"{Fore.GREEN}[2]  " ,end="")
    time.sleep(0.15)
    print(f"{Fore.YELLOW}exit\n")
		
    choice = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
	
    while choice not in [1,2]:
        print(F"{Fore.RED}\nWRONG CHOICE!\n ")
        choice = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
        print(f"{Style.RESET_ALL}")
		
    return choice







def create_f():
    cnf_dir = "conf_dir"
    if cnf_dir not in os.listdir():
        os.mkdir(cnf_dir)
        
    os.chdir(cnf_dir)
    if "Windows" not in platform.platform():
        f_name = input(f"{Fore.YELLOW}Give file name withoute space or extention  {Fore.RED}-> {Fore.GREEN}")
    else:
        f_name = input(f"{Fore.YELLOW}Give file name  with extention and withoute space {Fore.RED}-> {Fore.GREEN}")

    return f_name
    


def conf_dhcp():

    ssh_client = connect_to()
    remote_connection = ssh_client.invoke_shell()

    pool_name = input(f"\n{Fore.YELLOW}Pool name  {Fore.RED}-> {Fore.GREEN}")
    netID_and_mask = input(f"{Fore.YELLOW}netID + MASK  {Fore.RED}-> {Fore.GREEN}")
    defau_get = input(f"{Fore.YELLOW}Default Getway  {Fore.RED}-> {Fore.GREEN}")
     
    remote_connection.send("ena\n")
    time.sleep(0.7)
    remote_connection.send("config t\n")
    time.sleep(0.7)
    remote_connection.send("service dhcp\n")
    time.sleep(0.7)
    remote_connection.send(f"ip dhcp pool {pool_name}\n")
    time.sleep(0.7)
    remote_connection.send(f"network {netID_and_mask}\n")
    time.sleep(0.7)
    remote_connection.send(f"default-router {defau_get}\n")
    time.sleep(0.7)
    remote_connection.send("end\n")
    remote_connection.close()

def conf_static():
    ssh_client = connect_to()
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("ena\n")
    time.sleep(0.7)
    remote_connection.send("config t\n")
    time.sleep(0.7)
                
    N = int(input(f"{Fore.YELLOW}Enter the number of Networks {Fore.RED}-> {Fore.GREEN}"))
    
    for n in range(1,N+1):    
        Net = input(f"{Fore.YELLOW}Enter Network {n} ID + Mask {Fore.RED}-> {Fore.GREEN}")
        Next_Hope_IP = input(f"{Fore.YELLOW} Enter the Next Hope IP for Network {n}  {Fore.RED}-> {Fore.GREEN}")
        
        
        remote_connection.send(f"ip route {Net} {Next_Hope_IP}\n")
        time.sleep(0.7)
        
    remote_connection.close()
    

def conf_rip():
    ssh_client = connect_to()
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("ena\n")
    time.sleep(0.7)
    remote_connection.send("config t\n")
    time.sleep(0.7)    
    remote_connection.send("router rip\n")
    time.sleep(1)     
    remote_connection.send("verssion 2\n")
    time.sleep(1)    
       
    N = int(input(f"\n{Fore.YELLOW}Enter the number of Connected Networks {Fore.RED}-> {Fore.GREEN}"))
    
    for n in range(1,N+1):
        Net_ID = input(f"{Fore.YELLOW}Enter Network {n} ID {Fore.RED}-> {Fore.GREEN}")
        remote_connection.send(f"network {Net_ID}\n")
        time.sleep(1)
        
    remote_connection.close()

def conf_ospf():
    ssh_client = connect_to()
    remote_connection = ssh_client.invoke_shell()
    
    remote_connection.send("ena\n")
    time.sleep(0.7)
    remote_connection.send("config t\n")
    time.sleep(0.7)
    p_id = input(f"\n{Fore.YELLOW}Enter the process id {Fore.RED}-> {Fore.GREEN}")   
    remote_connection.send(f"router ospf {p_id} \n")
    time.sleep(0.7)     

    N = int(input(f"{Fore.YELLOW}Enter the number of Connected Networks {Fore.RED}-> {Fore.GREEN}"))
    
    for n in range(1,N+1):
        Net_ID_w_c_mask = input(f"{Fore.YELLOW}Enter Network {n} ID + Wildcardmask {Fore.RED}-> {Fore.GREEN}")
        remote_connection.send(f"network {Net_ID_w_c_mask} area 0 \n")
        time.sleep(0.7)
        
    remote_connection.close()


def conf_vlan():
    ssh_client = connect_to()
    remote_connection = ssh_client.invoke_shell()
    time.sleep(0.7)
    remote_connection.send(f"ena\n")    
    s_vlan = int(input(f"\n{Fore.YELLOW}Enter start vlan {Fore.RED}-> {Fore.GREEN}"))
    e_vlan = int(input(f"{Fore.YELLOW}Enter end vlan  {Fore.RED}-> {Fore.GREEN}"))
    
    for n in range (s_vlan,e_vlan + 1):
        print ("Creating VLAN {n}")
        v_name = input(f"{Fore.YELLOW}Enter VLAN Name {Fore.RED}-> {Fore.GREEN}")
        
        remote_connection.send(f"vlan {n}\n")
        remote_connection.send(f"name {v_name} \n")
        time.sleep(0.7)
    remote_connection.close()

def conf__copy_to():
    ssh_client = connect_to()
    scp = SCPClient(ssh_client.get_transport())
    
    if "Windows" not in platform.platform():
        local_file = input(f"{Fore.YELLOW}Give local file name withoute space or extention  {Fore.RED}-> {Fore.GREEN}")
        dest_file = input(f"{Fore.YELLOW}Give destianation file name withoute space or extention  {Fore.RED}-> {Fore.GREEN}")
    else:
        local_file = input(f"{Fore.YELLOW}Give local file name  with extention and withoute space {Fore.RED}-> {Fore.GREEN}")
        dest_file = input(f"{Fore.YELLOW}Give destianation file name  with extention and withoute space {Fore.RED}-> {Fore.GREEN}")
    
    scp.put(local_file,dest_file)

def conf_copy_from():
    
    
    f_name = create_f()
    ssh_client = connect_to()

    stdin, stdout, stderr = ssh_client.exec_command("show running-config \n")
    output = stdout.read().decode()
    con_w = open(f_name, "w+")
    con_w.write(output)
    ssh_client.close()
   
   



def show_dhcp():
    ssh_client = connect_to()
    stdin, stdout, stderr = ssh_client.exec_command('show ip dhcp pool')
     
    output = stdout.read().decode()
    print(f"{Fore.BLUE}{output}")
     
    ssh_client.close()

def show_routing():
    ssh_client = connect_to()
    stdin, stdout, stderr = ssh_client.exec_command("show ip route")
    
     
    output = stdout.read().decode()
    print(f"{Fore.BLUE}{output}")
     
    ssh_client.close()

def show_vlan():
    ssh_client = connect_to()
    stdin, stdout, stderr = ssh_client.exec_command("show vlan")
    
     
    output = stdout.read().decode()
    print(f"{Fore.BLUE}{output}")
     
    ssh_client.close() 
    

	    
    
