class BootCodeRunner:
    def __init__(self, file):
        with open(file) as f:
            self.instructions = [(inst, int(value)) for line in f for inst, value in [line.strip().split()]]
        self.visited_indexes = {0}
        self.accumulator = 0

    @property
    def index(self):
        return self.__dict__.get("index", 0)

    @index.setter
    def index(self, value):
        self.__dict__["index"] = value
        if value in self.visited_indexes:
            print(f"Reached index {value} again, infinite loop detected")
            print(f"Accumulator value: {self.accumulator}")
            exit()
        self.visited_indexes.add(value)

    def run(self):
        size = len(self.instructions)
        while self.index != size:
            self._run_next_instruction()

    def _run_next_instruction(self):
        instruction, value = self.instructions[self.index]
        getattr(self, "_" + instruction)(value)

    def _nop(self, value):
        self.index += 1

    def _acc(self, value):
        self.index += 1
        self.accumulator += value

    def _jmp(self, value):
        self.index += value


runner = BootCodeRunner("input.txt")
runner.run()
