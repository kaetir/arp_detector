import argparse
from time import time, sleep
from datetime import date, datetime
from subprocess import getoutput
from syslog import syslog


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-V", "--version", help="print version", action="store_true")
    parser.add_argument("-t", "--time", help="time between checks of arp table (default 3000 ms)", type=int, default=3000)
    parser.add_argument("-o", "--output", help="output changes in syslog",  action="store_true")
    args = parser.parse_args()

    if args.version:
        print("""arp_spoofing. Python. GNU License. V 0.1.0. 2020-09""")
        exit()

    # options params
    time = args.time
    verbose = args.verbose
    output = args.output

    if not verbose and not output:
        print("choose output or verbose please (or both)")
        exit()

    if verbose:
        print(print_logo())
    
    run(t=time, verbose=verbose, output=output)

def print_logo():
    return """
     #                           #####                                             
   # #   #####  #####          #     # #####   ####   ####  ###### # #    #  ####  
  #   #  #    # #    #         #       #    # #    # #    # #      # ##   # #    # 
 #     # #    # #    #          #####  #    # #    # #    # #####  # # #  # #      
 ####### #####  #####                # #####  #    # #    # #      # #  # # #  ### 
 #     # #   #  #              #     # #      #    # #    # #      # #   ## #    # 
 #     # #    # #               #####  #       ####   ####  #      # #    #  ####  
                       #######                                                     
"""

def run(t=3000, verbose=False, output=False):
    if verbose:
        print("Start analysis : "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    arp_table_start = getoutput("arp -n")

    while True:
        t1 = time()
        d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arp_t = getoutput("arp -n")

        if arp_t != arp_table_start:
            arp_table_start = arp_t
            if output:
                syslog("Arp table changed " + d1)
            if verbose:
                print("==> Arp table changed " + d1)

        if (time() - t1) < t:
            # sleep the time between the time execution and the time allowed by the user
            sleep(t - ((time() - t1) * 1000))
        # raffect t1 to calculate
        t1 = time()
        

if __name__ == "__main__" :
    main()
