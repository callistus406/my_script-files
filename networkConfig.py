network_config_file = '/etc/sysconfig/network-scripts/ifcfg-enp0s3'
new_bootproto_value = 'static'
static_ip_config = '''
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=8.8.4.4
'''

try:
   
    with open(network_config_file, 'r') as file:
        lines = file.readlines()

    found_bootproto_line = False  

    for i in range(len(lines)):
        if lines[i].startswith('BOOTPROTO='):
            lines[i] = f'BOOTPROTO={new_bootproto_value}\n'
            found_bootproto_line = True 
            break  

    if found_bootproto_line:
    
        lines.append(static_ip_config)

       
        with open(network_config_file, 'w') as file:
            file.writelines(lines)

        print(f"Updated BOOTPROTO to '{new_bootproto_value}' in {network_config_file}")
        print("Appended static IP configuration to the file.")
    else:
        print("BOOTPROTO line not found in the file.")

except FileNotFoundError:
    print(f"The file {network_config_file} does not exist.")
except PermissionError:
    print(f"Permission denied. You may need superuser (root) privileges to modify this file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")