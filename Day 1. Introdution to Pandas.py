import pandas as pd

# Create a DataFrame from List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

# Return the result as an array: [number of rows, number of columns]
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_rows, num_cols = players.shape
    return [num_rows, num_cols]

# Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3) 

#  Select the name and age of the student with student_id = 101
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]   

# Create a new column name bonus that contains the doubled values of the salary column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 2*employees["salary"]
    return employees

# Drop Duplicate Rows: some duplicate rows in the DataFrame based on the email column
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ["email"])

# Drop Missing Data: some rows having missing values in the name column.
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = ["name"])

# Modify the salary column by multiplying each salary by 2
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = 2 * employees["salary"]
    return employees

# Rename Columns
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id": "student_id", 
                             "first": "first_name", 
                             "last": "last_name",    
                             "age": "age_in_years"})

# The grade column is stored as floats, convert it to integer
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

# Fill in the missing value as 0 in the quantity column
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna(value={"quantity": 0})

# Reshape Data: Concatenate
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    frames = [df1, df2]
    return pd.concat(frames)

# Pivot the data so that each row represents temperatures for a specific month, 
# and each city is a separate column.
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

# Reshape the data so that each row represents sales data for a product in a specific quarter
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report,id_vars=['product'],var_name='quarter',value_name='sales')

# Method chaining enables us to perform operations on a DataFrame without breaking up 
# each operation into a separate line or creating multiple temporary variables. 
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100] \
           .sort_values(by = ["weight"], ascending = False) \
           [["name"]]