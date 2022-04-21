# %%
# categories = ['frame', 'time_ms', 'time_us', 'RPM', 'VSS', 'Gear', 'PTANK', 'MAP',
#               'BP', 'BP CMD', 'TPedal', 'TPlate', 'AFM.v', 'AFM Hz', 'AFM', 'AFM.c',
#               'AIRC', 'EGR', 'IAT', 'IAT2', 'ECT', 'ECT2', 'PA', 'Oil.Press',
#               'CVT.Temp', 'INJ', 'INJ Bank 2', 'DUTY', 'DIFP', 'DIFPCMD', 'FuelP',
#               'IGN', 'CAM', 'CAMCMD', 'EXCAM', 'EXCAMCMD', 'WG', 'WGCMD', 'VTS',
#               'SVS', 'Purge', 'ACCL', 'BC Duty', 'AF', 'AF Bank 2', 'AF.Corr',
#               'Wide.V', 'Wide', 'AFCMD', 'AFCMD Bank 2', 'S.TRIM', 'L.TRIM',
#               'S.TRIM Bank 2', 'L.TRIM Bank 2', 'Trim', 'Fuel Status',
#               'Fuel Status Bank 2', 'Ethanol', 'K.Level', 'K.Retard', 'K.Retard.1',
#               'K.Retard.2', 'K.Retard.3', 'K.Retard.4', 'K.Control', 'Ign.Limit',
#               'K.Count', 'K.Count.1', 'K.Count.2', 'K.Count.3', 'K.Count.4',
#               'K.Count.5', 'K.Count.6', 'BAT', 'Cat.T', 'ABS.LF', 'ABS.RF', 'ABS.LR',
#               'ABS.RR', 'Clutch.Pos', 'Brake.Press', 'Steer Ang', 'Steer Trq',
#               'G.Lat', 'G.Long', 'G.Z', 'Yaw', 'Eco', 'Fuel Used', 'TC.V',
#               'TC.ECUSlip', 'TC.R', 'TC.LF', 'TC.RF', 'TC.LR', 'TC.RR', 'TC.Slip',
#               'TC.Turn', 'TC.OverSlip', 'TC.Out']
#
# # tc_df =


from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import os
import sqlite3
import pandas as pd
import plotly.express as px
import sqlite3
import plotly.graph_objs as go
import plotly.offline as pyo

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
con = sqlite3.connect('data/fk8_data.sqlite')


def fix_cols(df):
    """remove uppercases and periods from col names"""
    new_cols = []

    cols = df.columns

    for col in cols:
        col = col.lower().replace('.', '_')
        col = col.lower().replace(' ', '_')
        new_cols.append(col)

    df.columns = new_cols

    return df


# %%
for f in os.listdir('data'):
    if f.endswith('csv'):
        name = os.path.basename(f)
        df = pd.read_csv(f'data/{f}')
        df.to_json(f'data/{f[:-4]}.json')
        # print(f'{f[:-3]}')
# %%
df = pd.read_csv('data/tc_disp.csv')
df.to_json('tc_disp.json')

# %%


# %%

df = pd.read_sql(
    'SELECT '
    'time_ms'
    ', g_lat'
    ', g_long'
    ', steer_ang'
    ' FROM gfb'
    ,
    con=con)

print(df['steer_ang'].unique())
# %%
df['comb'] = df[['g_lat', 'g_long']].apply(lambda x: ', '.join(x.astype(str)), axis=1)

fig = px.scatter(
    df,
    x='g_lat',
    y='g_long',
    animation_frame='time_ms',
    text=df['comb']
)
pyo.plot(fig)
# %%
# x = [df['g_lat']]
# y = [df['g_long']]

update_men = [
    {
        'active': 1,
        "buttons": [
            {
                "args": [None, {
                    "frame": {"duration": 50, "redraw": False}, 'mode': 'immediate',
                    "fromcurrent": True, "transition": {"duration": 50}
                }
                         ],
                "label": None,
                "method": "animate"
            },
            {
                "args": [[None], {
                    "frame": {"duration": None, "redraw": False},
                    "mode": "immediate",
                    "transition": {"duration": 0}
                }
                         ],
                "label": None,
                "method": "animate"
            }
        ]
    }]

layout = go.Layout(updatemenus=update_men, xaxis={'range': [-0.5, 1.5]}, yaxis={'range': [-0.5, 1.5]})

fig.update_layout(layout)

fig.update_traces(marker=dict(size=20), textposition='top center', textfont_size=20)
pyo.plot(fig)

# %%
# fig_html = fig.to_html()
# #
# with open('fig__.html', 'w') as f:
#     f.write(fig_html)

fig.write_html('scatter_js.html', auto_play=False)
# %%

# con = sqlite3.connect('data/fk8_data.sqlite')
#
# df = pd.read_sql(
#     'SELECT map, '
#     'bp, '
#     '"bp cmd", '
#     'cam, '
#     'camcmd, '
#     'excam, '
#     'excamcmd, '
#     'wg, '
#     'wgcmd'
#     ', af'
#     ', afcmd'
#     ' FROM long_term'
#     ' WHERE frame BETWEEN 100000 AND 110000',
#     con
# )

df = pd.read_sql(
    'SELECT *'
    ' FROM long_term'
    ' WHERE frame BETWEEN 100000 AND 110000',
    con
)


def pct_diff(a, b, df=df):
    a = df[a]
    b = df[b]

    pct_diff = 100 * abs(b - a) / a
    return pct_diff


# df_bp['diff'] = pct_diff('map', 'bp cmd')

# df_bp['diff'].nlargest(5)
# df.head()

# ax_bp = df[['map', 'bp','bpcmd']]
# %%

# df = fix_cols(df)
# df.columns

# %%

fig = go.Figure()

# fig.add_trace(go.Scatter(x=df['frame'], y=df['map']))
# fig.add_trace(go.Scatter(x='frame', y='bp'))
# fig.add_trace(px.scatter(df, x='frame', y='bp',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='bp_cmd',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='cam',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='camcmd',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='excam',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='excamcmd',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='wg',type='scatter'))
# fig.add_trace(px.scatter(df, x='frame', y='wgcmd',type='scatter'))
fig_boost = px.line(df, y=['map', 'bp', 'bp_cmd'])
fig_cam = px.line(df, y=['cam', 'camcmd'])
fig_exh = px.line(df, y=['excam', 'excamcmd'])
fig_wg = px.line(df, y=['wg', 'wgcmd'])
fig_af = px.line(df, y=['af', 'afcmd'])
fig_knock = px.line(df, y=['k_retard_1', 'k_retard_2', 'k_retard_3', 'k_retard_4', 'k_retard'])
df_bp = df[['map', 'bp_cmd']]
df_af = df[['af', 'afcmd']]

# figaf = px.line(df_af)
# figbp = px.line(df_bp)

# pyo.plot(figaf)
pyo.plot(fig_knock)

# %%
pyo.plot(fig_boost)
# %%
pyo.plot(fig_exh)
pyo.plot(fig_wg)
pyo.plot(fig_cam)

# html = fig.to_html('long_one.html')

# with open('long_one.html', 'w+') as f:
#     f.write(html)
# %%


df['ms_corr'] = df['time_ms'] - 789410
df['s_corr'] = df['ms_corr'] / 1000
df['s_corr']

fig = make_subplots(rows=2, cols=2, shared_xaxes=True)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['wg'], name='Wastegate'),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['wgcmd'], name='Wastegate Command'),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['map'], name='MAP'),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['bp_cmd'], name='MAP Command'),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['bp'], name='Boost Pressure'),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['af'], name='A/F Ratio'),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['afcmd'], name='A/F Ratio Command'),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['s_trim'], name='S.Trim'),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['cam'], name='Cam Angle'),
    row=2, col=2
)

fig.add_trace(
    go.Scatter(x=df['s_corr'], y=df['camcmd'], name='Cam Angle Command'),
    row=2, col=2
)

# fig.update_layout(xaxis=dict(
#         rangeslider=dict(
#             visible=True
#         )
#     ), xaxis2={'rangeslider':{'visible':True}})

fig.update_layout(
    xaxis=dict(
        autorange=True, rangeslider=dict(autorange=True, thickness=0.05)
    ),
    xaxis2=dict(
        autorange=True, rangeslider=dict(autorange=True, thickness=0.05)
    )
)

# pyo.plot(fig)
# %%

fig.write_html('templates/multi_js1.html')

# %%
fig = go.Figure(data=[go.Table(
    header=dict(values=['Engine Retard', 'Degrees'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='center'),
    cells=dict(values=[df['k_retard'][0:5],  # 1st column
                       df['k_retard'].nlargest(5)],  # 2nd column
               line_color='darkslategray',
               fill_color='lightcyan',
               align='center'))
])

fig.update_layout(width=500, height=400)
pyo.plot(fig)

# %%
# con = sqlite3.connect('fk8_data.sqlite')

df = pd.read_sql(
    'SELECT *'
    ' FROM tc_disp',
    con
)
#
# fig = px.imshow(data=df['tc_slip'])
# fig = make_subplots(2, 1)
df['t'] = df['iat'] - df['iat2']
# fig.add_trace(go.Scatter(x=))
fig = px.density_heatmap(
    df,
    x='iat2',
    y='iat',
    z='t',
    histfunc='avg'
)

pyo.plot(fig)
# %%
fig = go.Figure(
    data=[go.Scatter(x=[df['g_lat'][0]], y=[df['g_long'][0]])],
    layout=go.Layout(
        xaxis=dict(range=[0, 1.5], autorange=False),
        yaxis=dict(range=[0, 1.5], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[df['g_lat'][i] for i in range(len(df.g_lat))],
                                      y=[df['g_lat'][i] for i in range(len(df.g_long))])]),
            # go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
            # go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])],
            #          layout=go.Layout(title_text="End Title"))
            ]
)

pyo.plot(fig)

# %%

df_iats = pd.read_sql(
    'SELECT * FROM iats2 WHERE tpedal > 90',
    con=con
)

# %%
fig = px.scatter(df_iats[210:511],
                 x='rpm',
                 y=['iat2', 'iat'],
                 range_y=[55, 65],
                 trendline='lowess'
                 )

t1 = px.scatter([df_iats[511:]],
                x='rpm',
                y=['iat2', 'iat'],
                range_y=[55, 65],
                trendline='lowess'
                )

# fig.add_trace()

pyo.plot(fig)
# %%

s1 = df[df['time_ms'].between(9726, 12352)][['iat2', 'iat', 'rpm', 'tpedal']][:-14].reset_index()

s2 = df[df['time_ms'].between(22345, 25221)][['iat2', 'iat', 'rpm', 'tpedal']].reset_index()

s1['run'] = '1'
s2['run'] = '2'

s12 = pd.concat([s1, s2], ignore_index=True)
print(s12)

fig = px.scatter(
    s1,
    x='rpm',
    y=['iat2', 'iat'])

fig = px.scatter(s1, x='rpm', y=['iat2', 'iat'])
fig2 = px.scatter(s2, x='rpm', y=['iat2', 'iat'])
# fig.add_scatter(s2, x=, y='iat2', )
# %%
# ses = s1.concat(s2, axis=1, ignore_index=True, sort=False)
# ses = s1.append(s2, ignore_index=True)


fig = make_subplots()

# trace1= go.Scatter(x=s1['rpm'],y=s1['iat'], mode='markers')
# trace2= go.Scatter(x=s2['rpm'],y=s2['iat'],connectgaps=True)
# fig = px.scatter(trace2)
# fig = go.Figure()
fig1 = px.scatter(s1, x='rpm', y=['iat2', 'iat'], trendline='lowess')
# fig.add_trace(trace1)
# fig = px.scatter(s1, x='rpm', y=['iat2', 'iat'], trendline='rolling')
# fig = px.scatter(s2, x='rpm', y=['iat2', 'iat'], trendline='lowess')
# fig2=px.scatter(s1, x='rpm', y=['iat2', 'iat'], trendline='lowess')

t1 = go.Scatter(
    x=s1['rpm'],
    y=s1['iat2']
)

t2 = go.Scatter(
    x=s1['rpm'],
    y=s1['iat']
)
fig = go.Figure()
fig.add_trace(t1)
fig.add_trace(t2)
# fig.add_trace([t2])
pyo.plot(fig)
# %%
fig = px.scatter(s2, x='rpm', y=['iat2', 'iat'], trendline='lowess')
l0 = s1['iat2'].to_list()
l1 = s1['iat'].to_list()
l2 = s2['iat2'].to_list()
l3 = s2['iat'].to_list()
l4 = s1['rpm'].to_list()
l5 = s2['rpm'].to_list()

pyo.plot(px.scatter(x=s1['rpm'], y=[l0, l1, l2, l3], labels=['Run 1 IAT2', '2', '3', '4']))
# fig.add_trace(go.Scatter(
#     x=s1['rpm'],y=s1['iat2'], mode='markers', name='first',type='scatter'))
# f=  px.scatter([s1, s2])
# pyo.plot(fig)

# %%
import plotly.figure_factory as ff

df = pd.read_sql('SELECT * FROM gfb', con)
df['bcorr'] = df['brake_press'] * 100 / df['brake_press'].max()

l = df[df['tc_r'] > 0]['tc_r']
print(l)
# %%

df = pd.read_sql('SELECT * FROM gfb', con)
d = px.scatter_ternary(a=df['steer_ang'], b=df['tc_r'], c=df['tpedal'])
# d = px.scatter_ternary(a=df['iat'], b=df['k_level'], c=df['iat2'])
g = px.line(df, x='frame', y=['tpedal', 'steer_ang'])

# g.add_vrect(l.index[0], l.index[-1], annotation_text='tc')
pyo.plot(d)

# %%
tc = [[1569, 1617],
      [1640, 1659],
      [1667, 1673],
      [1625, 1639],
      [1814, 1820],
      [2059, 2065],
      [2101, 2121],
      [2136, 2156],
      [2185, 2191],
      [2206, 2219],
      [2269, 2296],
      [2367, 2436],
      [2542, 2555],
      [2570, 2590],
      [2598, 2611],
      [2626, 2632],
      [2675, 2695]]
lf = [tc[i][0] for i in range(len(tc))]
ll = [tc[i][-1] for i in range(len(tc))]
z = list(zip(lf, ll))
# g.add_vrect(x0=lf, x1=ll)

# %%
# update_men = [
#     {
#         "buttons": [
#             {
#                 "args": ['shapes[i].visible' for i in shapes], [False]],
#                 "label": 'Update',
#                 "method": "relayout"
#             },
# {
#                 "args": ['shapes[0:16].visible', [True, True, True]],
#                 "label": 'Again',
#                 "method": "relayout"
#             }
#         ]
#     }]
# layout = go.Layout(updatemenus=update_men)
# g.update_layout(layout)
#
# pyo.plot(g)

df = pd.read_sql('SELECT * FROM gfb', con)

g = px.line(df, x='frame', y=['tpedal', 'steer_ang'])
# %%

for x in range(len(tc)):
    g.add_vrect(x0=tc[x][0], x1=tc[x][1],
                fillcolor='black', opacity=0.15, line_width=0, visible=True)

g.update_layout(
    xaxis=dict(
        range=[0, 3200], rangeslider=dict(autorange=True)
    ),
    showlegend=True,
    title='Activity of traction control as steering angle and throttle position vary'
)

pyo.plot(g)

# %%

g.write_html('tc.html', include_plotlyjs=False)


def add_tc():
    for x in range(len(tc)):
        g.add_vrect(
            x0=tc[x][0],
            x1=tc[x][1],
            fillcolor='black',
            opacity=0.15,
            line_width=0
        )


# %%
for i in range(len(tc)):
    g.add_vrect(tc[i][0], tc[i][1], visible=False)

pyo.plot(g)

# %%

df = pd.read_sql('SELECT * FROM gfb')

fig = go.Figure(
    data=[go.contourcarpet()]
)


