# Arp-detector

Arp table alteration detection services and script for syslog output



## Install

```bash
cd /opt
sudo git clone https://github.com/kaetir/arp_detector
cd arp_detector
sudo cp arpspoof_detect_sh.service arpspoof_detect_py.service /etc/systemd/system
```

### Enable service 

```bash
sudo systemctl enable --now arpspoof_detect_sh 
# OR
sudo systemctl enable --now arpspoof_detect_py
```

 

## Uninstall

### Disable the services 

```bash
sudo systemctl disable --now arpspoof_detect_sh 
# OR
sudo systemctl disable --now arpspoof_detect_py
```

### Then remove the files

```bash
sudo rm -rf /opt/arp_detector
sudo rm /etc/systemd/system/arpspoof_detect_*
```

