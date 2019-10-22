def create_dataframe(url):
    import pandas as pd
    data = pd.read_csv(url)
    return data

def test_create_dataframe(data, colunm_names):
    data_colunm = data.columns.tolist()
    colunm_check = False
    type_check = True
    row_check = False
    if len(colunm_names) == len(data_colunm):
        for x in data_colunm:
            if x in colunm_names:
                column_check = True
            else:
                column_check = False
                break                                                                                
    if colunm_check == True:
        for x in colunm_names:
            type_reference = type(data.loc[0, x])
            for y in data[x]:
                if type_reference != type(y):
                    type_check = False
                    break
    if colunm_check & type_check:
        if len(data.index.tolist) >= 10:
            return True
    return False
