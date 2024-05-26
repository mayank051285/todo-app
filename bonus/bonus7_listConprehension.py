filename = ["1.doc", "1.report", "1.presentations"]

# Need to change the above list to below one.
# ["1-doc.txt", "1-report.txt", "1-presentations.txt"
# new_filename = []
# for items in filename:
#     j = ""
#     for i in items:
#         if i == ".":
#             i = "-"
#
#         j = j + i
#     j = j + ".txt"
#     new_filename.append(j)
#
# print(new_filename)

filename = [items.replace(".", "-") + ".txt" for items in filename]
print(filename)