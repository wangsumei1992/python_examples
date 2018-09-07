"""统计代码行"""
import os

class CodeStat:

    def __init__(self):
        self.code_lines = 0
        self.comment_lines = 0
        self.blank_lines = 0

    def list_python_files(self):
        temp = os.listdir('./')
        #print(temp)
        return [f for f in temp if f.split('.')[-1] == 'py']

    def stat(self):
        for f in self.list_python_files():
            with open(f, 'rb') as file_handle:
                for line in file_handle.readlines():
                    striped_line = line.decode('utf-8').strip()
                    if striped_line == '':
                        self.blank_lines += 1
                    elif striped_line.startswith('#'):
                        self.comment_lines += 1
                    else:
                        self.code_lines += 1
        return self

    def display(self):
        print("code lines: %s\ncomment lines: %s\nblank lines: %s" % (self.code_lines, self.comment_lines, self.blank_lines))


if __name__ == '__main__':
    CodeStat().stat().display()