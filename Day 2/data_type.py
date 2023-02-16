# Take a look at the codes below 

num_char = len(input("What is your name ? "))

print("your name has " + num_char + " characters.")

# The above code will return an error due to trying to concatenate string and integers.

# To remove the error we do what is known as type casting or type conversion.

# we have to know the data type(using the type function) first before we can carry out type casting.

print(type(num_char))

# we can then carry out type casting

new_num_char = str(num_char)

# Next thing is to rewrite our print statement to print the type casted data

print("your name has " + new_num_char + " characters.")

The above codes will work just fine.