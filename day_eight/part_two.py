from copy import deepcopy


class BootCodeRunner:
    def __init__(self, file=None):
        if file:
            with open(file) as f:
                self.instructions = [(inst, int(value)) for line in f for inst, value in [line.strip().split()]]
            self.visited_indexes = {0}
            self.accumulator = 0
            self.cloned = False
        else:
            self.cloned = True
        self.is_infinite = False

    @property
    def index(self):
        return self.__dict__.get("index", 0)

    @index.setter
    def index(self, value):
        if value in self.visited_indexes:
            print(f"Reached index {value} again, infinite loop detected")
            print(f"Accumulator value: {self.accumulator}")
            self.is_infinite = True
        else:
            self.__dict__["index"] = value
            self.visited_indexes.add(value)

    def clone(self):
        runner = BootCodeRunner()
        runner.accumulator = self.accumulator
        runner.visited_indexes = set()
        runner.index = self.index
        runner.visited_indexes = deepcopy(self.visited_indexes)
        runner.instructions = deepcopy(self.instructions)
        inst, value = runner.instructions[self.index]
        print(f"Swapping {inst} instruction at index {self.index}")
        inst = "nop" if inst == 'jmp' else 'jmp'
        runner.instructions[self.index] = (inst, value)
        runner.run()

    def run(self):
        size = len(self.instructions)
        while self.index != size:
            self._run_next_instruction()
            if self.is_infinite:
                break
        else:
            print("Program exited gracefully")
            print(f"Accumulator: {self.accumulator}")
            exit()

    def _run_next_instruction(self):
        instruction, value = self.instructions[self.index]
        getattr(self, "_" + instruction)(value)

    def _nop(self, value):
        if not self.cloned:
            self.clone()
        self.index += 1

    def _acc(self, value):
        self.index += 1
        if not self.is_infinite:
            self.accumulator += value

    def _jmp(self, value):
        if not self.cloned:
            self.clone()
        self.index += value


runner = BootCodeRunner("input.txt")
runner.run()
