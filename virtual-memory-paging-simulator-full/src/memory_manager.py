import threading
import time
from collections import deque
import csv
import os

class MemoryManager:
    def __init__(self, num_frames, algorithm='fifo', io_latency=0.001, log_dir='logs'):
        self.num_frames = num_frames
        self.algorithm = algorithm.lower()
        self.io_latency = io_latency
        self.frames = []
        self.page_order = deque()
        self.lock = threading.Lock()
        self.page_faults = 0
        self.access_log = []
        self.log_dir = log_dir

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def access_page(self, pid, page, future_sequence=None):
        """Access a page for a process, handle page fault if needed"""
        with self.lock:
            hit = page in self.frames
            if hit:
                if self.algorithm == 'lru':
                    self.page_order.remove(page)
                    self.page_order.append(page)
                self.access_log.append([pid, page, 'HIT'])
                print(f"Process {pid}: Page {page} HIT")
            else:
                self.page_faults += 1
                self.access_log.append([pid, page, 'FAULT'])
                print(f"Process {pid}: Page {page} FAULT")
                self.handle_page_fault(page, future_sequence)
            time.sleep(self.io_latency)

    def handle_page_fault(self, page, future_sequence=None):
        if len(self.frames) < self.num_frames:
            self.frames.append(page)
        else:
            if self.algorithm in ['fifo', 'lru']:
                victim = self.page_order.popleft()
                self.frames.remove(victim)
            elif self.algorithm == 'optimal':
                victim = self.select_optimal_victim(future_sequence)
                self.frames.remove(victim)
            self.frames.append(page)
        self.page_order.append(page)

    def select_optimal_victim(self, future_sequence):
        """Select the page that will not be used for the longest time"""
        farthest_index = -1
        victim_page = None
        for page in self.frames:
            try:
                index = future_sequence.index(page)
            except ValueError:
                index = float('inf')
            if index > farthest_index:
                farthest_index = index
                victim_page = page
        return victim_page

    def write_logs(self, algorithm_name):
        """Write page access and summary logs to CSV"""
        access_file = os.path.join(self.log_dir, f'access_log_{algorithm_name}.csv')
        summary_file = os.path.join(self.log_dir, f'summary_{algorithm_name}.csv')

        with open(access_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ProcessID', 'Page', 'Status'])
            writer.writerows(self.access_log)

        with open(summary_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Total Page Faults'])
            writer.writerow([self.page_faults])

    def summary(self):
        print(f"Simulation complete. Total Page Faults: {self.page_faults}")

