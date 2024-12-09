# Get my_list.txt from the current executed directory
list_path = "2024/Day1/my_list.txt"

left_list = list()
right_list = list()

# Load the content of my_list.txt
with open(list_path, "r") as f:
    my_list = f.read().splitlines()
    # Split each entry in the left and right entry, each is divided by 3 spaces, but it will be safer to split on all whitespaces in case of more or less spacing
    for entry in my_list:
        left, right = entry.split()
        left_list.append(left)
        right_list.append(right)

# Sort from small to big
left_list.sort()
right_list.sort()

# Compare each same entry and figure out the difference and store that in a new list
difference = list()
for i in range(len(left_list)):
    # Show for the first 5 to check
    if i < 5:
        print(f"Left: {left_list[i]} Right: {right_list[i]}")
        print(f"Difference: {abs(int(right_list[i]) - int(left_list[i]))}")
    difference.append(abs(int(right_list[i]) - int(left_list[i]))) # abs() is to get the absolute difference (so negatives become positive which gives us the correct output when summing)

# Lastly combine all the entries to 1
result = sum(difference)

print(result) # 1722302 CORRECT!!