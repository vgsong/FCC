class Tempo:
    def __init__(self, h, m, apm=None, weekd=None, days=None):
        self.h = h
        self.m = m
        self.apm = apm if apm is not None else ""
        self.weekd = weekd if weekd is not None else ""
        self.days = days if days is not None else ""


def add_time(horas, ahoras, wd=None):
    def get_horas(x):
        pos = x.find(":")
        h = x[:pos]
        m = x[pos + 1:pos + 3]
        apm = x[-2:]

        return int(h), int(m), str(apm)

    def to_twentyf(x, apm):
        if apm == "PM" and x == 12:
            return x

        elif apm == "PM":
            return x + 12

        elif apm == "AM" and x == 12:
            return x - 12

        else:
            return x

    def min_spill(x):
        # where 1 is the min to hour
        if x > 59:
            return x % 60, 1

        else:
            return x, 0

    def to_twelve(x):
        if x > 12:
            return x - 12

        elif x == 0:
            return x + 12

        else:
            return x

    def final_apm(x):
        if x > 11:
            return "PM"

        else:
            return "AM"

    wd_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # breakdown string and create t1 and t2 object class and store values
    t1 = Tempo(get_horas(horas)[0], get_horas(horas)[1], get_horas(horas)[2])
    t2 = Tempo(get_horas(ahoras)[0], get_horas(ahoras)[1])

    # converts to 24hours
    th = to_twentyf(t1.h, t1.apm)

    # adds ahoras minutes into horas
    tm = t1.m + t2.m

    # get 24hours final hour and add hour spill from minutes
    th += min_spill(tm)[1]

    # then adds ahours into hour
    th += t2.h

    # get total days
    td = int(th / 24)

    # for debug, uncomment if necessary
    #     print("total hours: "+ str(th))
    #     print("total days: "+ str(td))
    #     print("total minutes: " + str(tm%60))
    #     print("total hours spillover: "+ str(th%24))
    #     print("final APM: " + final_apm(th%24))

    if wd == None:

        fh = Tempo(to_twelve(th % 24), tm % 60, final_apm(th % 24), None, str(td))

        if td == 0:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(fh.m) + " " + fh.apm

        elif td == 1:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(fh.m) + " " + fh.apm + " (next day)"

        elif td > 1:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(fh.m) + " " + fh.apm + " (" + fh.days + " days later)"


    else:
        # obtain weekday string and add the days passed
        tweekd = wd_list[(wd_list.index(wd.capitalize()) + int(td)) % 7]
        fh = Tempo(to_twelve(th % 24), tm % 60, final_apm(th % 24), tweekd, str(td))

        if td == 0:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(fh.m) + " " + fh.apm + ", " + fh.weekd

        elif td == 1:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(fh.m) + " " + fh.apm + ", " + fh.weekd + " (next day)"

        elif td > 1:
            return "{:01d}".format(fh.h) + ":" + "{:02d}".format(
                fh.m) + " " + fh.apm + ", " + fh.weekd + " (" + fh.days + " days later)"

