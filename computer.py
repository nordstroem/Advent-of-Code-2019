import itertools

def positional_mode(modes, i):
    return modes[-(i + 1)] == 0 if i < len(modes) else True

class Computer:
    def __init__(self, initial_memory, input_queue):
        self.memory = initial_memory
        self.pc = 0
        self.input_queue = input_queue
    
    def operations(self, opcode):
        ops = {
            1: self.add,
            2: self.mul,
            3: self.get_input,
            4: self.write_output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals
        }
        return ops[opcode]

    parameter_counts = { 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3 }

    def run(self):
        while self.memory[self.pc] != 99:
            instruction = str(self.memory[self.pc])
            opcode = int(instruction[-2:])
            modes = [int(c) for c in instruction[:-2]] 
            parameters = [self.memory[self.pc + i] for i in range(1, self.parameter_counts[opcode] + 1)]
            update_pc = self.operations(opcode)(*parameters, modes)
    
            if (update_pc):
                self.pc = self.pc + self.parameter_counts[opcode] + 1

    def add(self, src1, src2, dst, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        self.memory[dst] = a + b
        return True

    def mul(self, src1, src2, dst, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        self.memory[dst] = a * b
        return True

    def get_input(self, src, _):
        self.memory[src] = int(input("Enter input value: "))
        return True

    def write_output(self, src, modes):
        value = self.memory[src] if positional_mode(modes, 0) else src
        print(value)
        return True

    def equals(self, src1, src2, dst, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        self.memory[dst] = 1 if a == b else 0
        return True

    def less_than(self, src1, src2, dst, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        self.memory[dst] = 1 if a < b else 0
        return True

    def jump_if_true(self, src1, src2, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        if a != 0:
            self.pc = b
            return False
        return True

    def jump_if_false(self, src1, src2, modes):
        a = self.memory[src1] if positional_mode(modes, 0) else src1
        b = self.memory[src2] if positional_mode(modes, 1) else src2
        if a == 0:
            self.pc = b
            return False
        return True




