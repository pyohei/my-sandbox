"""Create cron schedule from exported data from `crontab -l` ."""
from crontab import CronTab
from datetime import datetime
from datetime import timedelta
import os
import re

IGNORE_CASE = ['MAILTO', '#']
CRON_FROM = datetime(2017, 1, 14, 23, 59, 59)
CRON_TO = datetime(2017, 1, 15, 6, 0, 0)
CRON_DIRECTORY_NAME = 'crontab'


def __create_file_object_by_server():
    server_list = {}
    for server_file in os.listdir(CRON_DIRECTORY_NAME):
        file_path = os.path.join(CRON_DIRECTORY_NAME, server_file)
        f = open(file_path, 'r')
        lines = f.readlines()
        name, __ext = os.path.splitext(server_file)
        server_list[name] = lines
        f.close()
    return server_list


def main():
    script_to_server = {}
    targets = {}

    for sv, lines in __create_file_object_by_server().items():
        for li in lines:
            is_ignore = False
            li = li.replace('\n', '')
            for c in IGNORE_CASE:
                if c in li or li == '':
                    is_ignore = True
                    break
            if is_ignore:
                continue

            # Maybe the below script is not good and has to fix.
            result = re.sub(r'  +', '\t',li) 
            result_list = result.split('\t')
            cron_time = ' '.join(result_list[0:5])
            cron_script = result_list[-1]

            if cron_script in script_to_server:
                script_to_server[cron_script].append(sv)
            else:
                script_to_server[cron_script] = [sv]
            c = CronTab(cron_time)
            current_time = CRON_FROM

            while current_time <= CRON_TO:
                interval_second = c.next(current_time)
                current_time = current_time + timedelta(seconds=interval_second)
                if current_time > CRON_TO:
                    print('FINISH,{0},{1}'.format(cron_script, cron_time))
                    break
                print('{0},{1}'.format(current_time, cron_script))
                if current_time not in targets:
                    targets[current_time] = [cron_script]
                else:
                    targets[current_time].append(cron_script)

    with open('result.csv', 'w') as f:
        header = 'date, hour, miniute, second, scrip, server\n'
        for t, scripts in sorted(targets.items()):
            f.write(header)
            for s in scripts:
                server_name = ' or '.join(script_to_server[s])
                result = '{0},{1},{2}\n'.format(t.strftime('%Y-%m-%d,%H,%M,%S'),
                                             s,
                                             server_name)
                f.write(result)

if __name__ == '__main__':
    main()
