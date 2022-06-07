# Mike Bangham [ michael.bangham3@gmail.com ] 2021
# remliteral deletes Windows folders/files when all else fails

import sys
from subprocess import Popen, PIPE


def main(fp):
     proc = Popen(["powershell", "-Command", "Remove-Item", "-LiteralPath", '"{}"'.format(fp),
                   "-Force", "-Recurse", "-Verbose"], stdout=PIPE, stderr=PIPE)
     print('Finished Execution\n{}\n{}'.format(proc.stdout.readline().decode(), proc.stderr.readline().decode()))


if __name__ == "__main__":
     try:
          fp = sys.argv[1]
     except IndexError:
          print('Usage: python remliteral.py <path-to-folder')
          sys.exit()
     main(fp)