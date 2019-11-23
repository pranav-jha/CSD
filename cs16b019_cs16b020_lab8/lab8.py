import os
import sys
filename=sys.argv[1]
filename=filename.split('.')[0]
k=os.getcwd()
os.system(k+'\\JackCompiler.bat')
os.system('python3 cs16b019_20_vm.py '+filename+'.vm')
os.system('python3 cs16b019_20_assembler.py '+filename+'.asm')