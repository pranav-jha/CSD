import sys, re

CommTypeA = 'A'
CommTypeC = 'C'
CommTypeL = 'L'

class SymbolTable:
    preSymbols = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4, 'R0': 0,
                  'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
                  'R8': 8, 'R9': 9,' R10': 10, 'R11': 11, 'R12': 12, 'R13': 13,
                  'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
    
    def __init__(self):
        self.s_table = SymbolTable.preSymbols

    def contains(self, symbol):
        return symbol in self.s_table

    def address(self, symbol):
        return self.s_table[symbol]

    def addPair(self, symbol, address):
        self.s_table[symbol] = address

class cs16b019_20_Parser:
    def __init__(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.commands = list(filter(len,
                                            [re.sub('//.*$', '', l).strip() for l in f]))
        except FileNotFoundError:
            print("Could not find %s" % (filepath))

    def hasMoreCommands(self):
        return len(self.commands) > 0

    def next(self):
        self.command = self.commands.pop(0)

    def commandType(self):
        if self.command[0] == '@':
            return CommTypeA
        elif self.command[0] == '(' and self.command[-1] == ')':
            return CommTypeL
        return CommTypeC

    def symbol(self):
        return self.command.strip('@()')

    def dest(self):
        if '=' not in self.command:
            return ''
        return self.command.split('=')[0]

    def comp(self):
        return self.command.split('=')[-1].split(';')[0]

    def jump(self):
        if ';' not in self.command:
            return ''
        return self.command.split('=')[-1].split(';')[-1]
