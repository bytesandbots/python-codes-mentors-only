class Section:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
    def getLength(self):
        return abs(self.end - self.start) + 1

n = int(input()) #number of cows

cowsLine = input()
cows = []

for i in cowsLine:
    cows.append(int(i))

infectedCows = 0
if(n == 1):
    infectedCows = cows[0]
elif (cows[0] == 1 and cows[1] == 0) or (cows[n - 1] == 1 and cows[n - 2] == 0):
    #if either the cow on the far left or the cow on the far right is infected on the first day
    for cow in range (n):
        if int(cows[cow]) == 1:
            infectedCows += 1
else:
    #create the section
    i = 0
    sections = []
    while i < len(cows):
        sectionStart = None
        sectionEnd = None
        #find the beginning
        while i < len(cows):
            if cows[i] == 1:
                sectionStart = i
                break
            i += 1
        i += 1
        #find the end
        while i < len(cows):
            if cows[i] == 0:
                sectionEnd = i-1
                break
            i += 1
        else:
            sectionEnd = i-1
        sections.append(Section(sectionStart, sectionEnd))
    #analyze the sections
    #find the smallest section
    i = 1
    smallestSection = 0
    while i < len(sections):
        if sections[i].getLength() < sections[smallestSection].getLength():
            smallestsSection = i
        i += 1
    diff = 0
    if sections[smallestSection].getLength() % 2 == 0:
        diff = sections[smallestSection].getLength() - 2
    else:
        diff = sections[smallestSection].getLength() - 1    
    #calculate the minimum number of infected cows
    for section in sections:
        infectedCows = infectedCows + section.getLength() - diff
        
print(infectedCows)