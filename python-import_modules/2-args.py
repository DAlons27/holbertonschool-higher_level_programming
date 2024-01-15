#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv) - 1
    print("{} argument{}"
          .format(len_arg, "s." if len_arg == 0
                  else ":" if len_arg == 1 else "s:"))
    for i in range(len_arg):
        print("{}: {}".format(i + 1, argv[i + 1]))
