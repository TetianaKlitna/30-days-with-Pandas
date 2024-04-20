import pandas as pd

# Find the IDs of the invalid tweets. The tweet is invalid if the number of characters 
# used in the content of the tweet is strictly greater than 15.
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets["content"].str.len() > 15] \
            [["tweet_id"]]

"""
Calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and 
the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.
"""
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees.apply(
        lambda row: row["salary"] 
        if row["employee_id"] % 2 == 1 and not row["name"][:1] == "M" else 0,
    axis=1)
    return employees[["employee_id", "bonus"]] \
            .sort_values(by = "employee_id", ascending = True) 

# Fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by = "user_id", ascending = True)

# Find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. 
# Type I Diabetes always starts with DIAB1 prefix.
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[( patients["conditions"].str.contains(" DIAB1") ) \
                   |(patients["conditions"].str.startswith("DIAB1") )]

# prefix starts with letter
# alowed symbols ['_', '.', '-']
# contains '@leetcode.com'
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]  