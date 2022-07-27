# Final Examination in Parallel and Distributed Computing
Adrian Arboleda BSCS 3B

## SIMD vs MIMD
Single-Instruction Multiple-Data (SIMD) and Multiple-Instruction Multiple Data (MIMD) are classification in Flynn’s Taxonomy. SIMD and MIMD both operates on multiple data sets, but they have distinct difference. SIMD, although operates on multiple data, just uses a single instruction for these data because it does have contain a single decoder. On the other hand, MIMD, which also operates on multiple data, does have a multiple instructions for multiple data. It is a system built as a multiprocessor machine. MIMD is much efficient compared to SIMD.


## Performance Metrics for Parallel Systems
There are 5 Performance Metrics for Parallel Systems. This includes the following:

Execution Time – Execution Time is the total time taken by single process to complete the problem.

Total Parallel Overhead - The amount of time required to coordinate parallel tasks. It includes factors such as: Task start-up time, Synchronizations, Data communications.

Speedup - The speedup of a parallel solution is measured in the time it took to complete the task sequentially divided by the time it took to complete the task when done in parallel.

Efficiency - The parallel efficiency of a program is the ratio of the speedup factor and the number of processors. These quantities can be used to estimate how much of the computing capacity is actually used to carry out a calculation.

Cost -it is considered cost efficient if its asymptotic running time multiplied by the number of processing units involved in the computation is comparable to the running time of the best sequential algorithm. Processors will be considered cost efficient.


## How does the performance of metrics of parallel systems affect each other?
Performance metrics determine the total usability and efficiency of a parallel system. Performance is measured by this metrics, and the results of these metrics show how powerful a parallel system is. Each metric does have a threshold of what’s bad and what is good in the parallel system. For example, if the speedup is long and the cost is high, we can conclude that the parallel system built is not efficient. The metrics are the factors that determine the performance of the parallel system.

## Pipelining
In computing, a pipeline is the continuous and overlapped movement of instruction to the processor/CPU. It is also known as the arithmetic steps taken by the processor to perform an instruction. Pipelining, on the other hand, is the process of using a pipeline. It is best compared to a manufacturing assembly line in which different parts of a product are being assembled at the same time although ultimately there may be some parts that have to be assembled before others are. Even if there is some sequential dependency, the overall process can take advantage of those operations that can proceed concurrently.
In conclusion, pipelining in computing term is the process of dividing into an instruction pipeline and arithmetic pipeline. The instruction pipeline represents the stages in which an instruction is moved through the processor, while the arithmetic pipeline represents the parts of arithmetic operation that can be broken down and overlapped as they are performed.


## Von Neumann Architecture
![image](https://user-images.githubusercontent.com/73649759/181277456-46d7e7a3-85fb-47cc-b1cd-ae5d688d2648.png)

Von Neumann Architecture, or Princeton architecture, is a computer architecture based on 1945 description by John Von Neumann.
The modern computers are based on stored program concept where the programs and data are stored in a separate storage unit called memory unit and are treated the same.
It is a stored-program computer in which an instruction fetch and a data operation cannot run at the same time.
It is divided mainly in 3 basic units: Central Processing Unit, Main Memory Unit, and Input and Output Device.

## Central Processing Unit
In Control Unit, this is where all processors handle control signals. It directs all input and output flow, fetches code for instructions, and controls how data moves around the system.
The calculations needed by CPU is on the Arithmetic/Logic Unit. It performs Additon, Subtractions and Comparisons. It also performs Logical, Bit Shifting, and Arithmetic Operations.

## Memory Unit
Memory unit contains:
•	Accumulator – It stores the results of calculations made by Arithmetic/Logic Unit (ALU)
•	Program Counter – It keeps track of the memory location of the next instructions to be dealt with. The PC then passes this next address to Memory Address Register (MAR).
•	Memory Address Register - It stores the memory locations of instructions that need to be fetched from memory or stored into memory.
•	Memory Data Register - It stores instructions fetched from memory or any data that is to be transferred to, and stored in, memory.
•	Current Instruction Register - It stores the most recently fetched instructions while it is waiting to be coded and executed, and;
•	Instruction Buffer Register – It is the instruction that is not to be executed immediately is placed in the instruction buffer register IBR.

## Input/Output Devices
This are the programs or data that is read into main memory from the input device or secondary storage under the control of CPU instruction. Output Devices, on the other hand, are used to output the information from the computer. It is then displayed to the user.


## How does parallel programming/computing works? What do you think will be the advantage of utilizing parallel approach?
Parallel computing works by using multiple computer cores to attack several operations at once. It breaks down its job into component parts and multi-task them. It is used in everyday tasks and it can handle “big data” very well. The big advantage of utilizing the power of parallel computing is that the heavy tasks you do in your devices will become much easier. It will be also much faster as it uses multiple cores. For example – handling big data you fetched from being data scientist is much efficient and faster now as your computer uses parallel computing. Works will be smooth and you’ll be productive in your tasks.


## Multiprocessing vs Multithreading

Multiprocessing is what a system is called when is has more than one or two processors. The CPU are added for increasing computing speed of the system and because of it, there are many processes that are executed simultaneously. It has two categories – Symmetric and Asymmetric Multiprocessing.

Multithreading, on the other hand, is a system in which multiple THREADS are created for a process to increase the computing speed of the system. In this system, many threads of a process are executed simultaneously and process creation in multithreading is done according to economical.
There’s quite a difference in the two, but the most significant one is that in Multiprocessing, CPUs are added to increase computing power while in Multithreading, many threads are created in a single process to increase computing power. Also in Multiprocessing, every process owns a separate address in space while in Multithreading, a common address space is shared by all the threads. 

## Serial Computing and Parallel Computing

Before Parallel Computing, Serial computing was first use. As we know, parallel computing is the best system that we are using right now. The difference between the two is big. Here is the difference
In Serial Computing, there is only a single processors and the processes are only moved on when the present task is finished. In short, it is executed in sequence, while in Parallel Computing, the processors are completed at a time by multiple different processors. Serial computing also has lower performance compared to Parallel Computing, thus we can say that the serial computing requires more time to complete the task compared to parallel computing that only requires less time to do tasks.


## Programming Questions:

### L2.2
In a right triangle, the square of the length of one side is equal to the
sum of the squares of the lengths of the other two sides. Write a
program that prompts the user to enter the length of the three sides of
a triangle and then outputs a message indicating whether the triangle
is a right triangle. 

Code: 
[LEVEL 2.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL%202.py)

Output:

![image](https://user-images.githubusercontent.com/73649759/181278896-819cd710-77da-4cac-847a-424b9bca7324.png)

### L23
Write a program that prompts the user to input a number between 0
and 35. If the number is less than or equal to 9, the program should
output the number; otherwise, it should output A for 10, B for 11, C for
12… and Z for 35.

Code:
[LEVEL 2.3.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL%202.3.py)

Output:

![image](https://user-images.githubusercontent.com/73649759/181280535-80de7483-b50e-4676-97f4-887f2b4c2a43.png)

### L2.4
Write a program that will display all numbers divisible by 3, 4 and 5
from 1-50. 

Code:
[LEVEL 2.5.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL%202.5.py)

Output:

![image](https://user-images.githubusercontent.com/73649759/181281224-9f5cf0f5-1a4c-4380-80c2-eed9737c7bd6.png)

### L3.3
Create a function in Python that accepts two parameters. The first will
be a list of numbers. The second parameter will be a string that can
be one of the following values: asc, desc, and none. If the second
parameter is "asc," then the function should return a list with the
numbers in ascending order. If it's "desc," then the list should be in
descending order, and if it's "none," it should return the original list
unaltered. 

Code:
[LEVEL 3.3.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL%203.3.py)


Output:\
![image](https://user-images.githubusercontent.com/73649759/181282286-e92cb9c2-ea95-4439-b05e-c090c1dc7a19.png)
![image](https://user-images.githubusercontent.com/73649759/181282489-5dda8359-c90c-4897-a3ac-6bdabfc06989.png)
![image](https://user-images.githubusercontent.com/73649759/181282574-7b7f4990-f216-44c7-87c1-08d8e54ed66c.png)

### L4
Write a program that will generate 100 3-digit random numbers and
store it in a list. The program should display the following:
a. All elements in the list
b. All numbers grouped by odd and even numbers
c. All numbers divisible by 9.
d. All prime numbers
e. All numbers that contains the digit 9 (e.g 29, 91, 393, 961)

Code:

[LEVEL 4.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL%20%204.py)

Output:\
![image](https://user-images.githubusercontent.com/73649759/181282981-cfbd1954-fef5-4663-a059-3b2e77899927.png)


### L5
Flatten the given Linked list
Sorting must be performed during the flattening of the linked list. 


Code:
[LEVEL-5.py](https://github.com/0x0000017/final-examination/blob/main/LEVEL-5.py)

Output:\
![image](https://user-images.githubusercontent.com/73649759/181283222-02f9cd4e-6fb5-4b92-9e85-0dbcce894874.png)
