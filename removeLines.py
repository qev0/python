
listfile = 'mdfavlans.txt'
listFileWrite = 'newvlans.txt'
ipToKeep = ['10.','137.']

with open (listfile,'r') as f, open (listFileWrite, 'w') as f2:
  for line in f:
    if 'interface Vla' in line:
        f2.write(line)
    if 'description' in line:
        f2.write(line)
    if 'ip address' in line:
        f2.write(line)

