import sys, os, shutil

def this(x):
  return x
  
def rundir(indir):
  os.chdir(indir)
  files = os.listdir('.')
  for x in files:
    processfile(x)
  
def main():
  indir = sys.argv[1]
  rundir(indir)

if __name__ == '__main__':
  main()
