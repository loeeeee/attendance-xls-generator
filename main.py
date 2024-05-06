import os
import datetime
import holidays
import random

# Create a list of dates in the required format
def generate_dates(start_date, end_date):
    dates = []
    while start_date <= end_date:
        if start_date.weekday() < 5 and start_date not in holidays.country_holidays("CN"):  # Weekdays only
            dates.append(start_date.strftime('%m/%d/%Y'))
        start_date += datetime.timedelta(days=1)
    return dates
    
def create_folder_if_not_exists(folder_path: str) -> bool:
    # Return if the folder exists
    # It only create one folder at a time

    if not os.path.isfile(folder_path) and not os.path.isdir(folder_path):
        os.mkdir(folder_path)
        print("Folder does not exists. Creating a new one.")
        return True
    else:
        print("Folder exists. No further action.")
        return False

def generate_daily_attendance_record(date) -> str:
    start_time: float = random.gauss(9.3, 0.3)
    end_time: float = random.gauss(17.7, 0.3)

    start_hour = int(start_time)
    start_minute = int(start_time % 1 * 60)

    end_hour = int(end_time)
    end_minute = int(end_time % 1 * 60)
    return f"{date},{start_hour},{start_minute},{end_hour},{end_minute},"

def main() -> None:
    # Main VARs
    output_folder = "target/"
    start_date = datetime.datetime(2024, 3, 1)
    end_date = datetime.datetime.today() - datetime.timedelta(days=1)
    today = datetime.date.today()

    # Create target folder
    create_folder_if_not_exists(output_folder)
   
    # Get dates at work
    dates_at_work = generate_dates(start_date, end_date)

    # Generate attendance entries
    attendances = ["Date,Start time/hour,Start time/min,End time/hour,End time/min,Remark"]
    for i in dates_at_work:
        one_attendance = generate_daily_attendance_record(i)
        attendances.append(one_attendance)

    # The record
    attendances = "\n".join(attendances)
    save_path = os.path.join(output_folder, f"{today}.csv")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(attendances)

if __name__ == "__main__":
    main()