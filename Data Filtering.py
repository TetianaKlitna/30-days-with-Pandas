import pandas as pd

""" Big Countries
    A country is big if:
    it has an area of at least three million (i.e., 3000000 km2), or
    it has a population of at least twenty-five million (i.e., 25000000).
"""
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    condition = (world["area"] >= 3000000) | (world["population"] >= 25000000)
    filtered_world = world[condition]
    return filtered_world[["name", "population", "area"]]

# Recyclable and Low Fat Products
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    condition = (products["low_fats"] == "Y") & (products["recyclable"] == "Y") 
    return products[condition][["product_id"]]

# Customers Who Never Order
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers["id"].isin(orders["customerId"])]\
                         [["name"]]\
                         .rename(columns = {"name": "Customers"})

# Write a solution to find all the authors that viewed at least one of their own articles.
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views["author_id"] == views["viewer_id"]] \
                .drop_duplicates(subset = ["author_id"]) \
                .rename(columns = {"author_id": "id"}) \
                .sort_values(by = "id", ascending = True) \
                [["id"]]
    