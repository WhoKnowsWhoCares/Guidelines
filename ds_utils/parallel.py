'''
Скрипт содержит пример кода для многопоточной обработки списка файлов
'''

from joblib import Parallel, delayed

# Initialzie dataframe for collecting features for all stocks
df_all_stocks = pd.DataFrame()
# Initialize the dictionary for model estimates
model_dict = {}

def preprocessor(list_order_book_file_train, is_train = True):
    df = pd.DataFrame()
    # Parrallel for loop
    def for_joblib(file_book):
        
        book_stock = pd.read_parquet(file_book)
        stock_id = file_book.split('=')[1]
        trade_stock =  pd.read_parquet(file_book.split('=')[0].replace('book', 'trade') + '=' + stock_id)
    
#         df_tmp = pd.merge(book_stock, trade_stock, on = 'row_id', how = 'left')
        df_stock_book_features = generate_features_book_stock_bygroups(book_stock)
        df_stock_trade_features = generate_features_trade_stock_bygroups(trade_stock)

        df_stock_features = df_stock_book_features.join(df_stock_trade_features).fillna(0)
        features_names = df_stock_features.columns
        df_stock_features.reset_index(level=0, inplace=True)
        df_stock_features['row_id'] = df_stock_features["time_id"].apply(lambda x:f'{stock_id}-{x}')

        df_stock_train = train[train["stock_id"]==int(stock_id)]
        df_stock = df_stock_features.merge(df_stock_train[["time_id", "target"]], on = ["time_id"], how="left")

        # Fit linear regression with generated features
#         reg = LinearRegression().fit(df_stock.loc[:,features_names], df_stock['target'], sample_weight=1/np.square(df_stock["target"]))
#         model_dict[stock_id] = reg

        # in-sample fit
#         df_stock["pred_lr"] = reg.predict(df_stock.loc[:,features_names])

        df_stock["stock_id"] = int(stock_id)

        # Return the merge dataframe
        return df_stock
    
    # Use parallel api to call paralle for loop
    df = Parallel(n_jobs = -1, verbose = 1)(delayed(for_joblib)(file) for file in list_order_book_file_train)
    # Concatenate all the dataframes that return from Parallel
    df = pd.concat(df, ignore_index = True)
    return df

df_all_stocks = preprocessor(list_order_book_file_train[0:11])