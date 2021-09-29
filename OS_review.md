## lecture note

### Sep 08 Architectural Support for OS
- Kernel maintains a Process Control Block (PCB) for each process
    - holds page table and more
- PCB
    - maintained by kernel for each process
    - holds
        - page table
        - interrupt stack
        - process state 
            - new, ready, running, etc
        - PID
        - PC
- 'kernal is a library'
    - each process has 
        - user stack
        - interrupt stack / kernal stack (part of PCB)
    - kernel implemented using 'thread-based programming'
- types of signals
    - exceptions / faults
        - synchronous / non-maskable
        - process missteps, e.g. divided by zero
        - privileged instructions
    - syscalls
        - Synchronous / Non-maskable
        - User program requests OS service
    - device / I/O interrupts
        - Asynchronous / Maskable
        - HW (hardware?) device requires OS service
            - timer, I/O device, inter-processor, ...
            - An interrupt controller manages interrupts from multiple devices
- Interrupt handling
    - disables (“masks”) device interrupts 
        - at least interrupts of the same device
    - sets supervisor mode (if not set already)
    - pushes PC (IP), SP, PSW from before interrupt
    - pushes saved registers
    - sets PC (or kernal PC) to “signal handler”
        - depends on signal type
        - signal handlers specified in “interrupt vector” initialized during boot
    - pushes stack fram for handleSyscall()
- Reason for separating user SP / supervisor SP
    - user SP may be illegal
        - badly aligned or pointing to unwritable memory
    - user stack may be not be large enough and cause important data to be overwritten
        - might collide with heap 
    - user may use SP for other things than stack
    - security risks if only one SP
        -  kernel could push sensitive data on user stack and unwittingly leave it there (pop does not erase memory)
        – process could corrupt kernel code or data by pointing SP to kernel address
- Processor Status Word (PSW)
    - supervisor mode bit
    - interrupts enabled nit
    - condition codes
- return from interrupt instructions
    - hardware pops PC, SP, PSW
    - depending on content of PSW
        - switch to user mode
        - re-enable interrupts
- how kernal starts a new process
    - allocate and initialize a PCB
    - set up initial page table
    - push process arguments onto user stack simulate an interrupt
        - push initial PC, user SP
        - push PSW
    - clear all other registers
    - return-from-interrupt
- device registers
    - A device presents itself to the CPU as pseudo-memory
    - Devices define a range of device registers
    - can only read/write blocks, not words
- device drivers
    - a code module that deals with a particular brand/model of hardware device
    - all disk drivers have a common API
        - disk_init()
        - read_block()
- booting an OS
    - CPU starts at fixed address
        - in supervisor mode with interrupts disabled
    - IOS (in ROM) loads “boot loader” code from specified storage or network device into memory and runs it
    - boot loader loads O.S. kernel code into memory and runs it
- OS initialization
    - determine location/size of physical memory
    - set up initial MMU/page tables
    - initialize the interrupt vector
    - determine which devices the computer has 
        – invoke device driver initialization code for each
    - initialize file system code
    - load first process from file system  
    - start first process
- OC code architecture
    - user space
        - OS process
        - application process
    - kernal space ?
        - process management
        - user management
        - file systems
        - network protocols
        - memory management
        - device management
    - hardware-dependent code
        - boot/init
        - device driver

### Sep 10 Processes
- Process vs Program
    - program
        - code 
        - data
        - specified in some programming language
        - typically stored in a file on disk
    - executable   
        - a file containing
            - executable code
            - data
        - obtained by compiling a program and linking witn libraries
    - run program = create a process
    - process
        - executable running on an abstraction of a computer
        - Address Space (memory) 
        - Execution Context (registers incl. PC and SP)
            - manipulated through machine instructions 
        - Environment (clock, files, network, etc)
            - manipulated through system call
    - program is passive
    - process is alive
        - mutable data
        - registers
        - files
    - same program can be run multiple time simutaneosly
        - 1 program
        - 2 processes
- good abstraction
    - is portable and hides implementation details
    - has an intuitive and easy-to-use interface
    - can be instantiated many times 
    - is efficient to implement
- process memory
    - stack
        - grows down
    - heap
        - dynanmic memory allocation
        - grows up
    - data
        - global variables
    - text
        - read-only
        - code & constants
    - 0x00000000
        - unmapped
        - typecasted to a null pointer
- system call interface
    - 'skinny'
        - portability
            - easy to implement & maintain
        - security
            - 'small attack surface'
- process life cycle
    - INIT
        - PCB created
        - registers unitialized
    - RUNNABLE
        - PCB on run queue / ready queue
        - registers pushed by kernal code onto interrupt stack
    - RUNNING
        - PCB currently executing
            - might restore sp from PCB
        - popped from interrupt stack into CPU
    - WAITING
        - upon blocking calls
            - read()
            - wait()
        - PCB on specified waiting queue
        - registers on interrupt stack
    - FINISHED
        - PCB on finished queue, ultimately deleted
        - registers no longer needed
- invariants
    - at most 1 process running per core at any time
    - if CPU in user mode, 
        - current process is running
        - interrupt stack empty
    - if process RUNNING
        - PCB not on any queue
        - not necessarily in user mode
    - if process RUNNABLE / WAITING
        - interrupt stack non-empty
        - PCB either
            - on run queue (if runnable)
            - on wait queue (if waiting)
- cleaning up zombies
    - process cannot clean up itself
    - can be cleaned up by 
        - another process
            - check for zombies before returnning to RUNNING
        - by parent
        - by dedicated 'reaper' process
- context switches
    - interrupt
        - user -> kernal space
        - sys call, exception, interrupt
        - Px user stack -> Px interrupt stack
    - yield
        - between two processes
        - inside kernal
        - Px interrupt stack -> Py interrupt stack
    - return from interrupt
        - kernal -> user space
        - Py interrupt stack -> Py user stack
- context
    - registers
        - PC, SP, PSW
    - memory
        - code, heap, stack
- load
    - length of run queue
- time multiplexing vs space partitioning
    - CPU registers are time multiplexed
    - memory is space partitioned using MMU
        - sometimes also time multiplexed via paging & swapping
    - disk is space partitioned
- process vs thread abstraction
    - process
        - abstraction of a computer
            - CPU, memory, devices
        - own virtual memory
        - mutually distrusting
    - thread
        - abstraction of a core
            - registers
            - PC, SP
        - share virtual memory
        - mutually trusting
        - stack allocated on the heap
- implementations for threads
    - kernal-level threads
        - kernal knows about, schedules threads, just like processes
        - PCB for each thread
        - PCB
            - same page table base register
            - different PC, SP, registers, interrupt stack
        - simplify system call handling & scheduling
        - easy to implement
            - just processes with shared page table
        - can run blocking sys calls concurrently
        - 3 context switches for thread switch
    - user-level threads
        - real OS unaware of threads
        - single PCB
        - Thread Control Block (TCB) for each thread
        - more efficient than kernel-level threads
        - requires user-level context switches, scheuler
        - blocking sys call blocks all threads
        - need OS support for non-blocking sys calls
        - thread switch effiicently implemented in user space
- thread vs event based programming
    - event based
        - no blocking operations, e.g. read(), wait(), lock()
        - code is a collection of event handlers
            - invoked when some event haooens
            - runs to completion
        - good for I/O parallelism/GUIs
        - no context switch overhead
        - no locks needed
        - determinstic
        - It is hard to discern the control flow in an event-based program
        - Only one event handler can run at a time, so locks are unnecessary

    - thread-based
        - good fro any parallelism
        - keeps track of control flow
        - need locks
        - code easy to read
        - hard to debug
- shell foreground vs background
    - shell is either
        - reading fron standard input
        - waiting for a process to finishe 
    - others are background processes

### Sep 17 CPU scheduling
- CPU burst prediction
    - based on duration of the past bursts
    - exponential moving average
- job characteristics
    - arrival time
        - when job was first submitted
    - execution time
        - time needed to run task without contention
    - deadline
        - when task must have completed
    - total waiting time
        - = turnaround time - execution time
        - time on run queue but not running
    - response time
        - user-perceived time before first output
    - turnaround time
        - user-perceived time to complete some job
- performance terminology
    - throughput
        - rate at which jobs are completed
    - Predictability
        - how consistent?
        - low variance in turnaround time forr epeated jobs
    - overhead
        - time lost due to switching between jobs
    - fairness
        - equality in the resource given to each jonb
    - starvation
        - larck of progress for one job
        - due to resources given to higher priority jobs
    - envy free
        - no job wants to switch its schedule with another
    - maximize utilization / work conserving
        - keeps all devices busy
- context switch overhead
    - cost of saving registers
    - cost of schduler determining the next process to run
    - cost of restoring register
    - caches (L1, L2, TLB)
    - If the TLB is not tagged, then TLB flushing is one of the sources of context switch overhead
- generalization
    - priority scheduling
    - assign priority to each job
- priority inversion
    - some high priority process is waiting for some low priority process
        - e.g. for a lock
    - high priority process temporarily donates priority to lower priority process
- multi-core scheduling
    - desirables
        - balance load
            - each job gets approximately the same amount of CPU
        - scheudling affinity
            - avoid moving processes between cores
            - to avoid wasting cache content
        - avoid access contention on run queue
            - locking of run queue data structure
            - scalability
    - work stealing 
        - periodically balance load between cores
        - some loss for cache efficacy
- thread scheduling
    - gang scheduling
        - all threads of a process run together
        - good for CPU parallelism
    - space-based affinity
        - assign tasks to processors
            - e.g. pinki -> P1, P2
        - improve cache hit ratio
        - good for I/O parallelism

### Sep 22 Harmony and Critical Sections
- concurrent programming is hard
    - non-determinstic
    - program statements executed non-atomically
        - x += 1
            - LOAD x
            - ADD 1
            - STORE x
- race condition
    - timing dependent error involving shared state
    - some process accesses a data structure without obtaining a lock?
- ``await a``
    - means ``while not a: pass``
- harmony VM state
    - code
    - value of shared variables
    - state of each running process / context
        - name tag
        - PC
        - stack, implicit stack pointer
        - local variables
            - parameters
            - result
            - local vars declared in let & for statement
- critical sections in harmony  
    - ``@cs: assert atLabel.cs == dict{ nametag(): 1 };``
- interlock instructions
    - machine instructions that do multiple shared memory accesses atomically
    - e.g. TestAndSet(s, p)
        - try to set p to be s
        - s, p are pointers
        - p = old value of s
        - s = True
        - atomic
    - can have critical section with TAS
        - tas(?shared, ?private[self]) -> spinlock
        - at most one of all shared & private variables is False
        - private[i] = False ~ process i has the lock
- locks
    - ~ 'baton passing
    - at most one process, or shared, can be False
- spinlocks
    - work well when processes on different cores need to synchronize
- context switch in harmony
    - import synchS
    - r = stop list
        -  stops the current process and places its context at the end of the given list
    - go context r
        - adds a process with the given context to the bag of processes. 
        - Process resumes from stop expression
        - return r
at the end of the given list

### Oct 15 Deadlock
- deadlock
    - a set of processes
    - each is block
    - can become unblocked only be actions of another process
    - implies starvation (not vice bersa)
- deadlock prevention
    - Ensure that a necessary condition cannot hold
    - eliminate mutual exclusion / bounded resource 
        - make resource sharable without locks
            - non-blocking data structure
        - have sufficient resource available
            - unbounded queue
    - eliminate hold & wait
        - fine-grained locks
        - request all resources before execution begins
        - problems
            - probess don't know what they need ahead of time
            - starvation 
                - if waiting on many popular resources
            - low utilization 
                - need resource only for a bit
    - allow preemption
        - multiplex
        - ubdo/redo
    - eliminate circular waits
        - request resources in in creasing order
        - to request for R_j, first release all resources of type R_i, i < j
        - Havender's scheme
            - hierarchical resource allocation
            - H1
                - all resources from a given level must be acquired using a single request.
            - H2
                - After acquiring from level L_j must not acquire from L_i where i < j
            - H3
                - May not acquire from Li unless already released from Lj where j > i.

- deadlock avoidance
    - System does not allocate resources that will lead to a deadlock
    - state
        - allocation to each process
    - safe state
        - state from which some execution is possible that does not cause deadlock
        - Requires knowing max allocation for each process
        - exists seequene P_1, P_2, ..., P_n
            - for all i
            - P_i can be satisfied by avail resources held by P_1, ..., P_{i-1}
        - If a system is in a safe state at time T, it can always avoid being deadlocked at time T+1
- deadlock detection
    - Allow system to deadlock; detect it; recover
    - create a Wait-For Graph
        - 1 node per process
        - 1 edge per waiting process, from P to the process it's waiting for
        - graph holds for a single instant
        - cycle in graph indicates deadlock
        - reduction algorithm
            - Find a node with no outgoing edges
                - choice doesn't matter
                - Erase node
                - Erase any edges coming into it
            - graph remains -> deadlock
        - if no deadlock at T
            - cannot infer anything at T+x
            - next step could run process that request resource
            - cause deadlock
- deadlock recover
    - kill one/all deadlocked process
        - pick victim
        - terminate
        - repeat if needed
    - preempt resource/processes til deadlock broken
        - pick victim
        - rollback
- Banker's algorithm
    - proces declares its worst-case needs
    - ask for what it really needs
    - algotithm decides when to grant requests
        - build graph assuming request granted
        - reducible? grant
    - problems
        - fixed # of processes
        - need worst-case needs ahead of time
        - expensive

### Oct 22 Main Memory: Address Translation



### File System
- 

### Dec 3 Networking
- Basic Network Abstraction
    - A process can create “endpoints”
    - Each endpoint has a unique address • A message is a byte array
    - Processes can:
        - receive messages on endpoints 
        - sendmessagestoendpoints
    - Just another form of I/O
- protocol
    - Agreement between processes about messages
    - message
        - syntax
            - layout of bits, bytes, fields
        - semantics
            - what fields, messages mean
    - e.g.
        - HTTP 'get' requests and responses
- laying
    - application
        - exchanges nessages
        - HTTP, FTP, DNS
    - transport
        - transport messages
        - exchange segments
        - TCP, UDP
    - network
        - transport segments
        - exchange datagrams
        - IP, ICMP
    - link
        - transport datagrams
        - exchanges frames
        - Ethernet, WiFi
    - physical
        - transport frames
        - exchanges bits
        - wires, signal encoding
    - call them 'packets'
- modularity & abstraction
    - each layer
        - relies on service from layer below
        - exports services to layer above
- end-to-end argument
    - Application-specific properties are best provided by the applications
    - not the network
    - Internet performs best effort packet routing 
    - Higher-level applications do the rest
    - A check is necessary if nodes can fail.
- properties of a network connection
    - bandwidth
        - #bytes / second
    - latency 
        - How long does it take a bit to travel from one end to the other?
    - packet drop ratio
        - probability of packet loss
    - packet drop rate
        - #packets dropped / second
- Link layer: Local Area Networking (LAN) and Ethernet
    - each host has >= 1 NICs (Network Interface Cards)
    - each NIC has a MAC address
        - Media Access Control address
        - Ethernet example: b8:e3:56:15:6a:72 (48bits)
        - Unique to network instance
    - packet
        - header
            - destination address
            - source address
            - type
    - CSMA/CD
        - Carrier Sense
            - listen before you speak
        _ Multiple Access
            - mutliple hosts can access the network
        - Collision Detect
            - Detect and respond to cases where two hosts collide
    - Collision etection & Retransmission
        - The hosts involved in the collision stop data transmission, sleep for a while, and attempt to retransmit
        - sleep time: exponential back-off
        - abort after 16 retries
            - no guarantee that a packet will get to its destination
    - CRC checksum
        - hash function on teh packet
        - added to the end of a packet
        - detect malformed packet
- Network Layer
    - lots of Local Area Networks
    - each with their own 
        - address format
        - allocation shceme
        - packet format
        - LAN-level protocols, reliability guarantedes
    - Nodes with multiple NICs glue them together
    - standardize address and packet formats
    - -> WAN (wide-area network)
    - a complex system with simple components
    - Every NIC is assigned, and identified by, an IP address
        - NIC: Network Interface Card
        - IP: Internet Protocol
            - common address format
            - common packet format 
                - Specifies what packets look like
                - Fragments long packets into shorter packets
                - Reassembles fragments into original shape
            - IPv4 
                - what most applications use
                - 32 bit
                - e.g. 128.84.254.43
            - IPv6
                - more scalable and clears up some of the messy parts
                - 128 bit
                    - but only 64 functional bits
            - use IPv4 unless specified otherwise
    - network routes datagrams from the source NIC to the destination NIC
    - IP addressing
        - Each Internet Service Provider (ISP) owns a set of IP addresses
        - ISP assigns IP addresses to NICs
        - IP addresses can be re-used
        - same NIC may have different IP addresses over time
    - IP subnetting
        - an IP address consists of 
            - prefix of size n
            - suffix of size 32 - n
            - specified by an integer
                - e.g. 128.84.32.00/24 or 128.84.32/24
            - or netmask
                - 255.255.255.0 or 0xFFFFFF00 (in case n = 24)
        - A 'subnet' is identified by a prefix and has 2^{32-n} addresses
        - suffix of 'all zeroes' or 'all ones' reserved for broadcast
        - big subnets have a short prefix and long suffix
    - DHCP (dynamic host configuration protocol)
        - used to learn IP address and subnet mask (and more)
    - ARP (Address Resolution Protocol)
        - used to discover MAC addresses on same subnet
    - ARP and DHCP only scale to single subnet
    - Need more to scale to the Internet
- round trip time (RTT): 2 * latency
- bandwidth
    - number of lanes in the road
- latency
    - length of the road
- capacity  
    - bandwidth * latency   
- How long does it take to send a segment?
    - S 
        - size of segment in bytes
    - L
        - one-way latency in seconds
    - B
        - bandwidth in bytes per second
    - completion of receiving - start of sending
        - L + S/B
    - acknowledgment is received by the sender - start of the sending
        - 2L + S/B
    - end-to-end throughput without pipelining
        - S/(2L + S/B)
- how much data 'fits' in a pipe
    - bandwidth b
    - RTT r
    - ACK is a small message
    - can send b * r bytes before receiving an ACK for the first byte
- TCP congestion control
    - Additive-increase / multiplicative-decrease (AIMD)
    - window size++ every RTT if no packets dropped
    - window size/2 if packet drop
        - drop evident from the acknowledgement
    - slowly builds up to max bandwidth, and hover there
        - cons  
            - does not achieve the max possible
        - pros
            - shares bandwidth well with other TCP connections
    - TCP-friendliness
        - linear-increase
        - exponential backoff
        - in the face of congestion
- TCP fairness
    - if k TCP sessions share same bottleneck link of bandwidth R
    - each should have average rate of R/k
- TCP slow start
    - problem with AIMD
        - linear increase takes a long time to build up a window size that matches the link bandwidth * delay
        - most file transations are short
        - TCP spends a lot of time with small windows, never reaching large window size
    - Solution
        -  Allow TCP to increase window size by doubling until first loss
        - Initial rate is slow but ramps up exponentially fast
- TCP fast retransmit
    - Receiver detects a lost packet (i.e., a missing seq)
    - ACKs the last id it successfully received
    - Sender can detect the loss without waiting for timeout (uses 3rd duplicate ack)
- TCP summary
    - Reliable ordered message delivery 
        - Connection oriented, 3-way handshake
    - Transmission window for better throughput 
        - Timeouts based on link parameters
    - Congestion control
        - Linear increase, exponential backoff
    - Fast adaptation
        - Exponential increase in the initial phase








## OS: three easy pieces

### Chapter 2
- OS: the body of software that is responsible for making it easy to run programs (even allowing you to seemingly run many at the same time), allowing programs to share memory, enabling programs to interact with devices, etc.
- virtualization: the OS takes a physical resource (such as the processor, or memory, or a disk) and transforms it into a more general, powerful, and easy-to-use virtual form of itself. refer to the operating system as a virtual machine.
- Spin(i), a function that repeatedly checks the time and returns once it has run for i second
- file system: The software in the operating system that usually manages the disk

### Chapter 4 The Abstraction: The process
- process: a running program
- time sharing: allows users to run as many concurrent processes as they would like; the potential cost is performance, as each will run more slowly if the CPU(s) must be shared.
- space sharing: a resource is divided (in space) among those who wish to use it. e.g. disk space, a block is assigned to a file, it is not likely to be assigned to another file until the user deletes it
- context switch: stop running one program and start running another on a given CPU
- scheduling policy: given a number of possible programs to run on a CPU, which program should the OS run
- process abstraction
    - machine state
    - memory
        - address space
    - registers
        - PC
        - stack pointer
        - frame pointer
    - I/O information
        - a list of files the process currently has open
- program counter = instruction pointer = IP
- process API
    - Create
        - An operating system must include some method to create new processes. 
    - Destroy
        - As there is an interface for process creation, systems also provide an interface to destroy processes forcefully. Of course, many processes will run and just exit by themselves when complete; when they don’t, however, the user may wish to kill them, and thus an interface to halt a runaway process is quite useful.
    - Wait
        - Sometimes it is useful to wait for a process to stop running; thus some kind of waiting interface is often provided.
    - Miscellaneous Control
        - Other than killing or waiting for a process, there are sometimes other controls that are possible. For example, most operating systems provide some kind of method to suspend a process (stop it from running for a while) and then resume it (continue it running).
    - Status    
        - There are usually interfaces to get some status information about a process as well, such as how long it has run for, or what state it is in.
- C programs use the stack for local variables, function parameters, and return addresses
- heap: used for explicitly requested dynamically-allocated data; programs request such space by calling malloc() and free it explicitly by calling free()
- process states:
    - Running
        - In the running state, a process is running on a processor. This means it is executing instructions.
    - Ready
        - In the ready state, a process is ready to run but for some reason the OS has chosen not to run it at this given moment.
    - Blocked
        - In the blocked state, a process has performed some kind of operation that makes it not ready to run until some other event takes place
        - e.g. 
            - when a process initiates an I/O request to a disk
            - read from terminal
            - read from block not in cache
            - read from remote file server
            - it becomes blocked and thus some other process can use the processor
    - scheduled & descheduled

### Chap 5 Interlude: Process API
- process identifider = PID
- fork()
    - create almost exactly copy of the calling process
    - pid different from parent
    - comes into life as if it had called fork() itself.
    - while the parent receives the PID of the newly-created child, the child is simply returned a 0.
    - output non-determinstic
        - either parent or child could run first
- wait()
    - the parent process calls wait() to delay its execution until the child finishes executing.
    - When the child is done, wait() returns to the parent.
    - wait() won’t return until the child has run and exited
- exec()
    - useful when you want to run a program that is different from the calling program
    - given the name of an executable (e.g., wc), and some arguments (e.g., p3.c)
    - it loads code &s tatic data from that executable and overwrites its current code segment & current static data) with it
    - heap & stack & other memory re-initialized
    - transforms the currently running program (formerly p3) into a different running program (wc)
    - After the exec() in the child, it is almost as if p3.c never ran
    - a successful call to exec() never returns
    - does not create new process 
- shell
    - a user program
    - shows you a prompt
    - you type a command
    - shell calls fork, create new child process

### Chap 6 Mechanism: Limited Direct Execution
- user mode
    - restricted
    - a process can’t issue I/O requests in user mode
    - doing so would result in the processor raising an exception
    - the OS would then likely kill the process.
- kernal mode
    - unrestricted access to all hardware
    - which the operating system (or kernel) runs in
    - including privileged operations such as issuing I/O requests and executing all types of restricted instructions.
- system call
    - allow the kernel to carefully expose certain key pieces of functionality to user programs
    - such as accessing the file system, creating and destroying processes, communicating with other processes, and allocating more memory.
- To execute a system call
    - a program must execute a special trap instruction
    - This instruction simultaneously jumps into the kernel and raises the privilege level to kernel mode
    - once in the kernel, the system can now perform whatever privileged operations are needed (if allowed), and thus do the required work for the calling process.
    - When finished, the OS calls a special return-from-trap instruction
    - which returns into the calling user program while simultaneously reducing the privilege level back to user mode.
- hardware execute a trap
    - save enough of the caller’s register state in order to be able to return correctly when the OS issues the return-from-trap instruction
    - on x86, the processor will push the program counter, flags, and a few other registers onto a per-process kernel stack;
    - set up a trap table
        - so trap knows which code to run inside OS
        - when boots up, OS tells the hardware what code to run when certain exceptional events occur
        - The OS informs the hardware of the locations of these trap handlers
        - Once the hardware is informed, it remembers the location of these handlers until the machine is next rebooted
        - thus the hardware knows what to do (i.e., what code to jump to) when system calls 
- ![Limited direction execution protocol](images/sys_call.png)
    - priviledged instruction in bold
    - boot time
        - kernel initializes the trap table
        - the CPU remembers its location for subsequent use
    - running a process
        - kernel sets up a few things (e.g., allocating a node on the process list, allocating memory) before using a return-from-trap instruction to start the execution of the process
- each process has a kernel stack where registers (including general purpose registers & the program counter) are saved to and restored from (by the hardware) when transitioning into and out of the kernel.

- **switch between processes**
- cooperative approach: wait for sys call
    - OS trusts the processes that run for too long are assumed to periodically give up the CPU
    - yield system call: transfer control to the OS so it can run other processes.
    - Applications also transfer control to the OS when they do something illegal.
        - e.g. if an application divides by zero. or tries to access memory that it shouldn’t be able to access, it will generate a trap to the OS
        - OS will then have control of the CPU again, and likely terminate the offending process
- noncooperative approach: OS take control
    - timer interrupt:
        - A timer device can be programmed to raise an interrupt every so many milliseconds
        - when the interrupt is raised, the currently running process is halted, a pre-configured interrupt handler in the OS runs
        - OS could stop the current process, and start a different one
- saving and restoring context
    - To save the context of the currently-running process
    - OS will execute some low-level assembly code to save the general purpose registers, PC, and the kernel stack pointer of the currently-running process
    - then restore said registers, PC, and switch to the kernel stack for the soon-to-be-executing process. 
    - ![Limited direction execution protocol (Timer Interrupt)](images/timer_interrupt.png)
    - two types of register saves/restore
        - when the timer interrupt occurs
            - the *user register state* of the running process is implicitly saved by the *hardware*
            - saved by using the *kernel stack* of that process.
        - when the OS decides to switch from A to B
            - the *kernel register* state is explicitly saved by the *software* (i.e. the OS)
            - save into memory in the process structure (proc-struct) of the process.
- concurrency
    - OS might disable interrupts during interrupt processing

### Chap 7
- Jain's Fairness Index
    - fsairness metric
- turnaround time = completion time - arrival time
    - performance metric
- response time = first run time - arrival time
- FIFO 
    - if all jobs arriving at the same time
        - can be scheduled in any order
    - convoy effect
        - a number of relatively-short potential consumers of a resource get queued behind a heavyweight resource consumer. 
    - pros
        - simple
        - low overhead
        - no starvation
    - cons
        - average turnaround time sensative to schedule order
        - not responsive to interactive jobs
- SJF (shortest job first)
    - nonpreemptive
    - trouble when heavy jobs arrive first, suffer from convoy problem
    - pros
        - good turnaround time
        - optimal average turnaround time
    - cons
        - bad response time
        - pessimal variance in turnaround time
        - needs estimate of execution time
        - can starve long jobs
- EDF (earliest deadline first)
    - schedule in order of earliest deadline
    - does not need to know the execution times of the jobs
    - pros
        - meets deadlines if possible
        - free of starvation
    - cons
        - does not optimize other metrics
        - cannot decide when to run jobs without ddls
- preemptive scheduelrs
    - quite willing to stop one process from running in order to run another
- nonpreemptive
    - run each job to completion before considering whether to run a new job.
- SRTF (shortest remaining time first) / STCF (shortest time-to-completion first) / PSJF (Preemptive Shortest Job First 
    - SJF + preemption
    - Any time a new job enters the system / end of each quantum
    - it determines of the remaining jobs and new job, which has the least time left
    - then schedules that one
    - pros
        - good for response time and turnaround time of I/O-bound processes
        - low context switch overhead
    - cons
        - bad turnaround time and response time for CPU-bound processes
            - but don't really care
        - suffers from starvation
        - bad response time and interactivity
- (RR) round robin 
    - runs a job for a time slice /quantum 
    - then switches to the next job in the run queue.
    - next job is one on the run queue
        - that hasn't run for the longest time
        - a new job hasn't long for an infinite amount of time (?)
    - the length of a time slice must be a multiple of the timer-interrupt period
        - if the timer interrupts every 10 milliseconds, the time slice could be 10, 20, or any other multiple of 10 ms.
    - good quantum size
        - typical
            - 100X cost of context switch
        - longer time slice 
            - morphs into FIFO
        - shorter time slice
            - better response time
            - cost of context switching large
            - need to make it long enough to amortize the cost of switching
    - pro
        - no starvation
        - can reduce response time
        - fair
    - con
        - bad average turnaround for equal length jobs
        - context switch overhead
        - mix of I/O and CPU bound not fair for I/O task

- incorporating I/O
    - the currently-running job won’t be using the CPU during the I/O; it is blocked waiting for I/O completion.
- cost of context switching
    - program builds up a great deal of state in CPU caches, TLBs, branch predictors, and other on-chip hardware
    - switching to another job causes this state to be flushed 
    - new state relevant to the currently-running job to be brought in
- I/O
    - the currently-running job won’t be using the CPU during the I/O
    - it is blocked waiting for I/O completion.
- STCF
    - treats each CPU burst as a job, the CPU being used by one process while waiting for the I/O of another process to complete

### Chap 8
- MLFQ (Multi-level feedback queue)
    - optimize turnaround time and response time
- has a number of distinct queues, each with a different priority level
- a job on a higher queue is chosen to run
- use round-robin scheduling among jobs on the same queue
- varies the priority of a job based on its observed behavior
- approximates SRTF

- If a job repeatedly relinquishes the CPU while waiting for input from the keyboard 
    - MLFQ will keep its priority high, as this is how an interactive process might behave
- If a job uses the CPU intensively for long periods of time
    - MLFQ will reduce its priority.
- it first assumes it might be a short job, thus giving the job high priority.
- Rules
    - Rule 1: If Priority(A) > Priority(B), A runs (B doesn’t).
    - Rule 2: If Priority(A) = Priority(B), A & B run in RR.
    - Rule 3: When a job enters the system, it is placed at the highest priority (the topmost queue).
    - Rule 4a: If a job uses up an entire time slice while running, its priority is reduced (i.e., it moves down one queue).
    - Rule 4b: If a job gives up the CPU before the time slice is up, it stays at the same priority level.
    - -> Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced 
        - whether it uses the time slice in one long burst or many small ones does not matter
    - Rule 5: After some time period S, move all the jobs in the system to the topmost queue.
    - lower priority, longer quantum
- problems:
    - starvation: if there are “too many” interactive jobs in the system, they will combine to consume all CPU time
    - a smart user could rewrite their program to game the scheduler
        - perform better accounting of CPU time at each level of the MLFQ; the scheduler should keep track, how much of a time slice a process used at a given level
    - a program may change its behavior over time; what was CPU-bound may transition to a phase of interactivity.
    - -> rule 5

### Chap 9 Scheduling: Proportional Share
- proportional share / fair-share scheduler
- guarantee that each job obtain a certain percentage of CPU time.

### Chap 10 Multiprocessor Scheduling
- multicore processpor
    - multiple CPU cores packed onto a single chip
- write programs run in parallel, using threads
    - spread work across multiple CPUs and thus run faster when given more CPU resources
- cache affinity
    - a process, when run on a particular CPU, builds up a fair bit of state in the caches (and TLBs) of the CPU
    - The next time the process runs, it is often advantageous to run it on the same CPU
    - otherwise, the performance of the process will be worse, as it will have to reload the state each time it runs 
- single-queue scheduling (SQMS)
    - advantage
        - simplicity
    - disadvantage
        - lack of sacalability
            - to work correctly on multiple CPUs, need locking
            - increase contention for a single lock, as CPUs increases
        - cache affinity
            - each job could end up bouncing around from CPU to CPU
            - but could provide affinity for some jobs, but move others around to balance load
- multi-queue schedling (MQMS)
    - each queue follow a particular scheduling discipline, e.g. RR
    - when a job enters the system, it is placed on one scheduling queue, according to some heuristic (e.g., random, pick one with fewest jobs
    - advantage
        - more scalable
            - more CPUs, more queues
        - provide cache affinity
            - job stays on the same CPU
    - disadvantage
        - load imbalance
            - could do migration, move one job from a CPU to another
        - work stealing
            - a (source) queue that is low on jobs will occasionally peek at another (target) queue, to see how full it is.
            - source queue could steal to help balance load
            - but peeking would result in high overhead

### Chap 26
- each thread is very much like a separate process, except that they share the same address space and thus can access the same data.
- Each thread has its own private set of registers it uses for computation
- The context switch between threads is quite similar to the context switch between processes, as the register state of T1 must be saved and the register state of T2 restored before running T2
- With processes, we saved state to a process control block (PCB)- now, we’ll need one or more thread control blocks (TCBs) to store the state of each thread of a process. 
- in the context switch of threads: the address space remains the same (i.e., there is no need to switch which page table we are using).
- one stack per thread
- race condition: the results depend on the timing execution of the code.
- critical section: a piece of code that accesses a shared variable 
- mutual exclusion: if one thread is executing within the critical section, the others will be prevented from doing so.
- indeterminate: program consists of one or more race conditions; the output of the program varies from run to run, depending on which threads ran when.

### Chap 27
- condition variables: useful when some kind of signaling must take place between threads, if one thread is waiting for another to do something before it can continue
- pthread cond wait(): puts the calling thread to sleep, and thus waits for some other thread to signal it, usually when something in the program has changed that the now-sleeping thread might care about
```

Pthread_mutex_lock(&lock); 
while (initialized == 0)
    Pthread_cond_wait(&init, &lock);
Pthread_mutex_unlock(&lock);
...
Pthread_mutex_lock(&lock); 
initialized = 1; 
Pthread_cond_signal(&init); 
Pthread_mutex_unlock(&lock);
```
- wait call takes a lock as its second parameter, whereas the signal call only takes a condition. The reason for this difference is that the wait call, in addition to putting the calling thread to sleep, releases the lock when putting said caller to sleep.
- before returning after being woken, the pthread cond wait() re-acquires the lock

### Chap 28
- Test and set (atomic exchange)
    - correctness problem: with timely interrupts, could produce a case where both threads set their flags to 1 and both threads are thus able to enter the critical section.
    - performance problem: it endlessly checks the value of flag, a technique known as spin-waiting. Spin-waiting wastes time waiting for another thread to release a lock.
- working spin lock
    - 
    ```
    TestAndSet(int *ptr, int new) {
        int old = *ptr; // fetch old value at ptr 
        *ptr = new; // store ’new’ into ptr 
        return old; // return the old value
    ```
    - perfomed atomically
    - 
    ```
    void lock(lock_t *lock) {
        while (TestAndSet(&lock->flag, 1) == 1)
        ; // spin-wait (do nothing)
    }
    ```
    - requires a preemptive scheduler (i.e., one that will interrupt a thread via a timer, in order to run a different thread, from time to time).
- evaluating spin locks
    - spin locks don’t pro- vide any fairness guarantees. Indeed, a thread spinning may spin forever, under contention. Spin locks are not fair and may lead to starvation.
    - performance
        - wasteful on single CPU, the thread holding the lock is pre-empted within a critical section. The scheduler might then run every other thread (imagine there are N − 1 others), each of which tries to ac- quire the lock.
        - works reasonably well on multi-CPU, Thread A on CPU 1 and Thread B on CPU 2, both contending for a lock. If Thread A (CPU 1) grabs the lock, and then Thread B tries to, B will spin (on CPU 2)
- compare and swap
```
int CompareAndSwap(int *ptr, int expected, int new) { int actual = *ptr;
    if (actual == expected)
        *ptr = new; 
    return actual;
...
void lock(lock_t *lock) {
    while (CompareAndSwap(&lock->flag, 0, 1) == 1)
    ; // spin
```
- load-linked & store-conditional
    - store-conditional only succeeds (and updates the value stored at the address just load-linked from) if no intermittent store to the address has taken place.
- fetch-and-add
    - when a thread wishes to acquire a lock, it first does an atomic fetch-and-add on the ticket value; that value is now considered this thread’s “turn”
    - Unlock is accomplished simply by incrementing the turn such that the next waiting thread (if there is one) can now enter the critical section.
    - ensure progress for all threads
- yield
    -  when you are going to spin, instead give up the CPU to another thread.
    -
    ```
    void lock() {
        while (TestAndSet(&flag, 1) == 1)
                yield(); // give up the CPU
    }
    ```
- use queues: sleeping instead of spinning
    - park() puts a calling thread to sleep
    - unpark(threadID) wakes a thread
- two-phase lock

### Chap 30
- condition variable
    - an explicit queue that threads can put themselves on when some state of execution (i.e., some condition) is not as desired (by waiting on the condition);
    - some other thread, when it changes said state, can then wake one (or more) of those waiting threads and thus allow them to continue (by signaling on the condition)
- wait()
    - executed when a thread wishes to put itself to sleep
    - release the lock and put the calling thread to sleep (atomically)
    - when the thread wakes up (after some other thread has signaled it), it must re-acquire the lock before returning to the caller
- signal() 
    - executed when a thread has changed something in the program and thus wants to wake a sleeping thread waiting on this condition.
- producer-consumer (bound buffer) problem
    - Producers produce data items and wish to place them in a buffer
    - consumers grab data items out of the buffer consume them in some way
    - mesa sementics    
        - Signaling a thread only wakes them up; it is thus a hint that the state of the world has changed (in this case, that a value has been placed in the buffer), but there is no guarantee that when the woken thread runs, the state will still be as desired.
    - hoare semantics
        - provides a stronger guarantee that the woken thread will run immediately upon being woken
    - use two cv
        - producer threads wait on the condition empty, and signals fill
        - figure 30.10
    - covering codition
        - covers all the cases where a thread needs to wake up (conservatively);
        - pthread cond signal() call in the code above with a call to pthread cond broadcast(), which wakes up all waiting threads.

### Chap 31
- binary semaphores (locks)
    - initial value is 1
    - scheduler states: running, ready, sleeping
- semaphore as cv
    - inital value set to 0
    - The parent runs, decrements the semaphore (to -1), then waits (sleeping). When the child finally runs, it will call sem post(), increment the value of the semaphore to 0, and wake the parent
- producer/consumer 31.8
- reader-writer lock figure 31.9
    - would be relatively easy for readers to starve writers.
- dining philosopher
    - need to break the dependency

### Chap 13
- stack: function call chain, allocate local variables and pass parameters and return values to and from routines
- heap: dynamically-allocated, user-managed memory
- goal of virtual memory
    -  transparency
        - OS should implement virtual memory in a way that is invisible to the running program
        - the program shouldn’t be aware of the fact that memory is virtualized
    - efficiency
        - time: not making programs run much more slowly
        - space: not using too much memory for structures needed to support virtualization
    - protection
        - should not be able to anything outside its address space

### Chap 14
- segmentation fault: forget to allocate memory
- buffer overflow: not allocatung enough memory
- uninitialized read: forget to initialize allocated memory
- memory leak: forget to free memory
- dangling pointer: free memory before you are done with it
- double free: freeing memory repeatedly
- invalid frees: calling free() incorrectly, we can only free pointers received from malloc earlier

### Chap 15
- hardware-based address translation
    - hardware changes the virtual address to physical address
- dynamic (hardware-based) relocation
    - base and bounds
    - two hardware registers with each CPU
        - base register
        - limit register (bounds)
- issues
    - The OS must take action when a process is created, finding space for its address space in memory.
    - the OS must take action when a process is terminated, reclaiming all of its memory for use in other processes or the OS.
    - the OS must also take action when a context switch occur
        - must save the values of the base and bounds registers to memory, in process control block (PCB).

### Chap 16 Segmentation
- place each segment (code, heap, stack) independently in physical memory.
- external fragmentation
    -  physical memory quickly becomes full of little holes of free space, making it difficult to allocate new segments
- internal fragmentation
    - if an allocator hands out chunks of memory bigger than that requested
    - any unused space in such a chunk is considered internal fragmentation

### Chap 17 Free-Space Management
- splitting and coalescing
    - splitting
        - find a free chunk of memory that can satisfy the request and split it into two
    - coalescing
        - if the newly-freed space sits right next to one/two existing free chunks, merge them into a single larger free chunk
- header
    - contains size of the allocated region & other information
- strategies
    - best fit
        - find chunks of free memory that are as big or bigger than the requested size
        - return the one that is the smallest in that group of candidates
        - naive implementations pay a heavy performance penalty when performing an exhaustive search for the correct free block
    - worst fit
        - leave big chunks free instead of lots of small chunks
        - leading to excess fragmentation
    - first fit
        - finds the first block that is big enough and returns 
        - pollutes the beginning of the free list with a small objects
        - address-based ordering: keep the list ordered by the address of the free space, coalescing becomes easier
    - next fit
        - keeps an extra pointer to the location within the list where one was looking last
        - spread the searches for free space throughout the list more uniformly
- segregated list
    - keep a separate list just to manage objects of a particular size
    - when the kernel boots up, it allocates a number of object caches for kernel objects that are likely to be requested frequently 
    - When a given cache is running low on free space, it requests some slabs of memory from a more general memory allocator
- (binary) buddy allocation
    - recursively divides free space by two until a block that is big enough to accommodate the request is found 
    - When returning the 8KB block to the free list, the allocator checks whether the “buddy” 8KB is free; if so, it coalesces the two blocks into a 16KB block.
    - address of each buddy pair only differs by a single bit
    - suffer from internal fragmentation
- lack of scaling
    - searching list slow
    - -> use more complex data structures

### Chap 18 Paging
- split virtual space into pages
- physical memory: page frame
- page table
    - per process data structure
    - store address translations for each of the virtual pages of the address space
- inverted page table: not per-process
- virtual address + virtual page number + offset
- offset just tells us which byte within the page we want
- store page table for each process in memory
- page table entry contains valid bit, protection bit, present bit (indicating whether this page is in physical memory or on disk (swapped out)), reference/access bit track whether a page has been accessed
- a single page-table base register contains the physical address of the starting location of the page table

### Chap 19 Paging: Faster Translations (TLBs)
- translation-lookaside buffer (TLB)
    - part of MMU (memory-management unit)
    - a hardware cache of popular virtual-to-physical address translations
- Upon each virtual memory reference, the hardware first checks the TLB to see if the desired translation is held therein
- hardware-managed TLB
    - if TLB miss
        - hardware accesses the page table to find the translation
        - updates the TLB with the translation
        - the hardware retries the instruction
    - hardware would handle the TLB miss entirely
- software-managed TLB
    - flexible
        - OS can use any data structure it wants to implement the page table
    - simple
        - TLB control flow
    - TLB miss
        - the hardware raises an exception
        - which pauses the current instruction stream
        - raises the privilege level to kernel mode 
        - jumps to a trap handler
        - trap handler is code within the OS, written with the express purpose of handling TLB misses
- return-from-trap
    - in syscall
        - resume execution at the instruction after the trap into the OS
    - in TLB miss-handling trap
        -  resume execution at the instruction that caused the trap
- OS needs to be careful not to cause an infinite chain of TLB misses to occur when running TLB miss-handling code
    - keep TLB miss handlers in physical memory, not subject to address translation
- protection bits
    - code pages: read & execute
    - heap pages: read and write
- TLB issue: context switch
    - flush the TLB on context switches
    - on software-based TLB
        - accomplished with privilegded hardware instruction
    - on hardware-based TLB
        - flush done when the page-table base register changed
    - some system supposrt sharing of TLB across context switches
        - manage address space identifier (ASID)
        
### Chap 20 Paging: smaller tables
- big page
    - waste within each page
    - internal fragmentation
- page directory
    - tell you where a page of the page table is
    - or that the entire page of the page table contains no valid pages
    - page directory entry, contains valid bit and page frame number
    - if PD entry valid, at least one of the pagers of the page table that the entry points to is valid
- advantage
    - compact; 
    - supports sparse address space; 
    - only allocates page-table space in proportion to the amount of address space you are using
    - each portion of the page table fits neatly within a page; easy to manage memory; 
    - otherwise, entire linear page table must reside contiguous in physical memory
- VPN = page directory index + page table index
- inverted page table
    - keep a single page table that has an entry for each physical page of the system
    - tells which process is using the page
    - and which virtual page of that process maps to this physical page
    - multiple processes can share the same segment
- swapping page tables to disk
    - some systems place large page tables in kernel virtual memory
    - allowing the system to swap some of these page tables to disk when memory pressure gets a little tight

### Chap 21: Beyond physical memory: mechanisms
- swap space
    - some space on the disk reserved for moving pages back and forth
    - swap pages out of memory to it and swap pages into memory from it
- page fault
    - when translating VPN
    - accessing a page that is not in physical memory is commonly referred to as a page fault
    - -> page-fault handler, handled in software/OS
    - looks in PTE to find address, issue request to disk to fetch page
    - update page table to mark page as present
    - retry the instruction, may still generate a TLB miss
    - process in blocked state, OS free to run other ready process
- if memory full
    - page replacement policy
- page fault control flow
    - if access to an invalid page
    - hardware traps the invalid access
    - OS trap handler runs, terminating the process
- when replacement occurs
    - when OS notice thag fewer than LW (low watermark) pages available
    - background thread (swap/page daemon) evicts pages until there are HW (high watermark) pages available

### Chap 22: Beyond Physical Memory: Policies
- cold-start miss / compulsory miss: first couple accesses
- policy
    - FIFO
    - random
    - LRU
    - LFU
- 80-20 workload
    - 80% of the references are made to 20% of the pages (the “hot” pages)
- clock algorithm: approxinating LRU
    - use bit
        - Whenever a page is referenced (read / written), the use bit is set by hardware to 1
        - clock hand points to some particular page to begin with (doesn’t matter which)
        - checks if current-pointed to page has use bit 1 or 0
            - if 1, set use bit to 0, move to next
            - else, use that slot
- modified bit
    - must be written back to disk to evict it
- page selection policy
    - OS decides when to bring a page into memory
- demand paging
    - OS brings the page into memory when it is accessed
    - "on demand"
- prefetching
    - OS guess that a page is about to be used
    - bring it in ahead of time
- thrashing
    - constantly be paging
    - when memory is simply oversubscribed
    - the memory demands of the set of running processes simply exceeds the available physical memory
    - could not to run a subset of processes, fit working sets into memory

### Chap36 I/O Device
- simplified device interface
    - status register: see current status of the device
    - command register: tell the device to perform a certain task
    - data register: pass data to the device,
- protocal
    - polling: OS waits until the device is ready to receive a command by repeatedly reading the status register; polling the device 
    - OS sends some data down to the data register;
    - OS writes a command to the command register; 
        - implicitly lets the device know that the data is present
    - OS waits for the device to finish by again polling it in a loop, waiting to see if it is finished 
    - wastes a great deal of CPU time just waiting for the device to complete activity
- Lowering CPU Overhead With Interrupts
    - OS can issue a request, put the calling process to sleep, and context switch to another task
    - When the device is finally finished with the operation, raises a hardware interrupt
    - causing the CPU to jump into the OS at a pre-determined interrupt service routine (ISR) / interrupt handler
    - handler reads data / an error code from the device
    - wake the process waiting for the I/O
- problem
    - poll & interrupt
        - possible that the first poll usually finds the device to be done with task
        - if a device is fast,  poll
        - if it is slow, interrupts
        - hybrid
            - polls for a little while and then
            - if the device is not yet finished, uses interrupts.
    - networks
        - livelock
            - find itself only processing interrupts and never allowing a user-level process to run 
        - better occasionally use polling
    - optimization: coalescing
        - multiple interrupts can be coalesced into a single in- terrupt delivery
- Efficient Data Movement 
    - when using programmed I/O (PIO) to transfer a large chunk of data to a device
    - CPU used on a trivial task
    - Direct Memory Access (DMA)
        - very specific device that can orchestrate transfers between devices and main memory without much CPU intervention
- Methods Of Device Interaction
    - oldest method: have explicit I/O instructions
        - privileged instructions
    - memory-mapped I/O
        - hardware makes device registers available as if they were memory locations
        - OS issues a load (read) or store (write) the address
        - hardware then routes the load/store to the device instead of main memory

### Chap 27 hard disk drives
- interface
    - drive consists of a large number of sectors (512-byte blocks)
    - each of which can be read or written.
    - sectors are numbered from 0 to n − 1 on a disk with n sectors
- basic geometry
    - platter
    - a circular hard surface on which data is stored persistently by inducing magnetic changes to it
    - each platter has 2 sides/surface
    - platters are all bound together around the spindle, which is connected to a motor that spins the platters around 
    - Data is encoded on each surface in concentric circles of sectors; call such concentric circle a track
    - each sector has 512 bytes
    - disk head: do read/write, one head per surface
    - disk wait for the desired sector to rotate under the disk head-- rotational delay
    - full rotation delay: time needed to rotate one circle
- multiple tracks
    - seek: moving the disk arm to the correct track
        - acceleration: disk arm gets moving
        - coasting: moving at full speed
        - deceleration: arm slows down
        - settling: head carefully positioned over the correct track; settling time
    - transfer: data read/written
    - track skew
    - multi-zoned disk drives: disk is organized into multiple zones; zone is consecutive set of tracks on a surface.
    - cache/track buffer
        - when reading a sector from the disk
        - the drive might decide to read in all of the sectors on that track and cache them in its memory 
- I/O time
    - T_I/O = T_seek + T_rotation + T_transfer
    - rate of I/O = size_transfer/T_I/O
    - random workload: reads to random locations on the disk
    - sequential workload: reads a large number of sectors consecutively
- disk scheduling
    - SSTF: shortest seek time first
        - orders the queue of I/O requests by track
        - picking requests on the nearest track to complete first
        - problems
            - drive geometry is not available to the host OS
            - starvation
    - Elevator / SCAN / C-SCAN
        - simply moves across the disk servicing requests in order across the tracks
        - sweep: a single pass across the disk
        - F-SCAN
            - freeze the queue when doing a sweep
            - places re- quests that come in during the sweep into a queue to be serviced later
            - avoids starvation of far-away requests
        - C-SCAN
            - sweeps outer -> inner, inner -> outer
        - problem
            - ignores rotation
    - SPTF: shortes positioning time first / shortest access time first (SATF)
        - depends on seeking time and rotational delay
        - e.g. if seek faster than rotation
            - then should seek further, go to the furthest track
- other scheduling issues
    - I/O merging
        - merge the requests for blocks 33 and 34 into a single two-block request
    - anticipatory disk scheduling
        - By waiting, a new and “better” request may arrive at the disk
        - overall efficiency is increased

### Chap 38: Redundant Arrays of Inexpensive Disks (RAIDs)
- use multiple disks in concert to build a faster, bigger, and more reliable disk system
- properties
    - transparency
    - redundancy
    - deployability
- fault model
    - disk either working for failed
    - if failed, assume it's easily detected, then permanently lost
- sequential access S MB/s
    - disk operates in its most efficient mode
    - spending little time seeking and waiting for rotation and most of its time transferring data
- random access R MB/s
    - opposite
- number of disks: N
- RAID 0: Striping
    - spread blocks across the disks in a round-robin fashion
    - extract the most parallelism from the array when requests are made for contiguous chunks of the array
    - stripe: blocks in the same row, each one partition of it contains a chunk
    - chunk size: size of blocks placed on each disk before moving onto next
        - small chunk 
            - many files will get striped across many disks
            - increase parallelism
        - big chunk
            - relies on multiple concurrent requests to achieve high throughput
            - reduce positioning time: just the positioning time of less disks
    - latency 
        - r
    - sequential access
        - N * S
    - random access
        - N * R

- RAID 1: mirroring
    - make more than one copy of each block

- RAID-10
    - use mirrored pairs (RAID-1) then stripes (RAID-0)
    - useful capacity
        - N/2
    - reliability
        - 1 failure of any disk
        - N/2 if lucky
    - latency
        - read: r (same as that of a single disk)
        - write: r (parallel)
            - average higher than write to a single disk bc worst-case seek and rotational delay
    - sequential
        - write N*S/2
            - half of peak bandwidth when parallel
        - read N*S/s
            - disk reads 0, then 4, skipping 2, each disk receives a request for every other block
    - random 
        - write N*R/2
        - read N*R

- RAID 4: saving space with parity
    - P = XOR of all bits
    - invariant:  number of 1’s in any row must be an even number (adding the parity bit)
    - useful capacity
        - N-1
    - reliability
        - 1
    - latency
        - read r
        - write 2r
    - sequential
        - read
            - (N-1) * S
        - write
            - full stripe write: write all blocks in a stripe
            - (N-1) * S
    - random
        - read
            - (N-1)*R
        - write
            - R/2
            - two reads and two writes
            - small write problem: if two requests, need to read from parity disk at the same time
    
- RAID 5: rotating parity
    - same as above for effective capacity, failure toleracne, sequential
    - random
        - read
            - a bit better, can uilize all disks
        - write
            - N*R/4
- - ![RAID](images/raid.png)

### Chap 39: File and Directories
- hard links
    - when linking a new file name to old one -> create another way to refer to the same file
    - file is not copied
    - reference count / link count: track how many different file names have been linked to this particular inode
    - if reference count reaches 0, file system frees the inode and related data blocks
    - can't create hard link to a directory, in case creating a cycle
    - can't hard link to files in other disk partitions, bc inode number unique within a file system
- symbolic link / soft link
    - third type of the file system beyond file and directory, - for files, d for directory, l for soft link 
    - could have dangling reference: pointing to a pathname that no longer exists

### Chap 40: File System Implementation
- divided disk into blocks, common size 4kb
- data region: region used for data
- metadata: tracks things like which data blocks comprise a file, the size of the file, its owner and access rights
- inode table: holds an array of inodes
- bitmap
    - data bitmap and inode bitmap
    - track whether inodes/data blocks are free or allocated
- superblock
    - contains information about this particular file system
    - e.g. how many inodes and data blocks are in the file system
    - when mounting a file system, OS will read superblock first
- disk is not byte addressable, but in larger number of adddressable sectors, usually 512 bytes
- inode = index node
    - inode table = superblock + i-bmap + d-bmap + iblocks
    - each inode contains file type, size, num of blocks, identifier of owner allocated to it
    - contains direct pointers / disk addresses
    - indirect pointer
        - point to a block containing pointers
        - double indirect pointer
            - refers to a block that contains pointers to indirect blocks
    - most files are small
- read file from disk
    - open "/foo/bar"
    - read inode (#2) of the root directory
    -  look inside of it to find pointers to data blocks, which contain the contents of the root directory; by reading 1(+) blocks directory data blocks, find entry for foo & inode number
    - read the block containing inode for foo
    - read foo directory data, find entry for bar
    - read inode for bar
    - read first block of the file and so on
    - may update inode with a latest accessed time
- write to disk
    - may allocate a block
        - each write has 3 I/O
        - read data bitmap
        - write the bitmap
        - write to the actual block
    - create a file
        - allocate inode
        - allocate space within directory
        - I/O
            - read inode bitmap, find a free inode
            - write to inode bitmap
            - write to the new inode, initialize it
            - write to the data of the directory, link the high-level name of the fiel to its inode number
            - read and write to the directory inode to update
            - if directory needs to grow, need additional I/O needed
                - e.g. to data bitmap
                - new directory block
- caching and buffering
    - use system memory (DRAM) to cache important blocks
    - fixed-size to hold popular blocks
    - subsequent file opens of the same file hits the cache
    - write buffering
        - delay writes, batch some updates into a smaller set of I/Os
        - if buffer writes, then can schedule subsequent I/O, increase performance
            - e.g. if create a file then deletes it, can avoid

### Chap 41: Locality and the Fast File System
- FFS divide disk into cylinder groups / block groups
    - place two files within the same group -> no long seeks across disk when accessing one after another
    - super block in each group -> reliability
- policies: how to allocate files & directories
    - directory
        - find cylinder group with low number of allocated directories & high number of free inodes
            - balance dir across groups
    - files
        - allocate data blocks of a file in the same group as its inode
        - allocate files in the ame directory in the cylinder group fo the directory they are in
- large-file exception
    - divide into chunks, spread them across groups
    - if chunk size large enough
        - will spend most time transferring data from dist
        - little time seeking between chunks

### Chap 42: Crash consistency: FSCL and Journaling
- file system data structure must persist
    - stored on devices that retain data despite power loss 
- file system checker (fsck)
    - let inconsistencies happen
    - then fix them later when rebooting
    - run before file system is mounted
    - procedure
        - first checks superblock
        - free blocks: scans inodes, indirect blocks etc 
            - build an understanding of which blocks are allocated
            - produce correct version of bitmaps
        - inode state
        - inode links
        - duplicates
        - bad blocks
        - directory checks
    - problem
        - too slow
- journaling / write-ahead logging
    - physical logging
        - putting the exact contents in journal
    - contains
        - TxB transaction begin
            - final addresses of following blocks
            - transaction identifier (TID)
        - content of blocks
        - TxE end of transation
            - TID
    - checkpointing
        - write the pending metadata and data updates to their final locations in the file system.
    - to avoid problem with crashing during writes to journal
        - first write all except for TxE
        - write TxE
        - procedure
            - journal write
                - write TxB, metadata, data
            - journal commit
                - write transaction commit block, containing TxE
            - checkpoint
                - write content of the update to final on-disk locations    
- recovery
    - if crash happens before transaction written to log
        - update ignored
    - if crash after transaction commited
        - replay transaction

### Chap 43: log-structured file system
- observations
    - Memory sizes were growing
    - large and growing gap between random sequential I/O performance
    - Existing file systems perform poorly on many common workloads
        - e.g. large number of writes to create a new fuke
    - file systems were not RAID-aware
- LFS log-structured file system
    - uffers all updates in an in- memory segment
    - written to disk in one long sequential transfer if buffer full
    
## Harmony

## Chap 5 Critical Sections
- thread-safe 
    - implementation of a data structure that can be safely accessed by multiple processes (or threads) and free of race conditions
- mutual exclusion
    - @cs: assert atLabel.cs == dict{nametag():1}
    - atLabel: returns a bag of name tags of processes executing at that label
- progress/liveness
    - processes trying to enter cs
    - processes in cs leave eventually
- while choose({False, True})
    - a process can choose to enter a critical section more than once
    - can also choose to terminate, even without entering the critical section ever
- It is possible to implement critical sections without interlock instructions

## Chap 6 Peterson's Algorithm
- A process first indicates its interest in entering the critical section by setting its flag
- It then politely gives way to the other process should it also want to enter the critical section
- waiting until either the other process is nowhere near the critical section (flag[1 − self ] == False) or has given way (turn == self )
- nondeterminism
    - choose
    - more than q process can take a step
- reachable
    - initial state 
    - or it can be reached from the initial state through a trace.
- exclusive state
    - at most 1 process in the critical section
- invariant
    - a predicate that holds over all states reachable
- inductive invariant I 
    - I holds in the initial state
    - for any state in which I holds, for any process in the state, if the process takes a step, I also holds in the resulting sttae
    - also holds over unrechable states
    - base case
        - holds if in initial state
        - if holds in S, then also holds in any state reachable from S in one step
- exclusivity is an invariant, but not an inductive invariant
- C(i) = \not flags[1-i] \cup turn = i, condition on await
- I_p(i) = process(i)@cs => C(i) \cup process(1-i)@gate
- inductive invariant: I(0) \cap I(1)
- reachable states \subset states where inductive invariant hold \subset states where mutual exclusion holds

## Chap 8 Spinlock
- interlock instruction
    - special machine instructions that can read memory and then write it in an indivisible step
- test and set (TAS)
    - tas(?shared, ?private[self ]);
    - spinlock: implement mutual exclusion for a set of N processes, executed in tight loop
    - invariant
        - at most one of N+1 variables is False
        - if process i in critical section, then private[i] = False
        - 

## Chap 9 Locks and Blocking
- atomic 
    - statements executed within an atomic statement
    - if atomic statement executing, no other process can execute
    - assert statement executed atomically
    - rare programming paradigm
    - good for implementing interlock instructions
- critical section
    - protected by a lock
    - allos processes to run concurrently, but not within the cs
    - common, available in many progamming languages
    - good for building concurrent data structures
- lock in synch module
    - implemented with tas
    - 
        ```
        def tas(lk): 
            atomic:
                result = !lk; 
                !lk = True;

        def Lock():
            result = False
        
        def lock():
            await not tas(lk);
        
        def unlock():
            !lk = False
        ```
    
- process is blocked
    - if a process cannot change the state or terminate
    - or can only do so if another process changes the state first.

## Chap 10 Concurrent Data Structures
- uses separate locks for the head and tail
- allowing an enqueue and a dequeue operation to proceed concurrently
- uses a dummy node at the head of the linked list

## Chap 11 Reader/Writer Locks using Busy Waiting
- busy-waiting 
    - process spin in a loop until some desirable application-level condition is met
    - wasting CPU cycles
    - okay for multi-core (true) parallelism
    - bad for time-sharing (virtual) parallelism
    - preferable when 
        - schedling overhead larger than expected wait time
        - processor resource not needed for other process
    - in time-multiplexed threads, busy-waiting can lead to significant waste of CPU cycles
- if mutex is busy-waiting
    - the Harmony synch implementation of lock() spins in a loop until the mutex is available
    - process waiting for spinlock are blocked
    - placed on a scheduling queue, stops using CPU cycles, until mutex becomes available
    - but in busy-waiting, readers and writers only get suspended temporarily
- Busy waiting is when a process runs continually checking whether a flag has been set (or a lock freed)
- Blocking involves the process not running until it is woken up to let it know that the resource is available.

## Chap 12 Reader/Writer Locks with Blocking
- A writer simply acquires rwlock to enter the critical section and releases it to exit
- The first reader to enter the critical section acquires rwlock and the last reader to exit the critical section releases rwlock.
- no busy waiting
- readers and writers 'block' when they can't enter the critical section
## Chap 13 Semaphores
- essentially a counter that can be incremented and decremented but is not allowed to go below zero
- initialized to the number of units of a resource initially available
- P/Procure
    - blocks the invoking process if the counter is zero
- V/Vacate
    - increments the resource 

## Chap 14 Bounded Buffer
- bounded buffer / producer&consumer

## Chap 15 Split Binary Semaphores
- proposed by Tony Hoare
- baton-passing technique
    - a process needs the baton to access shared variables
    - if a process want to release the baton
    - first checks to see if there are any processes that are waiting for the baton
    - if not, then release
- if N waiting conditions, then use N+1 binary semaphora
    - one for each waiting condition
    - extra one (mutex) that processes use when they first try to enter the critical section and do not yet know if they need to wait.
    - sum of N+1 semaphores must be 0 / 1
        - 0 when a process is accessing the shared variable
- each process alternates P and V operations,
- V_one
    - baton passing function
    - If there are readers waiting and there are no writers in the critical section, it vacates the semaphore associated with readers waiting
    - passing the baton to the next reader
    - If none of the conditions hold
    - V one() vacates mutex, leaving the batom for a future process to pick up.

## Chap 17 Monitors
- condition variables
    - cv is a semaphore that is 0 when ``wait`` is invoked
    - wait
        - release the mutex
        - blocks while trying to procure the cv
    - signal
        - vacates cv
        - procures mutex
    -  
        ```
        def wait(c):
            V(?mutex);
            P(c);
        ;
        def signal(c):
            V(c);
            P(?mutex);
        ;
        ```
- hoare monitors
    - hidden mutex associated with each monitor
    - mutex automatically acquired upon entry to a method and released upon exit
    - only one process could enter the bathroom through bedroom
    - ~ split binary semaphore
- mesa monitors
    - notify (instead of signal) all processes
    - all processes could enter the bathroom through hall
    - when a process is entering, the condition that it waits for might no longer holds
    - notifyAll let all processes in a bedroom into the hall
    - ~ busy-waiting
    - Busy- waiting is “fixed” by placing a wait statement in the waiting loop.
    - A Mesa wait() operation should always be placed inside a while loop
    - It is always safe to replace wait(c) by the sequence unlock(k); lock(k);, where k is the monitor lock and c is some condition variable in the monitor
    - It is always safe to replace multiple condition variables of the same monitor lock by a single condition variable
- languages
    - Java
        - each object has a hidden lock and a hidden condition variable associated with it
        -  Methods declared with the synchronized keyword automatically obtain the lock
        - Java objects also support wait, notify, and notifyAll.
    - Python
    - locks and condition variables must be explicitly declared
    - The ``with`` statement makes it easy to acquire and release a lock for a section of code.
- cv condition variable
    - ``Condition(lk)`` creates a new condition variable associated with the given pointer to a lock ``lk``.
    - represented by a dictionary 
        - containing the pointer to the lock
        - a bag of name tags of processes waiting on the condition variable
    - ``wait`` adds the nametag of the process to the bag.
    - ``notify`` removes an arbitrary context from the bag
    - ``notifyAll`` empties out the entire bag, allowing all processes in the bag to resume.
- reader/writer locks with mesa condition variables
    - ``wait`` is always invoked within a while loop that checks for the condition that the process is waiting for.
    - when a process resumes after being notified, it is not guaranteed that the condition it was waiting for holds
- Waking up too many processes may lead to some inefficiency
- but waking up too few may cause the application to get stuck
- A semaphore has memory
    - if some process does a V on a semaphore, and later another process does a P
    - then the second process won’t block. 
- With condition variables
    - if a process signals a condition variable and later some other process invokes wait()
    - then the process ends up being blocked until there is another signal() operation

## Chapter 18 Deadlock
- four conditions that must hold for deadlock to occur 
    - Mutual Exclusion
        - each resource can only be used by one process at a time:
    - Hold and Wait
        - each process holds resources it already allocated while it waits for other resources that it needs;
    - No Preemption 
        - Resources cannot be forcibly taken away from processes that allocated them;
    - Circular Wait
        - There exists a directed circular chain of processes, each waiting to allocate a resource held by the next.
- techniques proposed by Havender to prevent deadlock
    - No Hold and Wait
        - a process must request all resources it is going to need at the same time
        - a philosopher would need a way to lock both the left and right forks at the same time
        - 
            ```
            while forks[left] or forks[right]:
                if forks[left]: 
                    wait(?conds [left ]);
                ;
                if forks[right]:
                    wait(?conds [right ]); 
                ;
            ;
            ```
    - Preemption
        - if a process is denied a request for a resource, it must release all resources that it has already acquired and start over;
        - allow process to backout
        - but invariably leads to a busy waiting solution, where a process keeps obtaining locks and releasing them
        - until it finally get all of them
    - No Circular Wait
        - define an ordering on all resources and allocate resources in a particular order
        - establish an ordering among the resources
        - e.g. pickup lower numbered fork before the higher numbered fork
    - deadlock avoidance
        - prevent > 4 philosophers eat at the same time

## Chapter 19 Actors and Message Passing
- actors
    - processes that have only private memory and communicate through message passing
    - no shared memory in the actor model, other than the message queues
- Each thread would have one such queue for receiving messages.
- Dequeuing from an empty synchronized queue blocks the thread until another thread enqueues a message on the queue.
- ``Queue`` behaves much like a zero-initialized semaphore
- ``enqueue`` is much like V, except that it is accompanied by data-
- ``dequeue`` is much like P, except that it also returns data.

## prelim 1
1.
The following concerns a single-core single-processor computer. Process P1 is in a read() system call to read data from a disk. The disk operation just completed and the disk interrupt handler has placed P1 on the run (aka ready) queue. Process P2 is currently running and is about to call the read() system call to read characters from the keyboard, although nobody is currently typing. There are no other runnable processes. Put the following steps that are about to occur in the right order. However, one of the steps is not a valid step, and you should leave it out. By the way, an “interrupt stack” is the same as the kernel stack of a process.
- P2 executes the read() system call to read from the keyboard.
- P2 switches from user mode to supervisor mode and pushes the PSW, PC, and (user) SP onto the interrupt stack of P2. P2 also loads the address of the system call interrupt handler into the PC.
- P2 pushes its general purpose registers onto the interrupt stack. P2 invokes the kernel code to read from the keyboard. P2 then goes into WAITING mode and enqueues its PCB onto the waiting queue of the keyboard driver. It then calls the scheduler, which takes P1 off the run queue.
- P2 executes a context switch to P1, pushing the kernel’s registers (except SP) of P2 onto P2 ’s interrupt stack, saves the SP into P2’s PCB, loads the SP from P1’s PCB, and pops P1’s kernel registers from the interrupt stack.
- P1 resumes executing the code that is reading data from the disk and returns to the system call interrupt handler. The interrupt handler pops the user registers except SP, PC, and PSW from the interrupt stack.
- P1 executes “return-from-interrupt”, which switches the CPU from supervisor mode to user mode and pops the user SP, PC, and PSW from the interrupt stack.
- P1 returns from the read() system call that reads data from disk.

## prelim2
- FAT file system
    - There is a clean separation between data blocks and meta-data blocks
    - FAT file systems are highly portable to many different operating systems
- write back cache
    - A write-back cache improves update latency for applications
    - Because writing to disk is delayed, a write-back cache could lead to data loss in case of a crash

## final practice
