import os
import sys
import time

if __name__ == '__main__':
    for i in range(1000):
        sys.stderr.write("\nvalidation at step 100\n")
        print('hello')
        time.sleep(10)

    sys.exit(0)
