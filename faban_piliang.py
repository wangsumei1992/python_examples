import os, sys

def faban(branch):
    projects = ['api', 'manager', 'pay', 'trade', 'www']
    for i in projects:
        shell = 'sh' + i + '.sh' + branch
        os.system(shell)

    os.system("")

if __name__ == '__main__':
    branch_ls = sys.argv
    if len(branch_ls) != 2:
        branch = "develop"
    else:
        branch = branch_ls[1]
    faban(branch)