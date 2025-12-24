#!/usr/bin/env python3
import json
import threading
import argparse
from memory_manager import MemoryManager
from process import Process
from utils import setup_logging

def load_config(path):
    """Load JSON configuration"""
    with open(path, 'r') as f:
        return json.load(f)

def main():
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Virtual Memory Paging Simulator")
    parser.add_argument('--config', default='configs/config_small.json', help='Path to config JSON')
    parser.add_argument('--algorithm', default=None, choices=['fifo', 'lru', 'optimal'], help='Page replacement algorithm')
    args = parser.parse_args()

    print("\n=== Virtual Memory Paging Simulator ===")
    print("Starting simulator...")
    print(f"Loading config file: {args.config}")

    cfg = load_config(args.config)

    # Override algorithm if passed via CLI
    algorithm = args.algorithm if args.algorithm else cfg.get('algorithm', 'fifo')
    cfg['algorithm'] = algorithm
    print(f"Using algorithm: {cfg['algorithm']}\n")

    # Setup logs folder
    setup_logging(cfg['log_dir'])

    # Initialize Memory Manager
    mem_manager = MemoryManager(
        num_frames=cfg['num_frames'],
        algorithm=cfg['algorithm'],
        io_latency=cfg['io_latency'],
        log_dir=cfg['log_dir']
    )

    # Counters for statistics
    total_accesses = 0
    page_hits = 0
    page_faults = 0

    # Create and start threads for each process
    threads = []
    for p_cfg in cfg['processes']:
        proc = Process(p_cfg['pid'], p_cfg['sequence'], mem_manager)
        t = threading.Thread(target=proc.run)
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # After simulation, compute stats
    # MemoryManager already tracks page_faults; let's sum hits too
    for entry in mem_manager.access_log:
        total_accesses += 1
        if entry[2] == 'HIT':
            page_hits += 1
        else:
            page_faults += 1

    fault_rate = (page_faults / total_accesses) * 100 if total_accesses > 0 else 0

    # Summary print
    print("\n=== Simulation Summary ===")
    print(f"Total Memory Accesses : {total_accesses}")
    print(f"Page Hits             : {page_hits}")
    print(f"Page Faults           : {page_faults}")
    print(f"Page Fault Rate       : {fault_rate:.2f}%")

    # Write CSV logs
    mem_manager.write_logs(cfg['algorithm'])
    print(f"\nCSV logs written to folder: {cfg['log_dir']}")
    print("Simulation finished!\n")

if __name__ == "__main__":
    main()

