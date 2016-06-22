#!/usr/bin/env python3
# coding=utf-8
"""
Lorum ipsum

Usage:
  filetool.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 30-09-15 / 20:57
"""
import os
import sys
import time

from arguments import Arguments
from consoleprinter import console, query_yes_no

if sys.version_info.major < 3:
    console("\033[31mpython3 is required\033[0m")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.input = ""
        super().__init__(doc)


def ossystem(cmd):
    """
    @type cmd: str
    @return: None
    """

    # print(cmd)
    os.system(cmd)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)

    def endswith(extension):
        """
        @type extension: str
        @return: None
        """
        return arguments.input.lower().endswith(extension)

    print("\033[91mopen: {}\033[0m".format(arguments.input))

    if "dash://" in arguments.input:
        os.system("/usr/bin/open " + arguments.input)
    elif "http" in arguments.input and not endswith("md"):
        os.system("osascript -e 'tell application \"Google Chrome\" to open location \"" + arguments.input + "\"'")
        os.system("osascript -e 'tell application \"Google Chrome\" to activate';")

        return
    else:
        arguments.input = os.path.abspath(os.path.expanduser(str(arguments.input)))

    alternative = ""

    if not os.path.exists(arguments.input):
        console(arguments.input, "not found", color="red")
        alts = os.popen("mdfind " + os.path.basename(arguments.input) + " | grep " + os.path.basename(arguments.input).split(".")[0] + " | grep -v pyc 2> /dev/null").read()
        alts = [x.strip() for x in str(alts).split("\n") if x.strip()]
        alts.extend([os.path.join(os.getcwd(), x) for x in os.listdir() if x.strip() and os.path.basename(arguments.input).split(".")[0] in x])

        if len(alts) > 0:
            alts = list(set(alts))
            alts.sort(key=lambda x: len(x))

            for alternative2 in alts:
                if query_yes_no("Try \033[34m" + alternative2 + "\033[96m instead?", default=False):
                    alternative = alternative2
                    break
            else:
                return
        else:
            return

    if alternative:
        arguments.input = alternative
        console("opening", arguments.input, color="darkyellow")

    pycharm = False
    sublime = False

    if endswith("py"):
        if query_yes_no("Use sublime=Y(def), or pycharm=N?", default=True):
            pycharm = False
            sublime = True
        else:
            pycharm = True
            sublime = False

    elif endswith("html"):
        if os.path.exists(arguments.input):
            location = "file://" + os.path.join(os.getcwd(), arguments.input)
        else:
            location = arguments.input

        os.system("osascript -e 'tell application \"Safari\" to open location \"" + location + "\"'")
        time.sleep(0.2)
        os.system("osascript -e 'tell application \"Safari\" to activate';")
    elif os.path.isdir(arguments.input):
        if os.path.exists(os.path.join(arguments.input, "setup.py")):
            pycharm = True

    if pycharm:
        if os.path.exists(os.path.join(arguments.input, ".idea")):
            cmd = "cd '" + arguments.input
            cmd += "'&&/Applications/PyCharm.app/Contents/MacOS/pycharm '" + arguments.input + "'' > /dev/null 2> /dev/null &"
        else:
            cmd = "cd '" + os.path.dirname(arguments.input)
            cmd += "'&&/Applications/PyCharm.app/Contents/MacOS/pycharm " + os.path.dirname(arguments.input) + " > /dev/null 2> /dev/null &"

        ossystem(cmd)
        time.sleep(0.2)
        ossystem("osascript -e 'tell application \"Pycharm\" to activate'")
    elif sublime:
        cmd = '/usr/bin/open -a /Applications/Sublime\ Text.app ' + arguments.input
        ossystem(cmd)
        time.sleep(0.2)
        ossystem("osascript -e 'tell application \"Sublime\" to activate'")
    else:
        os.system("cd '" + os.path.dirname(arguments.input) + "'&&/usr/bin/open '" + arguments.input + "'")

# print(cmd)


if __name__ == "__main__":
    main()
