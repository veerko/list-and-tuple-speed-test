


# tuples is much faster, so to prove it we are going to do a test 

#list speed test
import timeit
#list speed is slower since its divided 
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', nummber=10000000))


#tuple speed test
#tuple is faster since its stored in 1 block memory
print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', nummber=10000000))