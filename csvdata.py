import csv
import os


def main():pass
    # Check if the CSV file exists
    #folder_check()

def folder_check():
    if not os.path.exists('user_data.csv'):
        # Create the CSV file
        with open('user_data.csv', 'w') as file:
            pass

def save_user(chat_id, username):
    folder_check()
    if not check_duplicate(chat_id):
        # If not a duplicate, save the user's data
        with open('user_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([chat_id, username])

def check_duplicate(chat_id):
    with open('user_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0 and row[0] == str(chat_id):
                return True
    return False



if __name__ == "__main__":
    main()
