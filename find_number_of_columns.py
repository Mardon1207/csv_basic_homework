from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=open('data.csv')
    r=reader(f,delimiter=',')
    return len(list(r)[0])
print(find_number_of_columns('data.csv'))
# Read the csv file