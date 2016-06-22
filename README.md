# filetool
Open a [file]() with the correct MacOS program from the terminal, if it's not in the current folder it will look it up and open the correct tooling for that file.

## dependency
- [Consoleprinter](https://github.com/erikdejonge/consoleprinter) for *console, query_yes_no*
- [Arguments](https://github.com/erikdejonge/arguments) for *Arguments*

``` bash
pip3 install Arguments
pip3 install consoleprinter
```

## install
clone project
make alias

``` bash
cd
mkdir -p workspace
cd workspace
git clone git@github.com:erikdejonge/filetool.git
cd
echo 'alias filetool="python3 ~/workspace/filetool/filetool.py"' >> .bash_profile
echo 'alias filetool="python3 ~/workspace/filetool/filetool.py"' | sh
```

## example

``` bash
[Desktop] filetool process_youtube.py
open: process_youtube.py
2.12 | openfile.py:80 | process_youtube.py | not found
Try /Users/rabshakeh/workspace/research/youtubedownload/process_youtube.py instead?
[y/N/q] $: y
-> yes
7772.82 | openfile.py:101 | opening
Use sublime=Y(def), or pycharm=N?
[Y/n/q] $:
Opening file process_youtube.py with sublime
```
