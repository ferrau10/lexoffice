import sys
import json
from datetime import datetime, timedelta
import uuid


def validate_time_format(time_str, time_format):
    try:
        # Validates if a given time string matches the specified format.
        datetime.strptime(time_str, time_format)
        return True
    except ValueError:
        return False


def round_to_nearest_15_minutes(time_str, time_format):
    """
    Rounds a given time string to the nearest 15-minute interval.

    Args:
        time_str (str): The time string to round.
        time_format (str): The format of the time string.

    Returns:
        str: The rounded time string.
    """
    time = datetime.strptime(time_str, time_format)
    #Rounds the minutes to the nearest 15-minute interval.
    total_minutes = time.minute + (time.second / 60)
    rounded_minutes = round(total_minutes / 15) * 15
    rounded_time = time.replace(minute=int(rounded_minutes), second=0, microsecond=0)
    return rounded_time.strftime(time_format)


def validate_time_difference(start_time, end_time, time_format):
    start = datetime.strptime(start_time, time_format)
    end = datetime.strptime(end_time, time_format)
    time_difference = end - start
    if time_difference >= timedelta(minutes=15):
        return True
    else:
        return False


def generate_blocks(start_time, end_time, time_format):
    """
    Generates 15-minute blocks within the specified time range.

    Args:
        start_time (str): The start time.
        end_time (str): The end time.
        time_format (str): The format of the time strings.

    Returns:
        list: A list of dictionaries representing the 15-minute blocks.
    """
    start = datetime.strptime(start_time, time_format)
    end = datetime.strptime(end_time, time_format)
    block_list = []

    while start < end:
        block = {
            "block_start_time": start.strftime(time_format),
            "block_end_time": (start + timedelta(minutes=15)).strftime(time_format),
            "unique_id": str(uuid.uuid4()) #generate a random ID of which there less than one chance in a trillion for ID to repeat itself.
        }
        block_list.append(block)
        start += timedelta(minutes=15)

    return block_list


def main(time_format):
    if len(sys.argv) != 3:
        print("Usage: python script.py start-time end-time")
        return

    start_time = sys.argv[1]
    end_time = sys.argv[2]

    if not validate_time_format(start_time, time_format) or not validate_time_format(end_time, time_format):
        print("Invalid time format. Please provide time in 'YYYY-MM-DDTHH:MM:SSZ' format.")
        return

    rounded_start_time = round_to_nearest_15_minutes(start_time, time_format)
    rounded_end_time = round_to_nearest_15_minutes(end_time, time_format)

    if not validate_time_difference(rounded_start_time, rounded_end_time, time_format):
        print("The time difference between start and end times must be at least 15 minutes.")
        return

    blocks = generate_blocks(rounded_start_time, rounded_end_time, time_format)

    with open('output.json', 'w') as file:
        json.dump(blocks, file, indent=4)

    print("Output file 'output.json' generated successfully.")


time_format_zone = '%Y-%m-%dT%H:%M:%SZ'

if __name__ == '__main__':
    main(time_format_zone)
