# -*- coding: utf-8 -*-

from src.shell import Shell

def main(args):
    s = Shell()
    s.run()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
