import numpy as np
import pandas as pd
import json


def getactivity(infile, outfile):
    df = pd.read_csv(infile, index_col="timestamp_excel", usecols=["timestamp_excel", "motionStatus"])
    df.index = pd.to_datetime(df.index)
    dates = np.unique(df.index.date)
    start = df.index[0]
    activity = pd.DataFrame(0, index=dates, columns=['duration'])
    for i, r in df.iterrows():
        if r['motionStatus'] == 1:
            activity.loc[i.date(), 'duration'] += (i - start).seconds / 3600
        start = i
    activity_json = {}
    for i, r in activity.iterrows():
        activity_json[i.strftime("%m-%d-%Y")] = r['duration']
    with open(outfile, 'w') as f:
        json.dump(activity_json, f, indent=4)
    return activity_json


def summarize(outfile, **kwargs):
    summary = {}
    for date in liv:
        famdur = fam.get(date, 0)
        kitdur = kit.get(date, 0)
        livdur = liv[date]
        mbtdur = mbt.get(date, 0)
        mbddur = mbd.get(date, 0)
        totaldur = famdur + kitdur + livdur + mbtdur + mbddur
        summary[date] = {
            "familyroom": famdur / totaldur * 24,
            "kitchen": kitdur / totaldur * 24,
            "livingroom": livdur / totaldur * 24,
            "masterbathroom": mbtdur / totaldur * 24,
            "masterbedroom": mbddur / totaldur * 24
        }   # portion of the day (in hours) spent in each room
    with open(outfile, 'w') as f:
        json.dump(summary, f, indent=4)


fam = getactivity("Dump 2020-01-17/Family-room-Motion-Sensor.csv", "Processed/familyroom_out.json")
kit = getactivity("Dump 2020-01-17/Kitchen-Motion-Sensor.csv", "Processed/kitchen_out.json")
liv = getactivity("Dump 2020-01-17/Living-room-Motion-Detector.csv", "Processed/livingroom_out.json")
mbt = getactivity("Dump 2020-01-17/Master-Bathroom-Motion-Sensor.csv", "Processed/masterbathroom_out.json")
mbd = getactivity("Dump 2020-01-17/Master-Bedroom-Motion-Sensor.csv", "Processed/masterbedroom_out.json")
summarize("Processed/activitysummary_out.json", fam=fam, kit=kit, liv=liv, mbt=mbt, mbd=mbd)
