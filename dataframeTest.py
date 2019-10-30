def create_dataframe(url):
    import pandas as pd
    data = pd.read_csv(url)
    return data


def test_create_dataframe(data, column_names):
    data_column = data.columns.tolist()
    column_check = False
    type_check = True
    if len(column_names) == len(data_column):
        for x in data_column:
            if x in column_names:
                column_check = True
            else:
                column_check = False
                break
    if column_check:
        for x in column_names:
            type_reference = type(data.loc[0, x])
            for y in data[x]:
                if type_reference != type(y):
                    type_check = False
                    break
    if column_check & type_check:
        if len(data.index.tolist) >= 10:
            return True
    return False
