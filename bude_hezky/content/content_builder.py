# Copyright mg. (https://stackoverflow.com/questions/2556108/rreplace-how-to-replace-the-last-occurrence-of-an-expression-in-a-string)
def rreplace(string, old, new, occurrence):
    li = string.rsplit(old, occurrence)
    
    return new.join(li)

def build_sunny_ranges(sunny_hours):
    sunny_ranges = []
    already_used_hours = []
    hour_window = 3

    for index, start_hour in enumerate(sunny_hours):
        if (start_hour in already_used_hours):
            continue

        end_hour = start_hour + hour_window
        end_hour_index = 1
        while (len(sunny_hours) > index + end_hour_index and end_hour == sunny_hours[index + end_hour_index]):
            already_used_hours.append(sunny_hours[index + end_hour_index])
            end_hour += hour_window
            end_hour_index += 1

        if (end_hour > 23):
            end_hour = 0

        sunny_ranges.append(f'{start_hour}:00 - {end_hour}:00')

    return sunny_ranges