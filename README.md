# Network-Monitor

## Dependencies-

ntfy -
Install with ``` sudo pip install ntfy ```
Note: Make sure you install ntfy as superuser

scapy -
Install with ``` pip install scapy ```

python -
Install with your package manager

## Installation -

Change ``` arp_result = scapy.arping('192.168.4.0/24') ``` with your own local gateway IP
In monitor.py

### Using ntfy with mobile device (Requires pushover mobile applicaton) -

1. download the pushover mobile application

2. create an account

3. paste ``` echo -e 'backends: ["pushover"]\npushover: {"user_key": "t0k3n"}' > ~/.ntfy.yml ``` into the terminal 
but replace 't0k3n' with personal pushover user token

For more information on how ntfy works consult the documentation
https://ntfy.readthedocs.io/en/v2.7.0/




