#Name:Tristan long
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("hello world")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
my_dictionary = {
    "key1": "value_a",
    "key2": 123,
    "key3": [1, 2, 3]}
#3. Print the keys of the dictionary from #2.
print(my_dictionary.keys())
#4. Print the values of the dictionary from #2
print(my_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(my_dictionary["key3"][2])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
my_dictionary.update({"fourth_key": "value4"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(my_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
sixth_hour_class = {
    "student_1" : {
        "Name" : "Ally",
        "Grade" : 12,
        "Sports" : False,
    },
    "student_2" : {
        "Name" : "Aaden",
        "Grade" : 11,
        "Sports" : True,
    },
    "student_3" : {
        "Name" : "Ethan",
        "Grade" : 9,
        "Sports" : True,
    },
}
#9. Print the names of all three classmates on the same line.
print(sixth_hour_class["student_1"]["Name"],sixth_hour_class["student_2"]["Name"],sixth_hour_class["student_3"]["Name"],)
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
sixth_hour_class.pop("student_3")
print(sixth_hour_class)