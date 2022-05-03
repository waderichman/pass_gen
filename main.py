import passwordgenerator
import priority_queue
import heapsort
import time

# take in value
keyword = input("\nEnter a keyword you'd like your password based around: ")
inputVar = True
while inputVar:
    length = int(input("Enter a number greater than or equal to 12: "))
    if length >= 12:
        break
    else:
        print("Try again (enter a string for keyword and an integer greater than or equal to 12 for length.")

print("\n")

start = time.time()
passwords_dict = passwordgenerator.generate_dict(keyword, length)
end = time.time()

print("Password Generator time: ")
print(end - start)

start = time.time()
arr_of_keys = list(passwords_dict.keys())

heapsort.heap_sort(arr_of_keys)

max_score_heapsort = arr_of_keys[-1]
end = time.time()
print("Heapsort time: ")
print(end - start)

start = time.time()
priority_queue_keys = priority_queue.PriorityQueue()
for j in arr_of_keys:
    priority_queue_keys.insert(j)

if not (priority_queue_keys.is_empty()):
    max_score_priority_queue = priority_queue_keys.pop()
end = time.time()

print("Priority Queue time: ")
print(end - start)

topPasswords = passwords_dict[max_score_heapsort][0: 30]

print("\nThe top passwords are: ")
print(*topPasswords, sep="\n")
