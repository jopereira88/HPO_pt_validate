import pandas as pd
import sys

def split_csv(fpath, nrows):
    '''Splits a .tsv file on fpath, in separate files
    on nrows size data frames'''
    df=pd.read_table(fpath, index_col=False)
    # Calculate the number of splits needed
    num_splits = len(df) // nrows + (1 if len(df) % nrows > 0 else 0)
    # Iterate over the number of splits and write to new csv files
    
    for i in range(num_splits):
        start_row = i * nrows
        end_row = (i + 1) * nrows
        split_df = df.iloc[start_row:end_row]
        
        # Create a new file name
        split_file_name = f'HPO_pt_{i + 1}.csv'
        
        # Save the split DataFrame to a new csv file
        split_df.to_csv(split_file_name,sep=';', index=False)
        print(f'Saved {split_file_name}')

if __name__=='__main__':
    try:
        path=sys.argv[1]
        rows=int(sys.argv[2])
        split_csv(path,rows)
    except Exception:
        print('Invalid argument(s)')
        sys.exit(1)


