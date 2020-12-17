import subprocess as sp
import os


def software_scan(print_it: bool = False): #print_it - первое задание
    cmd = ['apt', 'list', '--installed']
    process=sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    if (print_it == True):
        print_soft(stdout.decode().replace('\t',' ').split('\n'))
    return stdout.decode().replace('\t',' ').split('\n')



def print_soft(soft_list: list = software_scan()):
    for i in soft_list:
        print(i)


def scan_save(scan_results: list = software_scan(), filename: str = 'soft_scan.txt'):
    with open(filename, 'w') as scan_file:
        for item in scan_results[1:]:
            scan_file.write("%s\n" % item)



def get_full_list(): #Все файлы с разрешением на исполнение
    print(os.system("find / -perm /111"))
