import scan

def compare(last_scan_file: str = 'soft_scan.txt', new_scan: list = scan.software_scan()):
    try:
        with open(last_scan_file, 'r', encoding='utf-8') as lsf:
            not_found = []
            for line in lsf.readlines():
                if (line.replace('\n', '') in new_scan):
                    new_scan.remove(line.replace('\n', ''))
                else:
                    not_found.append(line)
                    
        if (len(new_scan) <= 1):
            print('\nНовых программ не обнаружено')
        else:
            print('\nНовые программы:')
            scan.print_soft(new_scan)
        if (not_found == []):
            print('\nУдаления программ с прошлого сканирования не обнаружено')
        else:
            print('\nЭти программы удалились с прошлого сканирования:\n')
            scan.print_soft(not_found)
    except Exception as e:
        print(e)
