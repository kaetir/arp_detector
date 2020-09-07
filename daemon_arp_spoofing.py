import time
from datetime import date, datetime
import subprocess
import syslog
from scapy.all import sniff, ARPHDR_ETHER, ETHER_ANY, srp, conf


class Daemon_arp_spoofing():
    """
        active = detect all the request arp coming to change the arp table
        verbose = that results are displayed on the screen
        output = write a file with logs
    """
    def __init__(self, t=3000, active=False, output=False, verbose=False):
        self.t = t
        self.active = active
        self.output = output
        self.verbose = verbose

        self.go = False

    def restart(self):
        """
        Restart the daemon
        :return: void
        """
        self.stop()
        self.start()

    def start(self):
        self.go = True
        self.run()

    def stop(self):
        self.go = False

    def run(self):
        self.go = True
        if self.verbose:
            print("Start analysis : "+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        arp_table_start = subprocess.getoutput("arp -a")

        t1 = time.time()
        d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        while 1 and self.go:

            apr_t = subprocess.getoutput("arp -a")

            if apr_t != arp_table_start:
                print("==> Arp poisoning attack detected at " + d1)
                if self.verbose:
                    syslog.syslog("Arp poisoning attack detected at " + d1)

            if (time.time() - t1) * 1000 < self.t:
                # sleep the time between the time execution and the time allowed by the user
                time.sleep(self.t - ((time.time() - t1) * 1000))
            # raffect t1 to calculate
            t1 = time.time()
            if self.output or self.verbose:
                d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
