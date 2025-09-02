
def transform_data(df):
    df = df[["country", "cases", "deaths", "recovered", "active"]]
    df["death_rate"] = (df["deaths"] / df["cases"]).round(2)
    return df