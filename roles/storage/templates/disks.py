import os
import sys
import json

datafile = "/home/koho/code/facts.json"
sizelist = ["931.51 GB", "894.25 GB"]
paritysize =  "7.28 TB"

def main(file):
    with open(file) as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    disks = [drive for drive in data["devices"] if "sd" in drive]
    dataDiskUuids = []
    count = 1
    for item in disks:
        if data["devices"][item]["size"] in sizelist:
            dataDiskUuids.append(f'UUID={data["devices"][item]["links"]["uuids"][0]}')
            # dataDiskUuids.append("{{path: '{}', src: '{}'}}".format(f'/mnt/disk{count}',f'UUID={data["devices"][item]["links"]["uuids"][0]}'))
            count += 1
    for item in disks:
        if data["devices"][item]["size"] == paritysize:
            dataDiskUuids.append(f'UUID={data["devices"][item]["links"]["uuids"][0]}')
            # dataDiskUuids.append("{{path: '{}', src: '{}'}}".format(f'/mnt/parity', f'UUID={data["devices"][item]["links"]["uuids"][0]}'))
    # print(dataDiskUuids)
    for item in dataDiskUuids:
        print(item)

    
        


if __name__ == "__main__":
    main(datafile)
