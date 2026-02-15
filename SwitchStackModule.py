# List created for testing, can be pulled from "show switch" output on Cisco switches by passing output into a list
my_list = [
    '*1', 'Standby', '7802.b1fe.b580', '1', 'V02', 'Ready',
    '2', 'Standby', '7802.b1e9.7e00', '1', 'V02', 'Ready']

# Checks for filtered output to create total numbers of switches in stack
search_value = "Ready"
total_members = 0
for item in my_list:
    if search_value in item:
        total_members += 1
        count_value = str(total_members)
        print("Located switch " + count_value)

print("Total switches in stack - " + count_value)

# Takes the total number of stack members and repeats an action(s) for each stack member
stack_members = total_members
for stack_number in range(stack_members):
    number = str(stack_number + 1)
    print("Performing tasks on switch " + number)