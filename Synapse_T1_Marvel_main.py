# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

jumbled_superheroes = ['DocToR_sTRAngE', 'sPidERmaN', 'MoON_KnigHT', 'caPTAIN_aMERIca', 'hULK']
decoded_name = []
indices = []
name_lengths = []
s=""

for s in jumbled_superheroes:
    s = s.lower()
    s = s.replace('_', ' ')
    decoded_name.append(s)
#print("Decoded_names:",decoded_name)

for i,s in enumerate(jumbled_superheroes):
    indices.append(i)
#print("Indices:", indices)

func = lambda str: len(str)
name_lengths = map(func, jumbled_superheroes)
#print("Name lengths:", list(name_lengths))

decoded_name.sort(key=func)
#print(decoded_name)

print("Phase 5 kickoff list:")
i=1
for s in decoded_name:
    print(i,".",s.title())
    i=i+1