"""Parameter operation."""

import argparse


def setup_common_params():
    parser = argparse.ArgumentParser(description='Parse product pages.')
    parser.add_argument('-c', '--count', type=int, default=1,
                        help='count')
    parser.add_argument('--min-sleep', type=str, default=3,
                        help='minmum sleep time')
    parser.add_argument('--max-sleep', type=str, default=5,
                        help='maximum sleep time')
    args = parser.parse_args()
    count = args.count
    min_sleep = args.min_sleep
    max_sleep = args.max_sleep
    if min_sleep > max_sleep:
        raise ValueError('Exceeded your max time to min time!')
    print count
    print min_sleep
    print max_sleep

if __name__ == '__main__':
    setup_common_params()
