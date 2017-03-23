import getopt

import sys

import manager_util as manager_util

VERSION = "1.0"


def print_help():
    print(__doc__.strip())


def prepare_data_from_row(path, input_file, minutes, time_behind_minutes):
    output = manager_util.get_generate_minutes_splited(path=path,
                                                       input_file=input_file,
                                                       minutes=minutes)

    manager_util.group_by_hours_temperature(path=path,
                                            input_file=output,
                                            minutes=minutes,
                                            time_behind_hours=time_behind_minutes)

    manager_util.group_by_hours_environment_humidity(path=path,
                                                     input_file=output,
                                                     minutes=minutes,
                                                     time_behind_hours=time_behind_minutes)

    manager_util.group_by_hours_ground_humidity(path=path,
                                                input_file=output,
                                                minutes=minutes,
                                                time_behind_hours=time_behind_minutes)

    manager_util.group_by_hours_luminosity(path=path,
                                           input_file=output,
                                           minutes=minutes,
                                           time_behind_hours=time_behind_minutes)


def main():
    optlist, arglist = getopt.getopt(sys.argv[1:], "p:i:m:t:Vhs")
    flags = dict(optlist)

    if '-V' in flags:
        print(VERSION)
        sys.exit(0)

    path = flags.get('-p', None)
    input_file = flags.get('-i', None)
    minutes = int(flags.get('-m', None))
    time_behind_minutes = int(flags.get('-t', None))

    if path is None or input_file is None or minutes is None or time_behind_minutes is None:
        print 'Error a parameter is missing'
        return
    print 'Wait until the data be processed :)'
    prepare_data_from_row(path=path,
                          input_file=input_file,
                          minutes=minutes,
                          time_behind_minutes=time_behind_minutes)

    print 'Done! :) yaaaaaaaaayyyyy!!!!! \o/'


if __name__ == '__main__':
    main()
