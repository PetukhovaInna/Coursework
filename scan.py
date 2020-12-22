import subprocess as sp
import os

def software_scan():
    cmd = ['apt', 'list', '--installed'] 
    process=sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode().replace('\t',' ').split('\n')

def print_soft(soft_list: list = software_scan()):
    for i in soft_list:
        print(i)


def scan_save(scan_results: list = software_scan()[1:], filename: str = 'soft_scan.txt'):
    with open(filename, 'w') as scan_file:
        for item in scan_results:
            scan_file.write("%s\n" % item)


def get_full_list():
    print(os.system("find / -perm /111"))