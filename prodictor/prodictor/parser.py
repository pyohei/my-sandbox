"""Create cron schedule from exported data from `crontab -l` ."""
from crontab import CronTab
from datetime import timedelta
import os
import re
import warnings


IGNORE_CASES = ['MAILTO', '#']


def stop_future_warning(func):
    """Stop printing warning."""
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', FutureWarning)
            return func(*args, **kwargs)
    return wrapper


def __create_file_object_by_server(directory):
    """Read cronfile and create file object."""
    server_list = {}
    for server_file in os.listdir(directory):
        file_path = os.path.join(directory, server_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            name, __ext = os.path.splitext(server_file)
            server_list[name] = lines
    return server_list


@stop_future_warning
def main(directory, start, end):
    """Main process."""
    targets = {}

    for sv, lines in __create_file_object_by_server(directory).items():
        for li in lines:
            li = li.rstrip()
            if not is_cron_script(li):
                continue

            nz_crnon = normalize_cron_script(li)
            cron_time = nz_crnon[0]
            cron_script = nz_crnon[1]

            # TODO: has to handle error occuring missed cron script.
            c = CronTab(cron_time)

            current_time = start
            while current_time <= end:
                interval_second = c.next(current_time)
                current_time = current_time + \
                    timedelta(seconds=interval_second)
                if current_time > end:
                    break
                cron_combo = (sv, cron_script)
                if current_time not in targets:
                    targets[current_time] = [cron_combo]
                else:
                    targets[current_time].append(cron_combo)
    return targets

def is_cron_script(cron_script):
    for ic in IGNORE_CASES:
        if ic in cron_script or cron_script == '':
            return False
    return True

def normalize_cron_script(cron_script):
    result = re.sub(r'  +', '\t', cron_script)
    result_list = result.split('\t')
    return (' '.join(result_list[0:5]), result_list[-1])

def export(targets):
    header = 'date, hour, miniute, second, scrip, server\n'
    with open('result.csv', 'w') as f:
        f.write(header)
        for t, scripts in sorted(targets.items()):
            for s in scripts:
                result = '{0},{1},{2}\n'.format(
                        t.strftime('%Y-%m-%d,%H,%M,%S'),
                        s[1],
                        s[0])
                f.write(result)

if __name__ == '__main__':
    def _main():
        import argparse
        from datetime import datetime
        p = argparse.ArgumentParser(description="Download sites.")
        p.add_argument('-s', '--start', type=str,
                       default=datetime.now().strftime('%Y%m%d000000'),
                       help='Cron start datetime.(YYYYmmddHHMMSS)',
                       dest='start_datetime' )
        p.add_argument('-e', '--end', type=str,
                       help='Cron end datetime.(YYYYmmddHHMMSS)',
                       default=datetime.now().strftime('%Y%m%d235959'),
                       dest='end_datetime')
        p.add_argument('-d', '--directory', type=str,
                       help='Directory name excluding cron files.',
                       default='crontab',
                       dest='directory')
        args = p.parse_args()
        start = datetime.strptime(args.start_datetime, '%Y%m%d%H%M%S')
        end = datetime.strptime(args.end_datetime, '%Y%m%d%H%M%S')
        directory = args.directory
        
        t = main(directory, start, end)
        export(t)
    _main()
