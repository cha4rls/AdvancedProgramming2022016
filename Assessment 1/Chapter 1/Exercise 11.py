#Tuples
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

#Value at index -3
print(f"Value at index -3: {year[-3]}")

#Prints the original and reversed tuple
print(f"Original Tuple: {year}")
print(f"Reversed Tuple: {tuple(reversed(year))}")

#Counts the amount of 2009 in the tuple
print(f"Number of times 2009 is in the tuple: {year.count(2009)}")

#Finds index value of 2018
index_2018 = year.index(2018)
print(f"Index value of 2018: {year.index(2018)}")

#Counts the amount of tuples
print(f"Length of the tuple: {len(year)}")
