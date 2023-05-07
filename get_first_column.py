from csv import reader
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=open('data.csv')
    r=reader(f,delimiter=',')
    lst=[]
    for i in list(r):
        lst.append(i[1])
    return lst
print(get_first_column('data.csv'))
    
# Read the csv file