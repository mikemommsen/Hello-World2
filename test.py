import sys, os, shutil

def this(x):
  return x
  
# this is a comment

hey liz i am writing this here

def processline(inline):
  counter = 0
  x = inline.split(',')
  for i in x:
    counter += 1
  return counter

def processfile(infile):
  f = open(infile)
  counter = set()
  counter2 = set()
  for r in f:
    counter.add(r.split(',')[1])
    counter2.add(r.split(',')[0])
  print infile, len(counter), len(counter2)
  
def rundir(indir):
  os.chdir(indir)
  files = sorted(os.listdir('.'))
  for x in files:
    processfile(x)
  
def main():
  indir = sys.argv[1]
  rundir(indir)

if __name__ == '__main__':
  main()
