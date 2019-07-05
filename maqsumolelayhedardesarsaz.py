counter = 0
inp = int(input())
if (inp >= 1 and inp <= 5000):
    for i in range(1, inp + 1):
        for o in range(1, i + 1):
            if (i % o == 0):
                counter = counter + 1
print(counter, " ", counter + inp)
