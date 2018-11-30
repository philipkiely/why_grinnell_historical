
class Alum:

    def __init__(self, data):
        print(data)
        self.id = int(data[0])
        self.name = data[1]
        self.class_year = int(data[2])
        self.complete = True
        try: #complete entry
            self.origin = data[3]
            self.distance = int(data[4])
            self.distance_category = int(data[5])
        except: #no distance, valueerror on int()
            self.origin = None
            self.distance = None
            self.distance_category = None
            self.complete = False #missing substantial data
        self.reasons = data[6]
        if data[7] != "":
            self.reason1 = reasons[data[7]]
        if data[8] != "" and data[8] != "\n": #if there is a second reason
            self.reason2 = reasons[data[8][:-1]] #strip newline
        else:
            self.reason2 = None
        if data[6] == "": #reasons section missing
            self.reasons = None
            self.reason1 = None
            self.reason2 = None
            self.complete = False

    def printfields(self):
        print(self.id, self.name, self.class_year, self.origin, self.distance, self.distance_category, self.reasons, self.reason1, self.reason2, self.complete)

if __name__=="__main__":
    reasons = {"Financial Aid": 1,
               "Alumni/Student Connection": 2,
               "Academic Reputation": 3,
               "Athletics": 4,
               "Campus Visit": 5,
               "Grinnell Admissions": 6,
               "High School Recommendation": 7,
               "Location": 8,
               "Student Life": 9}
    file = open('alumni.csv', 'r')
    alumni = []
    dex = 0
    for line in file:
        if dex == 0:
            dex += 1
            continue
        data = line.split(",")
        A = Alum(data)
        alumni.append(A)
        dex += 1
    complete = 0
    c_alumni = []
    for alum in alumni:
        #alum.printfields()
        if alum.complete:
            complete += 1
            c_alumni.append(alum)
    print(complete)
    d1 = d2 = d3 = 0
    for alum in c_alumni:
        if alum.distance_category == 1:
            d1 += 1
        elif alum.distance_category == 2:
            d2 += 1
        else:
            d3 += 1
    print(d1, d2, d3)
