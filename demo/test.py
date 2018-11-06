import os
import sys
import time

if __name__ == '__main__':
    os.system("ls /gruntdata")
    for i in range(10):
        sys.stderr.write("\nvalidation at step 100\n")
        print('hello')
        time.sleep(10)
        
    with open('/gruntdata/datacube/test.txt') as f:
        print(f.read())
        
    workspace = '/gruntdata/datacube/test/80/pnasnet_large/sample'
    os.chdir(workspace)
    os.system('python alps_job_wrapper.py')
    sys.exit(0)
