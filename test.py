import socket
import json
import yaml
from pprint import pprint

def main():
    with open('sites.json', 'r') as f:
        sites = json.load(f)
    print("Already stored values in json: ",sites)
    for object in sites:
        for site in object.keys():
            ip = socket.gethostbyname(site)
            if object[site] != ip:
                print("[ERROR IN JSON] ",site," IP mismatch: ",object.get(site), ip)
                object[site]=ip
        with open('sites.json', 'w') as f:
            json.dump(sites,f)

    with open('sites.yaml') as f:
        y_sites = yaml.safe_load(f)
    print("Already stored values in yaml: ",y_sites)
    for y_object in y_sites:
        for site in y_object.keys():
            ip = socket.gethostbyname(site)
            if y_object[site] != ip:
                print("[ERROR IN YAML] ",site," IP mismatch: ",y_object.get(site), ip)
                object[site]=ip
        with open('sites.json', 'w') as f:
            yaml.dump(y_sites,f)
if __name__== "__main__":
    main()