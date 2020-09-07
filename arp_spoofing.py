import getopt, sys
from daemon_arp_spoofing import Daemon_arp_spoofing


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "t:vahoV", ["time="])
    except getopt.GetoptError as err:
        print(err)
        print(print_help())
        sys.exit(2)

    # options params
    time = 3000
    verbose = False
    active = False
    output = False

    for o, a in opts:
        if o in ('-t', "--time="):
            time = a
        elif o == '-v':
            verbose = True
        elif o == '-a':
            active = True
        elif o == '-o':
            output = True
        elif o == '-V':
            print(print_version())
            sys.exit()
        elif o == '-h':
            print(print_logo())
            print(print_help())
            sys.exit()

    d = Daemon_arp_spoofing(time=time, verbose=verbose, active=active, output=output)
    d.run()

def print_logo():
    return """
 $$$$$$\                                                                       $$$$$$\  $$\                     
$$  __$$\                                                                     $$  __$$\ \__|                    
$$ /  $$ | $$$$$$\   $$$$$$\           $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$ /  \__|$$\ $$$$$$$\   $$$$$$\  
$$$$$$$$ |$$  __$$\ $$  __$$\         $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$$$\     $$ |$$  __$$\ $$  __$$\ 
$$  __$$ |$$ |  \__|$$ /  $$ |        \$$$$$$\  $$ /  $$ |$$ /  $$ |$$ /  $$ |$$  _|    $$ |$$ |  $$ |$$ /  $$ |
$$ |  $$ |$$ |      $$ |  $$ |         \____$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |      $$$$$$$  |        $$$$$$$  |$$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |      $$ |$$ |  $$ |\$$$$$$$ |
\__|  \__|\__|      $$  ____/ $$$$$$\ \_______/ $$  ____/  \______/  \______/ \__|      \__|\__|  \__| \____$$ |
                    $$ |      \______|          $$ |                                                  $$\   $$ |
                    $$ |                        $$ |                                                  \$$$$$$  |
                    \__|                        \__|                                                   \______/ 
_________________________________________________________________________________________________________________
    """

def print_help():
    return """   
    Syntax : apr_spoofing.py [options]
    
    Options : 
    --------
    
    -t, --time=     time before checking again arp table (default 3000 ms)
    -v              Verbose mode (default none)
    -a              Active analysis. Check in continue to avoid false positive (default none)
    -V              Print the version of the software and exit
    """

def print_version():
    return """
    arp_spoofing. Python. GNU License. V 0.0.1. 2020-09
    """

if __name__ == "__main__" :
    main()
