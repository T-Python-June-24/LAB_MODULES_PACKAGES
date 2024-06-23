from datetime import datetime

def print_current_date():
    ''' 
    This function uses the datetime module to retrieve the current date
    and then prints it in both default format and MM/DD/YYYY.
    '''
    current_date = datetime.now().date()
    formatted_date = current_date.strftime('%m/%d/%Y')
    print(f"\033[32m Current date in default ISO 8601 format: {current_date}")
    print(f"\033[32m Current date in format MM/DD/YYYY: {formatted_date}")
