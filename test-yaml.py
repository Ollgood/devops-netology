import socket
import json

def main():
    with open('sites.json', 'r') as f:
        sites = json.load(f)
    print("Already stored values: ",sites)
    for site in sites.keys():
        ip = socket.gethostbyname(site)
        if sites[site] != ip:
            print("[ERROR] ",site," IP mismatch: ",sites.get(site), ip)
            sites[site]=ip
    with open('sites.json', 'w') as f:
        json.dump(sites,f)
if __name__== "__main__":
    main()