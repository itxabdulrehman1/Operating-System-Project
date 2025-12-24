# Operating-System-Project
#Virtual Memory Paging Simulator

#Operating System Project

#Project Overview

This project is a Virtual Memory Paging Simulator designed to demonstrate the core concepts of memory management in modern operating systems. The simulator models how virtual memory pages are mapped to physical memory frames, how page faults occur, and how page replacement policies affect system performance.

The project is developed as part of the Operating Systems course and serves as a working prototype that clearly illustrates paging behavior through simulation.

#Objectives

Simulate virtual memory paging

Demonstrate page faults

Implement page replacement algorithms

Visualize logical vs physical memory mapping

Provide hands-on understanding of OS memory management

#Features

Virtual address space simulation

Physical memory (frame) allocation

Page table management

Page fault detection

Page replacement strategy implementation

Modular and extensible design

Command-line based execution

#Technologies Used

Programming Language: Python 3

Concepts Applied:

Virtual Memory

Paging

Page Tables

Page Replacement Algorithms

Operating System Memory Management

#Project Structure
  virtual-memory-paging-simulator-full/
  │
  ├── src/
  │   ├── simulator.py        # Main simulator execution file
  │   ├── memory.py           # Memory and frame handling logic
  │   ├── page_table.py       # Page table implementation
  │   ├── replacement.py     # Page replacement algorithms
  │
  ├── README.md               # Project documentation
  ├── requirements.txt        # Python dependencies
  └── venv/                   # Virtual environment (optional)

#How to Run the Project
Step 1: Activate Virtual Environment (if used)
source venv/bin/activate

Step 2: Navigate to Project Directory
cd virtual-memory-paging-simulator-full

Step 3: Run the Simulator
python3 src/simulator.py

#Page Replacement Algorithms

The simulator supports basic page replacement logic and can be extended to include:

#FIFO (First In First Out)

#LRU (Least Recently Used)

#Optimal Replacement (future enhancement)

#Output Explanation

When executed, the simulator:

Displays page references

Indicates page hits and page faults

Shows memory frame allocation

Updates page table dynamically

This output helps understand how an operating system manages memory efficiently.

#Project Type

✅ Prototype Implementation

Fully functional simulation

Concept-focused design

Ready for academic demonstration

Can be extended into a full-scale system

#Limitations

No graphical user interface (CLI based)

Simplified memory model

Designed for learning and demonstration purposes

#Future Enhancements

Add GUI for visualization

Support multiple replacement algorithms selection

Performance comparison metrics

Real-time memory mapping graphs

#Learning Outcomes

Clear understanding of virtual memory

Practical exposure to OS memory management

Improved problem-solving in low-level system design

Experience in modular simulator development

#Author

Abdul Rehman
BS Computer Science – 4th Semester
Operating Systems Project

License

This project is developed for academic purposes only.
