import sys, os, shutil

def this(x):
  return x

def processline(inline):
  counter = 0
  x = inline.split(',')
  for i in x:
    counter += 1
  print counter

def processfile(infile):
  f = open(infile):
  for r in f:
    processline(r)
  
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
