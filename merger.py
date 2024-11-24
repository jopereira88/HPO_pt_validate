import pandas as pd
import sys

if __name__=='__main__':
    main_translation=sys.argv[1]
    batch_translation=sys.argv[2]

#Run Arguments - CHANGE IF NEEDED
verbose=False
overwrite=False 

#Main translation sheet
df1 = pd.read_table(main_translation,index_col=False)

#Value dataframe
path=batch_translation
df2 = pd.read_csv(path, sep=';')


# Merge df1 with df2 on the 'key' column (left join keeps all rows in df1)
df_merged = pd.merge(df1, df2[['subject_id', 'translation_value', 'translation_status'\
    ,'translator', 'translator_expertise', 'comment' ,'translation_date']], on='subject_id', how='left')

if verbose:
    print(df_merged.columns)

# Update x columns in df1 with y from df2, if present

df_merged['translation_value_x'] = df_merged['translation_value_y'].combine_first(df_merged['translation_value_x'])
df_merged['translation_status_x'] = df_merged['translation_status_y'].combine_first(df_merged['translation_status_x'])
df_merged['translator_x'] = df_merged['translator_y'].combine_first(df_merged['translator_x'])
df_merged['translator_expertise_x'] = df_merged['translator_expertise_y'].combine_first(df_merged['translator_expertise_x'])
df_merged['comment_x'] = df_merged['comment_y'].combine_first(df_merged['comment_x'])
df_merged['translation_date_x'] = df_merged['translation_date_y'].combine_first(df_merged['translation_date_x'])

# 4. Drop the 'new_value' column (optional, depends on whether you want to keep it)
df_updated = df_merged.drop(columns=['translation_value_y', 'translation_status_y',
       'translator_y', 'translator_expertise_y', 'comment_y',
       'translation_date_y'])
df_updated=df_updated.rename(columns={'translation_value_x':'translation_value','translation_status_x':'translation_status',
    'translator_x':'translator','translator_expertise_x':'translator_expertise','comment_x':'comment','translation_date_x':'translation_date'})

if verbose:
    print(df_updated['source_value'][df_updated['translation_status']=='CANDIDATE'])

if not overwrite:    
    df_updated.to_csv(f'{main_translation}_update', sep='\t', index=False)
else:
    df_updated.to_csv(main_translation, sep='\t', index=False)
