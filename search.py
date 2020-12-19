import scan

def soft_search(search_args: list, soft_list: list = scan.software_scan()):
    found = []
    not_found = []
    for arg in search_args:
        flag = False
        for line in soft_list:
            if (arg in line):
                flag = True
                found.append(line)
        if (flag == False):
            not_found.append(arg)
            
    if (found == []):
        print('Совпадений не найдено')
    else:
        print('\nНайдены следующие совпадения:\n')
        scan.print_soft(found)
        if (not_found != []):
            print('\nПо следующим запросам совпадений не найдено:\n')
            scan.print_soft(not_found)
