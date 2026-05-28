# A tuple is an immutable, ordered collection of elements in Python. 
# Tuples are similar to lists but cannot be modified after creation(IMMUTABLE like STRINGS).

# Creating tuples
my_tuple = (1, 2, 3)           # Parentheses (recommended)
my_tuple = 1, 2, 3             # Parentheses optional (tuple packing)
empty_tuple = ()               # Empty tuple
single_tuple = (5,)            # Single element (comma is required!)
single_tuple_wrong = (5)       # This is just an integer, NOT a tuple

# 1. Immutability
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 2. Ordered Collection
my_tuple = (10, 20, 30) #After creating new tuple with same name (this point to new reference , old tuple has no reference eligible for garbage collection)
print(my_tuple[0])   # 10
print(my_tuple[-1])  # 30

#3. Mixed Tuple
mixed_tuple = (1, "hello", 3.14, [1, 2, 3], ["key", "value"])
print(mixed_tuple[3][2]) #output : 3 bcz 3rd index of mixed_tuple is [1,2,3] and 2nd index of [1,2,3] is 3
print(mixed_tuple[4][1]) #output :  value

# Creating Tuples
# Different ways to create tuples
tuple1 = (1, 2, 3)                     # Direct assignment
tuple2 = tuple([1, 2, 3])              # From list --> list in tuple
tuple3 = tuple("abc")                  # From string -> ('a', 'b', 'c')
tuple4 = tuple(range(5))               # From range -> (0, 1, 2, 3, 4)
tuple5 = tuple(x*2 for x in range(3))  # -> (0, 2, 4)
print(tuple3[2]) # output : c
print(tuple4)
print(tuple5)

# Accessing Tuple Elements

my_tuple = ('a', 'b', 'c', 'd', 'e')

# Indexing
print(my_tuple[0])      # 'a'
print(my_tuple[-1])     # 'e'

# Slicing (New Tuple is returned )
print(my_tuple[1:3])    # ('b', 'c')
print(my_tuple[:3])     # ('a', 'b', 'c')
print(my_tuple[2:])     # ('c', 'd', 'e')
print(my_tuple[::2])    # ('a', 'c', 'e') - step of 2


# Tuple Operations

# 1. Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# 2. Repetition
my_tuple = (1, 2)
repeated = my_tuple * 3  # (1, 2, 1, 2, 1, 2)

# 3. Membership Testing
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)      # True
print(10 not in my_tuple) # True


# TUPLE METHODS

# Tuples have only two built-in methods:

my_tuple = (1, 2, 3, 2, 4, 2)

# count() - counts occurrences
print(my_tuple.count(2))  # 3

# index() - finds first occurrence
print(my_tuple.index(3))  # 2
print(my_tuple.index(2, 2))  # 3 (start searching from index 2)