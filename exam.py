from csv_ical import Convert
import pandas as pd

def new_event(ics_file, id):
    def format(date):
        dt = date.split("-")
        return f"{dt[0]}/{dt[1]}/{dt[2]}" 



    convert = Convert()
    convert.CSV_FILE_LOCATION = 'test.csv'
    convert.SAVE_LOCATION = ics_file

    # Read the .ics file
    convert.read_ical(convert.SAVE_LOCATION)

    # Create the CSV object and save it at the specified location
    convert.make_csv()
    convert.save_csv(convert.CSV_FILE_LOCATION)

    df = pd.read_csv("test.csv", header=None)
    df2 = pd.read_csv("base.csv")

    for index, row in df.iterrows():
        stuff = row[0].split()
        if "Exam" in stuff[1]:
            subject, start, end = stuff[0], row[1].split("+")[0], row[2].split("+")[0]

            start = format(row[1].split("+")[0])
            end = format(row[2].split("+")[0])

            new_row = {
                "Event": f"{subject} exam",
                "Start": start,
                "End": end
                }
            df2.loc[len(df2)] = new_row

    df2.to_csv(f"events_{id}.csv")

new_event("jensen.ics", 1712009148)

