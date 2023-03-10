Schedule Tasks on Minimum Machines

Given a set of n number of tasks, implement a task scheduler method, tasks(), to run in O(n logn) time that finds the minimum number of machines required to 
complete these n tasks.


import heapq

def tasks(tasks_list):
    # to count the total number of machines for "optimal_machines" tasks
    optimal_machines = 0
    # empty list to store tasks finish time
    machines_available = []
    # converting list of set "optimal_machines" to a heap
    heapq.heapify(tasks_list)

    while tasks_list:  # looping through the tasks list
        # remove from "tasks_list" the task i with earliest start time
        task = heapq.heappop(tasks_list)

        if machines_available and task[0] >= machines_available[0][0]:
            print(task[0])
            print(machines_available[0][0])
            
            # top element is deleted from "machines_available"
            machine_in_use = heapq.heappop(machines_available)

            # schedule task on the current machine
            machine_in_use = (task[1], machine_in_use[1])

        else:
            # if there's a conflicting task, increment the
            # counter for machines and store this task's
            # end time on heap "machines_available"
            optimal_machines += 1
            machine_in_use = (task[1], optimal_machines)

        heapq.heappush(machines_available, machine_in_use)

    # return the total number of machines used by "tasks_list" tasks
    return optimal_machines