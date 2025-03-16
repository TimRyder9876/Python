# exercise 5_22 simulating a queue with a list

queue_list = []

queue_list.append(3)
queue_list.append(2)
queue_list.append(1)

print(queue_list)

for i in range(len(queue_list)):
    queue_list.pop(0)
    print(queue_list)
