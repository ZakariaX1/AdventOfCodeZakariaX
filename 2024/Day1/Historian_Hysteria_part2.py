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

# Sort from small to big, this will help us finding the same numbers efficiently because if the next number is not the same then we exhausted the similar values
left_list.sort()
right_list.sort()

# Thought process:
# Step 1 look at the left list and pick the next (or first) number, remember this number for the next number in case it is the same
# Step 2 look for that number in the right list, keep a "cursor" in that list as well to know where you are at, since both lists are sorted if you are looking for a big number any smaller numbers aren't important anymore
# Step 2b stop looking for that number when the next number in the right list is bigger than the the number looked for
# Step 2c Store the number * the amount of times found in a new list and store this value in a temp value in case another same number is found to skip computation
# Step 3 sum all the weighted items together

lprev_int = None
lprev_result = None
right_list_cursor = 0
similarity_list = list()

for left_item in left_list:
    count_inr = 0
    if left_item == lprev_int:
        similarity_list.append(lprev_result)
        continue

    while left_item >= right_list[right_list_cursor]:
        if left_item < right_list[right_list_cursor]:
            break # Not to be found in right list, dont move cursor further yet
        if left_item == right_list[right_list_cursor]:
            count_inr += 1
        right_list_cursor += 1
    
    lprev_int = left_item
    lprev_result = count_inr * int(left_item)
    similarity_list.append(lprev_result)

result = sum(similarity_list)
print(result) # 20373490 CORRECT!!

