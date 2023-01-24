import subprocess
print("*****************************************")
ip = input("Enter IP: ")
print("*****************************************")
subprocess.run(['nmap', '-sV', '-Pn', f'{ip}', '-p', '502,5900,111', '--script','vuln'])

