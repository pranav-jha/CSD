
import sys, os
from cs16b019_20_Parser import *

class Code:
    compa0 = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100',
              'A': '110000', '!D': '001101', '-D': '001111', '-A': '110011',
              'D+1': '011111', 'A+1': '110111', 'D-1': '001110',
              'A-1': '110010', 'D+A': '000010', 'D-A': '010011',
              'A-D': '000111', 'D&A': '000000', 'D|A': '010101'}
    mapDest = {'': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
               'AM': '101', 'AD': '110', 'AMD': '111'}
    mapJump = {'': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
                'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
    compa1 = {'M': '110000', '!M': '110001', '-M': '110011', 'M+1': '110111',
              'M-1': '110010', 'D+M': '000010', 'D-M': '010011',
              'M-D': '000111', 'D&M': '000000', 'D|M': '010101'}

    @staticmethod
    def dest(mnemonic):
        return Code.mapDest[mnemonic]

    @staticmethod
    def comp(mnemonic):
        if mnemonic in Code.compa1:
            return '1' + Code.compa1[mnemonic]
        elif mnemonic in Code.compa0:
            return '0' + Code.compa0[mnemonic]

    @staticmethod
    def jump(mnemonic):
        return Code.mapJump[mnemonic]

class Assembler:
    def __init__(self, files):
        self.files = files
        self.table = SymbolTable()

    def hasFile(self):
        return len(self.files) > 0

    def softPass(self):
        asmfile = self.files[0]
        p = cs16b019_20_Parser(asmfile)
        current_address = 0
        while p.hasMoreCommands():
            p.next()
            cmd_type = p.commandType()
            if cmd_type is CommTypeA or cmd_type is CommTypeC:
                current_address += 1
            elif cmd_type is CommTypeL:
                self.table.addPair(p.symbol(), current_address)

    def getAddress(self,  symbol):
        if symbol.isdigit():
            return symbol
        else:
            if not self.table.contains(symbol):
                self.table.addPair(symbol, self.current_address)
                self.current_address += 1
            return self.table.address(symbol)

    def translateFile(self):
        asmfile = self.files.pop(0)
        p = cs16b019_20_Parser(asmfile)
        if asmfile.endswith('.asm'):
            fileout = asmfile.replace('.asm', '.hack')
        else:
            fileout = asmfile + '.hack'
        f = open(fileout, 'w')
        print("CS16B019-CS16B020 Translating %s" % (asmfile))
        self.current_address = 16
        while p.hasMoreCommands():
            p.next()
            if p.commandType() is CommTypeA:
                address = self.getAddress(p.symbol())
                instruction = '{0:016b}'.format(int(address))
            elif p.commandType() is CommTypeC:
                instruction = ''.join(['111', Code.comp(p.comp()),
                                       Code.dest(p.dest()), Code.jump(p.jump())])
            else:
                continue
            print(instruction, end='\n', file=f)
        f.close()
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Type: python3 Assembler.py FILE")
        sys.exit(1)
    cs16b019_20 = Assembler(sys.argv[1:])
    while cs16b019_20.hasFile():
        cs16b019_20.softPass()
        cs16b019_20.translateFile()
