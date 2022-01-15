# %%
import pandas as pd
import sqlite3


con = sqlite3.connect('fk8.sqlite')

tc_df = pd.read_sql(
    'SELECT * '
    'FROM gf_boost',
    con=con
)

sql = 'Select frame,' \
      '"G.Lat",' \
      '"G.Long"' \
    'from highest_gforce_boost_filtered'

sg_scatter = pd.read_sql(sql, con)