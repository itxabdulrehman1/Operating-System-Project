class Process:
    def __init__(self, pid, sequence, memory_manager):
        self.pid = pid
        self.sequence = sequence
        self.mem_manager = memory_manager

    def run(self):
        for i, page in enumerate(self.sequence):
            future_seq = self.sequence[i+1:] if self.mem_manager.algorithm == 'optimal' else None
            self.mem_manager.access_page(self.pid, page, future_sequence=future_seq)

