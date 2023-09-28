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
    # Read the current content of the file
    with open(network_config_file, 'r') as file:
        lines = file.readlines()

    found_bootproto_line = False  # Flag to track whether we found the BOOTPROTO line

    # Iterate through the lines and update BOOTPROTO if found
    for i in range(len(lines)):
        if lines[i].startswith('BOOTPROTO='):
            lines[i] = f'BOOTPROTO={new_bootproto_value}\n'
            found_bootproto_line = True  # Set the flag to indicate we found the line
            break  # Stop searching once we've updated the line

    if found_bootproto_line:
        # Append the static IP configuration at the bottom of the file
        lines.append(static_ip_config)

        # Write the modified content back to the file
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
