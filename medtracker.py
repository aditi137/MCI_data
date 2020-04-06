import json

medtracker_out_json = {
    'stamp': 1111111,  # epoch timestamp (1/1/20 - 1/10/20 daily 23:59:59 GMT)
    'missed': 7  # 0=None, 1=Morning, 2=Afternoon, 3=Evening, 4=M+A, 5=M+E, 6=A+E, 7=M+A+E
}

# for a certain week denoted by stamp, which days of that week was the door opened
EVENT_MAP = {
    0: '',
    1: '',  # Sun
    2: '',  # Mon
    3: '',  # Sun Mon
    4: '',  # Tue
    5: '',  # Sun Tue
    8: '',  # Wed
    9: '',  # Sun Wed
    10: '',  # Mon Wed
    14: '',  # Mon Tue Wed
    16: '',  # Thu
    20: '',  # Tue Thu
    21: '',  # Sun Tue Thu
    24: '',  # Wed Thu
    31: '',  # Sun Mon Tue Wed Thu
    32: '',  # Fri
    33: '',  # Sun Fri
    34: '',  # Mon Fri
    40: '',  # Wed Fri
    42: '',  # Mon Wed Fri
    48: '',  # Thu Fri
    54: '',  # Mon Tue Thu Fri
    62: '',  # Mon Tue Wed Thu Fri
    63: '',  # Sun Mon Tue Wed Thu Fri
    64: '',  # Sat
    65: '',  # Sun Sat
    68: '',  # Tue Sat
    72: '',  # Wed Sat
    80: '',  # Mon Wed Thu Sat
    96: '',  # Fri Sat
    119: '',  # Sun Mon Tue Thu Fri Sat
    127: ''  # Sun Mon Tue Wed Thu Fri Sat
}


def loadjson():
    with open('Home2Data\\json Output\\medTrackerData.json') as f:
        meddata = json.load(f)
    events = set()
    for item in meddata:
        events.add(item['event'])
    print(events)


if __name__ == "__main__":
    loadjson()
