



file = open("oupt.txt","r")
# for line in file:
#     print(line)


content_line = file.readlines()
print(content_line)


if any("Stopped" in s for s in content_line) == False:
    print("something")
#
# for line in content_line:
#     if 'stopped' in line:
#         flag = 1
# if flag == 1:
#     for line in content_line:
#         if "stopped" in line:
#             print(line)
#
