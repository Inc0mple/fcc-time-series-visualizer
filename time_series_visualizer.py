import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=[0],index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=[18,6])
    plt.plot(df["value"])
    #plt.plot_date(x=df["date"],y=df["value"],xdate=True,linestyle="solid")
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=[0])
    df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]
    #The code above this line is to make up for the fact that I did not initially add the index_col parameters to df that was needed to pass the tests
    df_bar = df.reset_index().groupby([df["date"].dt.strftime('%Y'),df["date"].dt.strftime('%B')],sort = False)['value'].mean()
    df_bar = df_bar.rename_axis(["Years","Months"]).unstack()
    df_bar_col = df_bar.columns.tolist()
    new_col = df_bar_col[8:]+df_bar_col[0:8]
    df_bar = df_bar[new_col]
    # Draw bar plot
    fig = df_bar.plot.bar(figsize=(8,6)).set_ylabel("Average Page Views").get_figure()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()
def draw_box_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=[0])
    df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]
    #The code above this line is to make up for the fact that I did not initially add the index_col parameters to df that was needed to pass the tests
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,6)) 
    sns.boxplot(data=df_box,y="value",x="year",ax = ax1).set(xlabel="Year",ylabel="Page Views",title="Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box,y="value",x="month",ax = ax2,order=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]).set(xlabel="Month",ylabel="Page Views",title="Month-wise Box Plot (Seasonality)")
    #plt.show()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
