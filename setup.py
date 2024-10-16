from fonctions import *
import time
import colorama
from colorama import Fore, Style
from banner import *




colorama.init(autoreset=True)






def config_dhcp():
    conf_type = "DHCP"
    conf_name = "     DHCP    "
        
    choice	= config_setup(conf_name,conf_type)

    if choice	== 1:
        conf_dhcp()
        choice1 = successful_conf(conf_name)

        if choice1 == 1:
            config_dhcp()
        else: 
            start_setup()
		 



    elif choice == 2:
        show_dhcp()        
        choice1 = successful_conf(conf_name)

        if choice == 1:
            config_dhcp()
        else: 
            start_setup()
	
			
    elif choice == 3:
        start_setup()

    else:
        choice2 = wrong_choice(conf_name)
	    
        if choice2 == 1:
                            
            config_dhcp()

        else:
            start_setup()
    			
	
	


def config_static():
	
	conf_type = "Routing Table"
	conf_name = "Static Rouote"
	

	choice = config_setup(conf_name,conf_type)
	
	if choice	== 1:
		
		conf_static()
		
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_static()
		else: 
			start_setup()
	
	elif choice == 2:
		
		show_routing()
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_static()
		else: 
			start_setup()
		
		
	elif choice == 3:
		start_setup()
		
		
		
		
	else:
		choice2 = wrong_choice(conf_name)
	    
		if choice2 == 1:
					
			config_static()

		else:
			start_setup()
	
	
	






def config_rip():
	conf_type = "Routing Table"
	conf_name = "    RIPv2    "

	
	choice = config_setup(conf_name,conf_type)
		
	if choice == 1:
	
		conf_rip()
	
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_rip()
		else: 
			start_setup()
	
	elif choice == 2:
		
		show_routing()
		
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_rip()
		else: 
			start_setup()
		
	elif choice == 3:
		start_setup()
		
		
		
		
	else:
		choice2 = wrong_choice(conf_name)
	    
		if choice2 == 1:
					
			config_rip()

		else:
			start_setup()
	
	
	
	
	
def config_ospf():
	conf_type = "Routing Table"
	conf_name = "     OSPF    "
	
	
	choice =config_setup(conf_name,conf_type)
	
	if choice	== 1:
	
		conf_ospf()
	
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_ospf()
		else: 
			start_setup()
	
	elif choice == 2:
		
		show_routing()
		
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_ospf()
		else: 
			start_setup()
		
	elif choice == 3:
		start_setup()
	
		
		
	else:
		choice2 = wrong_choice(conf_name)
	    
		if choice2 == 1:
					
			config_ospf()

		else:
			start_setup()
	
	
	
	
	
def config_vlan():
	conf_type = "VLAN"
	conf_name = "     VLAN    "


	choice = config_setup(conf_name,conf_type)
	
	if choice	== 1:
		
		conf_vlan()
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_vlan()
		else: 
			start_setup()

	elif choice == 2:
		show_vlan()
		
		
		choice1 = successful_conf(conf_name)

		if choice1 == 1:
			config_vlan()
		else: 
			start_setup()
		
	elif choice == 3:
		start_setup()
	
		
		
	else:
		choice2 = wrong_choice(conf_name)
	    
		if choice2 == 1:
					
			config_vlan()

		else:
			start_setup()	
	
	
	
	

	
	
def copy_run_from():
    
	copy_from_banner()
	conf_copy_from()
	

	
	
def copy_run_to():
	copy_to_banner()
	conf__copy_to()




def start_setup():
    		
	banner()
		
	cont_lst = ["DHCP","STATIC ROUTE","RIP","OSFF","VLAN","COPY CONFIGURATION TO","COPY CONFIGURATION FROM\n"]
	i = 1
	for l in cont_lst:
		print(f"{Fore.GREEN}[{i}]  " ,end="")
		time.sleep(0.15)
		print(f"{Fore.YELLOW}{l}")
		time.sleep(0.15)
		i += 1


	choice = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
	print(f"{Style.RESET_ALL}")

	while choice not in [1,2,3,4,5,6,7]:
		print(F"{Fore.RED}\nWRONG CHOICE!\n ")
		choice = int(input(f"{Fore.YELLOW}Enter your choice {Fore.RED}-> {Fore.GREEN}"))
		print(f"{Style.RESET_ALL}")

	if choice == 1:
		config_dhcp()
					
	elif choice == 2:
			config_static()
				

	elif choice == 3:
			
		config_rip()
					

	elif choice == 4:
		config_ospf()
			

	elif choice == 5:
		config_vlan()
			

	elif choice == 6:
		copy_run_to()
					

	elif choice == 7:
			
		copy_run_from()	

	else:
		print("wrong choice!")


start_setup()
