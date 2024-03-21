#Byte addressable Data mem
DataMem = ["0"*8]*40000000

#Accessing the Binary file
file=input("Enter file name:")
f=open(f"{file}.txt", "r")
text=(f.read()).splitlines()
textString="".join(text)
InstMem=[]

#Converting the binary instruction to byte addressable Instruction memory
l=0
r=8
for i in range(len(textString)//8):
    InstMem.append(textString[l:r])
    l+=8
    r+=8

#Functions for 2s complement conversions
def int_(binary):
    if binary[0] == '1':
        inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
        twos_complement = bin(int(inverted, 2) + 1)[2:]
        result = -int(twos_complement, 2)
    else:
        result = int(binary, 2)
    return result

def bin_(integer, bit):
    b=bin(abs(integer))[2:]
    l=len(b)
    if bit == 32:
        if integer >=0:
            return f"{integer:032b}"
        else:
            return "1" * (32 - l) + b
    elif bit == 64:
        if integer >= 0:
            return f"{integer:064b}"
        else:
            return "1" * (64 - l) + b

#Making a class for Register memory with standard attributes which maintain a reg dictionary
class Reg():
    def __init__(self, registers):
        self.regs = registers
        self.RD1 = ""
        self.RD2 = ""
        self.Wreg = ""
    def Read1(self, RegOp):
        self.RD1 = self.regs[RegOp]
    def Read2(self, RegOp):
        self.RD2 = self.regs[RegOp]
    def write(self, data):
        if(len(data)==32):
            self.regs[self.Wreg] = data
        else:
            self.regs["hi"] = data[0:32]
            self.regs["lo"] = data[32:]
            self.regs[self.Wreg] = data[32:]
    def print(self):
        print(self.regs)

#Dictionary containing all the registers
regs = {
    "00000": str(0)*32,  # $0
    "00001": str(0)*32,  # $at
    "00010": str(0)*32,  # $v0
    "00011": str(0)*32,  # $v1
    "00100": str(0)*32,  # $a0
    "00101": str(0)*32,  # $a1
    "00110": str(0)*32,  # $a2
    "00111": str(0)*32,  # $a3
    "01000": str(0)*32,  # $t0
    "01001": str(0)*32,  # $t1
    "01010": str(0)*32,  # $t2
    "01011": str(0)*32,  # $t3
    "01100": str(0)*32,  # $t4
    "01101": str(0)*32,  # $t5
    "01110": str(0)*32,  # $t6
    "01111": str(0)*32,  # $t7
    "10000": str(0)*32,  # $s0
    "10001": str(0)*32,  # $s1
    "10010": str(0)*32,  # $s2
    "10011": str(0)*32,  # $s3
    "10100": str(0)*32,  # $s4
    "10101": str(0)*32,  # $s5
    "10110": str(0)*32,  # $s6
    "10111": str(0)*32,  # $s7
    "11000": str(0)*32,  # $t8
    "11001": str(0)*32,  # $t9
    "11010": str(0)*32,  # $k0
    "11011": str(0)*32,  # $k1
    "11100": str(0)*32,  # $gp
    "11101": str(0)*32,  # $sp
    "11110": str(0)*32,  # $fp
    "11111": str(0)*32,  # $ra
    "hi": str(0)*32,
    "lo": str(0)*32
}

#Function for the sign extend module
def signExtend(Imm):
    return Imm[0]*16+Imm

#Function for control unit which returns a dictionary with all the control lines
def control_signal(instruction):
    opcode = instruction[0:6]
    control_signals = {}
    if opcode == '000000':
        func = instruction[26:]
        if func == "100000":  # add
            control_signals["ALUOp"] = "10"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"
        elif func == "100010":  # sub
            control_signals["ALUOp"] = "10"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"
        elif func == "100100":  # and
            control_signals["ALUOp"] = "10"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"
        elif func == "100101":  # or
            control_signals["ALUOp"] = "10"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"
        elif func == "101010":  # slt
            control_signals["ALUOp"] = "10"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"
    elif opcode == "011100":      #mul
            control_signals["ALUOp"] = "11"
            control_signals["RegDst"] = "1"
            control_signals["ALUSrc"] = "0"
            control_signals["MemWrite"] = "0"
            control_signals["MemRead"] = "0"
            control_signals["MemToReg"] = "0"
            control_signals["RegWrite"] = "1"
            control_signals["Branch"] = "0"
            control_signals["Jump"] = "0"
            control_signals["beq"] = "0"

    elif opcode == '001000':  # addi
        control_signals["ALUOp"] = "00"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "1"
        control_signals["MemWrite"] = "0"
        control_signals["MemRead"] = "0"
        control_signals["MemToReg"] = "0"
        control_signals["RegWrite"] = "1"
        control_signals["Branch"] = "0"
        control_signals["Jump"] = "0"
        control_signals["beq"] = "0"

    elif opcode == "000100":  # beq
        control_signals["ALUOp"] = "01"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "0"
        control_signals["MemWrite"] = "0"
        control_signals["MemRead"] = "0"
        control_signals["MemToReg"] = "0"
        control_signals["RegWrite"] = "0"
        control_signals["Branch"] = "1"
        control_signals["Jump"] = "0"
        control_signals["beq"] = "1"

    elif opcode == "000101":  # bne
        control_signals["ALUOp"] = "01"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "0"
        control_signals["MemWrite"] = "0"
        control_signals["MemRead"] = "0"
        control_signals["MemToReg"] = "0"
        control_signals["RegWrite"] = "0"
        control_signals["Branch"] = "1"
        control_signals["Jump"] = "0"
        control_signals["beq"] = "0"

    elif opcode == "100011":  # lw
        control_signals["ALUOp"] = "00"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "1"
        control_signals["MemWrite"] = "0"
        control_signals["MemRead"] = "1"
        control_signals["MemToReg"] = "1"
        control_signals["RegWrite"] = "1"
        control_signals["Branch"] = "0"
        control_signals["Jump"] = "0"
        control_signals["beq"] = "0"
    elif opcode == "101011":  # sw
        control_signals["ALUOp"] = "00"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "1"
        control_signals["MemWrite"] = "1"
        control_signals["MemRead"] = "0"
        control_signals["MemToReg"] = "0"
        control_signals["RegWrite"] = "0"
        control_signals["Branch"] = "0"
        control_signals["Jump"] = "0"
        control_signals["beq"] = "0"
    elif opcode == "000010":        #jump
        control_signals["ALUOp"] = "00"
        control_signals["RegDst"] = "0"
        control_signals["ALUSrc"] = "0"
        control_signals["MemWrite"] = "0"
        control_signals["MemRead"] = "0"
        control_signals["MemToReg"] = "0"
        control_signals["RegWrite"] = "0"
        control_signals["Branch"] = "0"
        control_signals["Jump"] = "1"
        control_signals["beq"] = "0"
    else:
        print("op not present")
    return control_signals

#Function for ALU which also contains a sub function-ALU control
def ALU(a1,a2,ALUOp,fun):
    def ALUCont(ALUOp, fun):
        if ALUOp == "00":
            return "010"
        if ALUOp == "01":
            return "011"
        if ALUOp == "10":
            if fun == "100000":
                return "010"
            elif fun == "100010":
                return "011"
            elif fun == "100100":
                return "000"
            elif fun == "100101":
                return "001"
            elif fun == "101010":
                return "100"
        if ALUOp == "11":
            return "101"

    ALUcont=ALUCont(ALUOp,fun)
    global zeroflag
    if(ALUcont=="000"):
        return (int_(a1) & int_(a2))
    elif(ALUcont=="001"):
        return (int_(a1) | int_(a2))
    elif(ALUcont=="010"):
        return (bin_(int_(a1)+int_(a2),32))
    elif(ALUcont=="011"):
        zeroflag = not(int_(a1)-int_(a2))
        return (bin_(int_(a1)-int_(a2),32))
    elif(ALUcont=="100"):
        return (bin_(int(int_(a1)<int_(a2)),32))
    elif (ALUcont=="101"):
        return (bin_(int_(a1)*int_(a2),64))

#Creating the RegMem as a Reg object
RegMem = Reg(regs)


PC = 0
zeroflag=0
while (PC < len(InstMem)):

    #Instruction Fetch
    instr = InstMem[PC]+InstMem[PC+1]+InstMem[PC+2]+InstMem[PC+3]
    RegMem.Read1(instr[6:11])
    RegMem.Read2(instr[11:16])

    #Send instruction to Control unit
    control_signals=control_signal(instr)

    #Instruction Decode
    if(int(control_signals["RegDst"])):
        RegMem.Wreg = instr[16:21]
    else:
        RegMem.Wreg = instr[11:16]

    extended=signExtend(instr[16:])

    #Instruction Execute
    if(int(control_signals["ALUSrc"])):
        ALUResult=ALU(RegMem.RD1,extended,control_signals["ALUOp"],instr[26:])
    else:
        ALUResult=ALU(RegMem.RD1,RegMem.RD2,control_signals["ALUOp"],instr[26:])
    Address=int_(ALUResult)

    #Memory access
    if(int(control_signals["MemWrite"],2)):
        DataMem[Address]=RegMem.RD2[0:8]
        DataMem[Address+1] = RegMem.RD2[8:16]
        DataMem[Address+2] = RegMem.RD2[16:24]
        DataMem[Address+3] = RegMem.RD2[24:32]
    else:
        ReadData="".join(DataMem[Address:Address+4])

    #Memory write-back
    if(int(control_signals["MemToReg"])):
        if(int(control_signals["RegWrite"])):
            RegMem.write(ReadData)
    else:
        if(int(control_signals["RegWrite"])):
            RegMem.write(ALUResult)


    #PC update(normal/branch/jump)
    PCAdder1 = PC+4
    sl2 = int_(extended) * 4 #shift imm value by 2 bits(as byte addressable)
    PCAdder2 = PCAdder1+sl2
    if(int(control_signals["Jump"])):
        PC=4*int_(instr[6:]) - (12288)
    elif(zeroflag and int(control_signals["beq"]) and int(control_signals["Branch"])):
        PC = PCAdder2
    elif(not(zeroflag) and not(int(control_signals["beq"])) and int(control_signals["Branch"])):
        PC = PCAdder2
    else:
        PC = PCAdder1


print(InstMem)
RegMem.print()

if(file=="ifaispowb"):
    print(int_(RegMem.regs["10111"]))
elif(file=="Factorial"):
    print(int_(RegMem.regs["10001"]))
elif(file=="Power"):
    print(int_(RegMem.regs["10010"]))