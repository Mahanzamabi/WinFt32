import time
import os
os.system('color 0a')
def tryagin():
    os.system('cls')
    main()
def OpenDrive():
            import os
            os.system('cls')
            DriveLatter=input('Enter Drive Latter->')
            os.system(f'start {DriveLatter}')
            os.system('cls')

def Firewall():
    while True:
        import os
        os.system('cls')
        on = 'Netsh Firewall Set Opmode Enable'
        off = 'Netsh Firewall Set Opmode Disable'
        print(''' 
        __[To do this you need to run cmd in admin mode]__
        1-Off
        2-On
        0-Back
        
        ''')
        Firewall = input('-->')
        if Firewall =='1':
            a = os.system(off)
            print('Success!')
        elif Firewall =='2':
            b= os.system(on)
            print('Success!')
        elif Firewall =='0':
            os.system('cls')
            break
def StartPowerShell():
    import os
    os.system('start Powershell')
    os.system('cls')
def SystemInfo():
    while True:
        
        print(''' 
        {========}
        {1-BIOS  }
        {2-CPU   }
        {3-RAM   }
        {0-Back  }       
        =========
        ''')
        info = input('==>')
        if info == '1':
            os.system('cls')
            print(os.system('wmic bios list full'))
        elif info=='2':
            os.system('cls')
            print(os.system('wmic cpu list full'))
        elif info =='3':
            os.system('cls')
            print(os.system('wmic Memorychip list full'))
        elif info =='0':
            os.system('cls')
            break
        

def main(): 
    import os
   
    os.system('Title WinFt')
    while True:
        print('''
        =============
        01-OpenDrive
        -------------
        02-Firewall
        -------------
        03-StartPowershell
        -------------
        04-SystemInfo
        -------------
        00-exit
        =============
        ''')
        date =input('-->')
        if date =='01':
            OpenDrive()
        elif date =='02':
            Firewall()
        elif date =='03':
            StartPowerShell()
        elif date =='04':
            SystemInfo()
        elif date =='00':
            os.system('color f')
            os.system('cls')

            exit()
        else:
            os.system('cls')
os.system('cls')
main()
os.system('cls')
tryagin()