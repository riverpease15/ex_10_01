file_name = input("Enter file: ")
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
handle = open(file_name)

emails = {}

for line in handle :
    line.rstrip()
    if not line.startswith("From ") : continue
    line = line.split()
    email = line[1]
    emails[email] = emails.get(email,0) + 1

lst = []
for key, value in emails.items() :
    lst.append((value, key))

lst.sort(reverse = True)
print(lst[0])
