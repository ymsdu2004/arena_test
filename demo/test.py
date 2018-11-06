import os
import sys
import time
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'training process startup arguments')
    parser.add_argument('--project_dir', help = 'project directory', required = True)
    parser.add_argument('--job_args', help = 'job arguments', required = False)
    return parser.parse_args()

if __name__ == '__main__':
    #os.system("ls /gruntdata")
    #for i in range(10):
    #    sys.stderr.write("\nvalidation at step 100\n")
    #    print('hello')
    #    time.sleep(10)
        
    #with open('/gruntdata/datacube/test.txt') as f:
    #    print(f.read())
    
    args = parse_arguments()
    project_dir = args.project_dir
    job_args = args.job_args or ''
    
    workspace = '.workspace'
    os.mkdir(workspace)
    os.system('cp -r %s/* %s' % (project_dir, workspace))
    os.chdir(workspace)
    os.system('python alps_job_wrapper.py %s' job_args)
    sys.exit(0)
