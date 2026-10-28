with open('application.log', 'r') as application:
    log = application.read()

err_war_count = 0

print('''ERROR REPORT
----------------------------------------''')

for num,line in enumerate(log.split('\n')):
    segment = line.split('|')
    date = segment[0].strip()
    status = segment[1]
    description = segment [2]
    if ('ERROR' in status.upper()) or ('WARNING' in status.upper()):
        err_war_count += 1
    
        log_order = date.strip(), status.upper().strip(), description.strip()
        log_message = ' - '.join(log_order)
        print(log_message)

print(f'\nTotal errors and warnings: {err_war_count}')
