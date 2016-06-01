# Get this figure: fig = py.get_figure("https://plot.ly/~jacquelinelars/2/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~jacquelinelars/2/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="ACTIV-ES Argentine Films by Year, Genre, and Word Count", fileopt="extend"))
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~jacquelinelars/2/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
data = Data([
    Scatter(
        x=['n', 'Mystery', 'Drama', 'Documentary', 'Horror', 'Adventure', 'Drama', 'Comedy', 'Comedy', 'Drama', 'Short', 'Drama', 'Drama', 'Drama', 'Drama', 'Drama', 'Comedy', 'Drama', 'Drama', 'Comedy', 'Drama', 'Comedy', 'Adventure', 'Comedy', 'Sci-Fi', 'Action', 'Drama', 'Action', 'Crime', 'Comedy', 'n', 'Documentary', 'Animation', 'Adventure', 'Comedy', 'Drama', 'Drama', 'Drama', 'Documentary', 'Comedy', 'Comedy', 'Documentary', 'Comedy', 'Drama', 'Drama', 'Comedy', 'Comedy', 'Drama', 'Documentary', 'Drama', 'Drama', 'Documentary', 'Crime', 'Drama', 'Drama', 'Adventure', 'Documentary', 'Drama', 'Drama', 'Drama', 'Drama', 'Comedy', 'Comedy', 'Crime', 'Comedy', 'Comedy', 'Drama', 'Drama', 'Drama', 'Documentary', 'Documentary', 'Crime', 'Drama', 'Drama', 'Animation', 'Documentary', 'Action', 'Crime', 'Comedy', 'Comedy', 'Drama', 'Drama', 'Drama', 'Comedy', 'Drama', 'Comedy', 'Comedy', 'Comedy', 'Drama', 'Action', 'Action', 'Drama', 'Drama', 'Drama', 'Comedy', 'Comedy', 'Drama', 'Drama', 'Drama', 'Drama', 'Drama', 'Animation', 'Comedy', 'Drama', 'Drama', 'Drama', 'Comedy', 'n', 'Drama', 'Drama', 'Documentary', 'Drama', 'Comedy', 'Crime', 'Adventure', 'Drama', 'Comedy', 'Drama', 'Drama', 'Drama', 'Comedy', 'Comedy', 'Drama', 'Drama', 'Drama', 'Drama', 'Comedy', 'Documentary'],
        y=[1950, 1952, 1955, 1965, 1969, 1973, 1975, 1977, 1979, 1980, 1981, 1983, 1984, 1984, 1984, 1984, 1985, 1985, 1986, 1992, 1993, 1994, 1995, 1996, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2002, 2002, 2002, 2002, 2003, 2003, 2003, 2003, 2004, 2004, 2004, 2004, 2004, 2004, 2004, 2004, 2004, 2004, 2004, 2005, 2005, 2005, 2005, 2005, 2005, 2005, 2005, 2005, 2005, 2005, 2006, 2006, 2006, 2006, 2006, 2006, 2006, 2006, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2007, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2008, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2009, 2010, 2010, 2010, 2010, 2010, 2011, 2011, 2011, 2011, 2011, 2011, 2012, 2012, 2012, 2012],
        error_x=ErrorX(
            color='black',
            thickness='1',
            width='2'
        ),
        error_y=ErrorY(
            color='black',
            thickness='1',
            width='2'
        ),
        fill='none',
        line=Line(
            color='black',
            dash='solid',
            width=1
        ),
        marker=Marker(
            color='rgba(0, 0, 0, 0)',
            line=Line(
                color='black',
                width=0.8
            ),
            size=[10659, 4631, 16652, 1316, 2935, 5597, 3994, 7915, 8690, 11119, 1673, 8772, 6902, 6663, 11252, 10004, 16316, 11022, 8355, 10362, 5848, 12427, 11558, 10628, 5277, 8606, 415, 8849, 12562, 17537, 4745, 10774, 582, 6651, 12772, 12247, 7390, 7644, 6115, 12317, 10074, 14436, 15374, 4021, 5025, 10261, 12273, 15120, 12282, 9396, 5948, 10415, 3715, 14615, 6213, 130, 13947, 4437, 9321, 8646, 6777, 7733, 9439, 6905, 12624, 10654, 3491, 8651, 6813, 13121, 7468, 7109, 6312, 7127, 4336, 84, 11932, 5864, 12283, 12081, 10198, 9537, 4862, 5991, 3920, 8853, 9322, 9839, 3666, 8978, 8978, 2922, 10217, 7229, 8273, 8965, 4695, 5836, 6316, 10706, 10118, 7227, 13137, 4917, 14700, 7434, 5925, 7061, 4917, 11984, 8169, 10415, 8311, 11894, 12179, 3934, 16164, 5124, 7420, 5088, 8298, 13345, 7152, 5973, 3096, 9983, 15377, 21545],
            sizemode='area',
            sizeref=5.9847222222222225,
            sizesrc='jacquelinelars:0:0VHBKFTYG0NAZBSYY3GW6IKZTSKQKM4S',
            symbol='square'
        ),
        mode='markers',
        name='Year',
        opacity=0.7,
        uid='810f25',
        xsrc='jacquelinelars:0:3YY3D1KHNNQQIONGBX6KWQYPBBJYQZYH',
        ysrc='jacquelinelars:0:8M4LMKD23QKSE9JCYRSPWIL1CMQ7D4Q5'
    )
])
layout = Layout(
    autosize=True,
    bargap=0.2,
    font=Font(
        family='"Courier New", monospace',
        size=10
    ),
    height=620,
    hovermode='closest',
    legend=Legend(
        bgcolor='white',
        bordercolor='black',
        borderwidth=0
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    title='ACTIV-ES Argentine Films by Year, Genre, and Word Count',
    titlefont=dict(
        color='black',
        family='"Courier New", monospace',
        size=11
    ),
    width=1332,
    xaxis=XAxis(
        autorange=True,
        gridcolor='rgba(31, 119, 180, 0.25)',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=5,
        range=[-1.01774582102477, 11.95254654464614],
        showgrid=True,
        showline=True,
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='black',
            family='"Courier New", monospace',
            size=8
        ),
        ticklen=6,
        title='Genre',
        titlefont=dict(
            color='black',
            family='"Courier New", monospace',
            size=10
        ),
        type='category',
        zeroline=True,
        zerolinewidth=1
    ),
    yaxis=YAxis(
        autorange=True,
        gridcolor='rgba(31, 119, 180, 0.25)',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=5,
        range=[1939.1099697475706, 2025.6576497371],
        showgrid=True,
        showline=True,
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='black',
            family='"Courier New", monospace',
            size=8
        ),
        ticklen=6,
        title='Year',
        titlefont=dict(
            color='black',
            family='"Courier New", monospace',
            size=10
        ),
        type='linear',
        zeroline=True,
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)