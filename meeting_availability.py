from datetime import datetime, timedelta
from dateutil import parser

def generate_time_blocks(input_text, time_interval_minutes=60):
    try:
        # Parse the input dates and times
        parsed_times = [parser.parse(time.strip()) for time in input_text.split(',')]

        # Sort the parsed times
        sorted_times = sorted(parsed_times)

        # Generate time blocks with flexible interval
        time_blocks = []
        for start_time, end_time in zip(sorted_times, sorted_times[1:]):
            day_date = start_time.strftime("%A, %B %d")
            time_block = f"{start_time.strftime('%I:%M%p')} - {end_time.strftime('%I:%M%p')} EST"
            time_blocks.append(f"{day_date}\n- {time_block}")

            # Add flexible interval
            start_time += timedelta(minutes=time_interval_minutes)

        return time_blocks

    except ValueError as e:
        return f"Error: {e}. Please check your input format."

# Example usage:
input_text = input("Enter multiple dates and times separated by commas: ")
interval = int(input("Enter the time interval between blocks in minutes (default is 60): ") or 60)

formatted_blocks = generate_time_blocks(input_text, interval)

# Print the formatted blocks
for block in formatted_blocks:
    print(block)

# The script is designed to be flexible in terms of input format, but here are a few guidelines for optimal input:

# Date and Time Format: While the script is flexible, using a standard format for dates and times can help ensure accurate parsing. For example, "YYYY-MM-DD HH:MM AM/PM" or any other format that the dateutil.parser library can handle.
# Example: "2023-12-15 10:30 AM, 2023-12-16 14:00, 2023-12-17 16:30"
# Comma Separation: Separate each date and time entry with a comma. This is the delimiter used to split the input string into individual date and time entries.
# Example: "2023-12-15 10:30 AM, 2023-12-16 14:00, 2023-12-17 16:30"
# Time Interval: If you want to specify a custom time interval between blocks, enter it when prompted. Press Enter without entering a value to use the default interval (60 minutes).
# Example: "Enter the time interval between blocks in minutes (default is 60): 30"
# Here's an example of how you might run the script:
#
# Enter multiple dates and times separated by commas: 2023-12-15 10:30 AM, 2023-12-16 14:00, 2023-12-17 16:30
# Enter the time interval between blocks in minutes (default is 60): 30
