# Operating Systems Laboratory Activity 2
# CPU Scheduling Simulator

PROCESSES = [
    {"pid": "P1", "at": 0, "bt": 8, "priority": 2},
    {"pid": "P2", "at": 0, "bt": 4, "priority": 1},
    {"pid": "P3", "at": 0, "bt": 2, "priority": 4},
    {"pid": "P4", "at": 0, "bt": 6, "priority": 3},
]

SRTF_PROCESSES = [
    {"pid": "P1", "at": 0, "bt": 8, "priority": 2},
    {"pid": "P2", "at": 1, "bt": 4, "priority": 1},
    {"pid": "P3", "at": 2, "bt": 2, "priority": 4},
    {"pid": "P4", "at": 3, "bt": 1, "priority": 3},
]

def print_concatenate(t1, t2):
    for x in range(4):
        t1[x] = PROCESSES[x]["pid"] + "\t" + str(PROCESSES[x]["at"]) + "\t" + str(PROCESSES[x]["bt"]) + "\t" + str(PROCESSES[x]["priority"])
        
        if(x == 3):
            for y in range(4):
                t2[y] = SRTF_PROCESSES[y]["pid"] + "\t" + str(SRTF_PROCESSES[y]["at"]) + "\t" + str(SRTF_PROCESSES[y]["bt"]) + "\t" + str(SRTF_PROCESSES[y]["priority"])

def print_set(t1, t2):
    print("Process Table\npid\tat\tbt\tpriority")
    for x in range(4):
        print(t1[x])

        if(x == 3):
            print("\nSRTF Process Table\npid\tat\tbt\tpriority")
            for y in range(4):
                print(t2[y])

def print_helper_function():
    text1 = ["", "", "", ""]
    text2 = ["", "", "", ""]

    print_concatenate(text1, text2)
    print_set(text1, text2)

print_helper_function()