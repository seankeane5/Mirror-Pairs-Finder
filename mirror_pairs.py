import time
start_time = time.time()
debug = False
print_timing = False

class TestNumber: #Making a class to hold the two numbers and their combined palindrome status
    def __init__(self, number_one, number_two):
        self.number_one = number_one
        self.number_two = number_two
        self.whole_number = number_one + number_two
        self.is_palindrome = (self.whole_number) == (self.whole_number)[::-1]
        
    def print_self(self):
        if(debug): 
            print('Whole Number:' , self.whole_number, ' Is Palindrome:', self.is_palindrome)

    def are_you_palindrome(self): # Defining a method to return if the number is a palindrome
        return self.is_palindrome
    
    def get_whole_number_as_int(self): #Getting the whole number as an integer
        return int(self.whole_number)
    
if (debug):
    print('Setting up hash tables...')

starts_with_hash_table = {}
ends_with_hash_table = {}

for i in range(10):
    for j in range(10):
        key = str(i) + str(j)
        starts_with_hash_table[key] = {} #Sets up empty hashtables for each digit 0-9
        ends_with_hash_table[key] = {}

n = int(input()) # Read how many numbers will be input

input_str = input() #Reads all the numbers as a single string
input_numbers = input_str.split() #Converts to a string and splits into list


for i in range(n): #Starts at 0
    number = input_numbers[i]
    if len(number) < 2:
        first_two = '0' + number[0] #Adds single digit numbers to the hash map by adding a zero in front
        last_two = '0' + number[-1]
    else:
        first_two = number[:2]
        last_two = number[-2:]
    list_one = starts_with_hash_table[first_two] #List for the first characters
    list_two = ends_with_hash_table[last_two] #List for the last characters
    list_one[number] = number #Puts the full number into the list for first characters
    list_two[number] = number

if (debug):
    for i in range(10):
        for j in range(10):
            key = str(i) + str(j)
            print('Items in key', key)
            list = starts_with_hash_table[key] #Grabs from numebrs 1-10 and prints the lists 
            for item in list:
                print('  ', item)
if (debug):
    print('Starting palindrome check...')
#Loop through items in the starts_with and ends_with hash tables

current_largest = 0

for i in range(10):
    for j in range(10):
        startsWithKey = str(i) + str(j)
        endsWithKey = str(j) + str(i)
        starts_with_list = starts_with_hash_table[startsWithKey] #Pulls the list out of the key for the starts_with table
        ends_with_list = ends_with_hash_table[endsWithKey] #Pulls the list out of the key for the ends_with table
        for item in starts_with_list: 
            for item_two in ends_with_list:
                if item == item_two: #Skip numbers of the same value
                    continue
                if(debug):
                    print('  Testing pair:', item, item_two)
                test_number = TestNumber(item, item_two) #Creates object from the two number parts
                if test_number.are_you_palindrome(): #Checks if it's a palindrome
                    if test_number.get_whole_number_as_int() > current_largest:
                        current_largest = test_number.get_whole_number_as_int()

print(current_largest)


if(print_timing):
    print("--- %s seconds ---" % (time.time() - start_time))