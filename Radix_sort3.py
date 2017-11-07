data = [209, 383, 100, 911, 25, 3]
num_digits = 3
print(data)

for i in range(0, num_digits):

    if i == 0:
        for j in range(0, len(data)):
            for k in range(0, len(data)):

                if data[j] % 10 < data[k] % 10:
                    data[j], data[k] = data[k], data[j]
        #print(data)

    if i == 1:
        for j in range(0, len(data)):
            for k in range(0, len(data)):

                if (data[j] / 10) % 10 < (data[k] / 10) % 10:
                    data[j], data[k] = data[k], data[j]
        #print(data)

    if i == 2:

        for j in range(0, len(data)):
            for k in range(0, len(data)):

                if (data[j] / 100) < (data[k] / 100):
                    data[j], data[k] = data[k], data[j]
        #print(data)

print(data)
