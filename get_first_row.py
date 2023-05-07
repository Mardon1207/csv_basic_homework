from csv import reader
#Define function,Get coloumn names from a csv file
def get_column_names(data):   
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f=open('data.csv')
    r=reader(f,delimiter=',')
    return list(r)[1]
print(get_column_names('data.csv'))
    
    
# Read the csv file