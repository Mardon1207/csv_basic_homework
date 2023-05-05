from csv import reader
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=open('data.csv')
    r=reader(f,delimiter=',')
    return len(list(r))
print(find_number_of_rows('data.csv'))
# Read the csv file

# Read the csv file
