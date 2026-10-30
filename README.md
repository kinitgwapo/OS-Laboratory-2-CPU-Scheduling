# Description
CPU scheduling is an operating system function that determines which process in the ready queue receives CPU time. Different scheduling algorithms use different rules to determine execution order, affecting waiting time, turnaround time, response time, and overall system responsiveness.

# Terminal Output
The Gantt chart, process metrics, and averages for each algorithm.

<img width="773" height="971" alt="Part C" src="https://github.com/user-attachments/assets/5357bede-1994-4677-b875-21ba258b051f" />

# Drawn Gantt chart for each algorithm

<img width="941" height="1080" alt="Part D Gantt Chart" src="https://github.com/user-attachments/assets/37d10add-34ed-4b19-abe2-7146a644a7dd" />

# FCFS & SJF verification

##### FCFS
<img width="1234" height="865" alt="Part D FCFS Verification" src="https://github.com/user-attachments/assets/04ec983a-9341-422f-806e-ead78b1c026b" />

##### SJF
<img width="1234" height="865" alt="Part D N-P SJF Verification" src="https://github.com/user-attachments/assets/095c8281-b21b-44d3-bf68-a4dca1c0b949" />

# Round Robin verification

<img width="1234" height="865" alt="Part D RR(Q=2) Verification" src="https://github.com/user-attachments/assets/20ebaae5-40fe-47a5-87aa-de4060395b40" />

# SRTF verification

<img width="1095" height="802" alt="Part D SRTF Identification" src="https://github.com/user-attachments/assets/f785e739-03b1-4d43-b99b-de979d5caf60" />

# Questions



## Context: Differences between quanta 1, 2 and 4

#### How does the time quantum affect the number of CPU allocations?
Time quantum affects how long each task gets its execution time. If it were a quantum time of 1, a general formula to acquire the total cpu allocations of all tasks is simply summing up all the burst times, but does not work for a quantum time that is not 1.

#### Which quantum produces the lowest average waiting time in your tests?
Quantum time of 2 & 4

#### What happens when the quantum becomes very large?
If the quantum value is larger than the highest recorded task burst time, then it simply becomes a First come First serve type of task scheduling algorithm.

#### Why can a very small quantum increase context-switching overhead in a real operating system?
Because the tasks are switching every 1 quantum unit of OS time, the Process control block (PCB) struggles to keep up with the amount of tasks states being saved and used by another task simultaneously, leading to context-switching overhead whenever the quantum time is very low.

## General Questions




#### What is CPU scheduling, and why is it necessary?
CPU scheduling or task scheduling deals with processes/task execution. Imagine a large amount of tasks waiting in line, the scheduler could technically just finish tasks based on a queue, or specify what comes and goes first in a way that reduces the total time it takes to complete a specific task.

#### What is the difference between FCFS and SJF?
FCFS executes the first task that is loaded onto the queue, the last task loaded will be executed last. Non-preemptive SJF executes tasks in an ascending burst time level, meaning, a task that has the lowest burst time is executed first while a task with the highest burst time will be executed last. And with the exception of no preemption, a task loaded with a lower burst time than the current executing task will not be interrupted until the current executing task is finished.

#### Why can SJF produce a lower average waiting time than FCFS?
SJF first finishes tasks with the lowest burst time, which leads to lower task waiting time to be significantly lower than the higher burst time tasks.

#### How does Priority Scheduling determine the next process?
Non-preemptive priority scheduling executes tasks first with the highest priority, except, it does not preempt or interrupt the currently executing task unlike the usual preemptive priority task scheduler.

#### What is starvation? Which algorithms can experience it?
Starvation means a task’s execution time is always robbed or used by other tasks due to the scheduling design. Algorithms such as, priority scheduling suffers from it due to unfair task prioritization. Although it is typically fixed by the term “aging”, it increases the stalled task’s priority level so that it can be executed sooner or later, rather than waiting indefinitely.

#### How does Round Robin improve responsiveness for interactive processes?
Processes/tasks that are interactive or require user input are in a great advantage when it comes to Round Robin because all tasks have an equal time slice in which they can execute, and having user input requires it to check quickly and periodically. A user input run every 40ms is considered enough for a simple interactive task.

#### What is the effect of changing the Round Robin time quantum?
Typically it is the waiting, response, average waiting, average response time of the processes because a large quantum time acts similar to a FCFS, while a smaller quantum time leads to lower response and average response time, but significantly increases the waiting and average waiting time.

#### How does SRTF differ from non-preemptive SJF?
SRTF is SJF but with preemption capabilities, unlike SJF which is also known as Non-Preemptive SJF. SRTF looks at the burst time, and whoever at a specific time frame has the lowest burst time is executed first, which means it preempts any currently running task that has a burst time higher than itself.

#### Why do preemptive algorithms require the operating system to save and restore process context?
The word preemptive means that the currently running task can be interrupted, meaning, it can be stopped momentarily for other tasks to work, in which case it requires the last task state to be saved and stored, managed by the Process Control Block. When the preempting task finishes, the scheduling returns to the previous preempted task, reads its last known state maintained by the PCB, and resumes from it. Without the knowledge of the previous task state, all its progress is erased, leading to starting all over again.

#### Does the algorithm with the lowest average waiting time always provide the best user experience? Explain.
An algorithm with the lowest average waiting time does not always provide the best user experience. Although shorter waiting times generally make users more satisfied, other factors such as fairness and consistency should also be considered. An algorithm should not only minimize the average waiting time but also ensure that all users receive a fair and efficient service.

#### Why is it important to use the same dataset when comparing algorithms?
It is important to compare algorithms with the same data configuration to avoid bias, and advantage to one another algorithm because some algorithms are stronger in a specific data configuration, and just like in any other experimental comparison, data must be the same throughout the tests.

#### What role does GitHub play in managing and submitting your laboratory work?
Github is simply an online git repository, which allows anyone (depending on the repository visibility) to acquire the same files/project with a recorded history of changes in the file/project state. Technically it is the git software that deals with tracking your files and preserving its history.

# Conclusions
In this laboratory, I have learned a few different types of task scheduling algorithms, how they differ from advantages and disadvantages, especially the experimentation on how Round robin’s quantum time quantity affects different datasets. Overall, having knowledge of the fundamentals of CPU scheduling provides us to understand more about the underlying logic of an Operating System, and provides a clearer understanding onto the coming topics.
