#!/usr/bin/env python3
import sys

try:
    file = sys.argv[1]
    with open(file,"w") as f:
        f.write("#!/usr/bin/env python3\n\n")
        print("\nsuccess\n")
except:
    print("\nNo arguments given!\n")
    exit(1)

