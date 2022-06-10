
import os
import subprocess

f = open("log.txt", "r")
s = open("sweep.txt", "w")
for line in f:

    split_line = line.strip().split(":")
    if len(split_line) < 6:
        continue

    oui = split_line[0] + split_line[1] + split_line[2]
    oui_split = oui.split(" ")
    if oui_split[0] == "(<ARPing":
        continue


    final_oui = subprocess.run(["grep", oui_split[0], "-i", "/usr/share/nmap/nmap-mac-prefixes"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    split_final_oui = final_oui.split(" ")
    s.write(line.strip('\n') + " " + str(split_final_oui[1]).strip('\n') + "\n")


f.close()
s.close()




