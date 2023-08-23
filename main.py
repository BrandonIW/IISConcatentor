import glob

from os import path
from time import sleep


def main():
    """For when you end up with a shitload of IIS logs and you just wanna concatenate all the days into one text file"""
    while True:
        args = input("Type directory where IIS logs are present. There should be nothing in this dir. other than IIS "
                     "logs: ")
        if _input_validator(args):
            return parser(args)
        print("Path provided could not be found. Try again")
        sleep(2)


def parser(args):
    filelist_trailing = glob.glob(args + "*")
    if len(filelist_trailing) > 1:
        final_list = filelist_trailing
    else:
        final_list = glob.glob(args + "\\*")

    with open('concatfile.txt', 'a') as concatfile:
        concatfile.write("date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) "
                         "cs(Referer) sc-status sc-substatus sc-win32-status time-taken\n")
        for file in final_list:
            with open(file, 'r') as file:
                filecontent = file.readlines()
                for line in filecontent[4:]:
                    concatfile.write(line)


def _input_validator(args):
    if path.isdir(args):
        return True
    return False


if __name__ == "__main__":
    main()
