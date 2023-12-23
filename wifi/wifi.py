import subprocess
data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[i][1:-1] for i in data if "All User profile" in i]

for i in profiles:
    result=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split('\n')

    result=[b.split(":")[1][1:-1] for b in result if "Key Content" in b]

    try:
        print("{:<30}|{:<}".format(i,result[0]))
    except IndexError:
        print("{:<30}|{:<}".format(i,""))    