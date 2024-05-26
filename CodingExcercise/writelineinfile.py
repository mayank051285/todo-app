temperature = [10, 20, 30]

file = open('file.txt', 'w')

# for temp in temperature:
#     file.write(str(temp))
#     file.write("\n")

temperature = [str(temp) + "\n" for temp in temperature]
file.writelines(temperature)

file.close()