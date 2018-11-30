
class Alum:

    def __init__(self, data):
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

def pprint(counts, size):
    r = dict(zip(reasons.values(),reasons.keys()))
    lst = []
    for key in counts:
        lst.append((r[key], counts[key]/size))
    lst.sort(key=lambda x: x[1], reverse=True)
    for i in lst:
        print(i)


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
    d_alumni = [[],[],[]]
    year1 = year2 = year3 = 0
    for alum in c_alumni:
        if alum.distance_category == 1:
            d_alumni[0].append(alum)
            year1 += alum.class_year
        elif alum.distance_category == 2:
            d_alumni[1].append(alum)
            year2 += alum.class_year
        else:
            d_alumni[2].append(alum)
            year3 += alum.class_year
    for lst in d_alumni:
        counts = {}
        for alum in lst:
            try:
                counts[alum.reason1] = counts[alum.reason1] + 1
            except: #new entry
                counts[alum.reason1] = 1
            try:
                counts[alum.reason2] = counts[alum.reason2] + 1
            except:
                if alum.reason2 is not None:
                    counts[alum.reason2] = 1
        print("new set: ", len(lst))
        pprint(counts, len(lst))
    print("d1 year: ", int(year1/len(d_alumni[0])))
    print("d2 year: ", int(year2/len(d_alumni[1])))
    print("d3 year: ", int(year3/len(d_alumni[2])))
    years = []
    for alum in c_alumni:
        years.append(alum.class_year)
    print((min(years),  max(years)))
    decades = {}
    for i in range(4, 11):
        dec = 1900 + i*10
        ndec = 1910 + i*10
        lst = []
        for alum in c_alumni:
            if alum.class_year >= dec and alum.class_year < ndec:
                lst.append(alum)
        decades[dec] = lst
        print(dec, len(lst))
    for dec in decades:
        counts = {}
        lst = decades[dec]
        for alum in lst:
            try:
                counts[alum.reason1] = counts[alum.reason1] + 1
            except: #new entry
                counts[alum.reason1] = 1
            try:
                counts[alum.reason2] = counts[alum.reason2] + 1
            except:
                if alum.reason2 is not None:
                    counts[alum.reason2] = 1
        print("new set: ", dec, "({})".format(len(lst)))
        pprint(counts, len(lst))
