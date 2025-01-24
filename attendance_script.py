import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Scope for accessing Google Sheets and Drive
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Path to your credentials file
creds = ServiceAccountCredentials.from_json_keyfile_name(r'locker-system-448612-4eb084c1dc80.json', scope)

# Authenticate with Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet by its name
spreadsheet = client.open("Student Attendance")
sheet = spreadsheet.sheet1

# List of students
students = ["Rishi", "Rayan", "Saru", "Abi", "Venkat"]

# Function to update the attendance status in Google Sheets
def update_attendance(student_name, status, elapsed_time, final_status):
    # Find the student row
    cell = sheet.find(student_name)
    row = cell.row
    
    # Update attendance status, elapsed time, and final attendance
    sheet.update_cell(row, 2, status)  # Column 2 for status (Present/Absent)
    sheet.update_cell(row, 3, elapsed_time)  # Column 3 for elapsed time
    sheet.update_cell(row, 4, final_status)  # Column 4 for final attendance

# Function to handle the locker and attendance system
def attendance_system():
    print("Starting attendance system...")
    for student_name in students:
        print(f"Opening locker for {student_name}")
        open_time = time.time()  # Record the time when locker is opened
        
        # Prompt user for attendance input
        print(f"Locker opened for {student_name}. Please enter True (Present):")
        
        # Get user input with a 40-second limit
        status = None
        start_time = time.time()
        while time.time() - start_time < 40:
            status = input("Enter 'True' for Present: ").strip()
            if status.lower() == "true":
                break
        
        # Calculate elapsed time
        elapsed_time = round(time.time() - open_time, 2)  # Time in seconds
        
        # Determine final attendance based on input and elapsed time
        if status and status.lower() == "true" and elapsed_time <= 40:
            final_status = "Present"
        else:
            final_status = "Absent"
        
        # Default status for column 2
        attendance_status = "True" if final_status == "Present" else "False"
        
        # Update attendance in Google Sheet
        update_attendance(student_name, attendance_status, elapsed_time, final_status)
        print(f"Updated attendance for {student_name}: Status: {attendance_status}, Time: {elapsed_time}s, Final: {final_status}")

# Run the attendance system
attendance_system()