import matplotlib.pyplot as plt
import pandas as pd
PATH = '../figures/'
def presidents_sent_plot():
    plt.clf()
    plt.plot(df['date'], df['zelensky_pos'], label='Zelensky pos', color='darkorange')
    plt.plot(df['date'], df['zelensky_neg'], label='Zelensky neg', color='olive')
    plt.plot(df['date'], [0]*len(df['date']), '--',color='black', linewidth=0.5)
    plt.plot(df['date'], df['putin_pos'], label='Putin pos', color='green')
    plt.plot(df['date'], df['putin_neg'], label='Putin neg', color='steelblue')

    ticks = list(df['date'].values)
    step = int(len(ticks) / 20)

    plt.xticks([ticks[i] for i in range(0,len(ticks),step)],[ticks[i] for i in range(0,len(ticks),step)])
    plt.xticks(rotation=45)
    plt.ylabel('Sentiment')
    plt.xlim([df['date'].values[0], df['date'].values[-1]])
    plt.tight_layout()

    plt.legend(ncols=2)
    plt.savefig(PATH + 'president_sentiment.png', dpi=800)

def countries_sent_plot():
    plt.clf()
    plt.plot(df['date'], df['ukrain_pos'], label='Ukraine pos', color='darkorange')
    plt.plot(df['date'], df['ukrain_neg'], label='Ukraine neg', color='olive')
    plt.plot(df['date'], [0]*len(df['date']), '--',color='black', linewidth=0.5)
    plt.plot(df['date'], df['russia_pos'], label='Russia pos', color='green')
    plt.plot(df['date'], df['russia_neg'], label='Russia neg', color='steelblue')

    ticks = list(df['date'].values)
    step = int(len(ticks) / 20)
    print(df['date'])
    #[ticks[i] for i in range(0,len(ticks),step)]

    plt.xticks([ticks[i] for i in range(0,len(ticks),step)],[ticks[i] for i in range(0,len(ticks),step)])
    plt.xticks(rotation=45)
    plt.ylabel('Sentiment')
    plt.xlim([df['date'].values[0], df['date'].values[-1]])
    plt.tight_layout()

    plt.legend(ncols=2)
    plt.savefig(PATH + 'country_sentiment.png', dpi=800)

def activity_plot():
    plt.clf()
    
    plt.plot(df['day'], df['daily_users'], label='Active users')#, color='darkorange')
    plt.plot(df['day'], df['daily_tweets'], label='Users activity')#, color='olive')
    

    ticks = list(df['day'].values)
    step = int(len(ticks) / 20)
    print(df['day'])
    

    plt.xticks([ticks[i] for i in range(0,len(ticks),step)],[ticks[i] for i in range(0,len(ticks),step)])
    plt.xticks(rotation=45)
    plt.yscale("log")
    plt.xlim([df['day'].values[0], df['day'].values[-1]])
    plt.tight_layout()

    plt.legend(ncols=2, loc='upper center', framealpha=0.5)
    plt.savefig(PATH + 'activity_log.png', dpi=800)

def top_hashtags_plot():
    plt.clf()    
    for item in list(df.columns)[1:]:
        plt.plot(df['date'], df[item], label=item)
    

    ticks = list(df['date'].values)
    step = int(len(ticks) / 20)
    print(df['date'])


    plt.xticks([ticks[i] for i in range(0,len(ticks),step)],[ticks[i] for i in range(0,len(ticks),step)])
    plt.xticks(rotation=45)
    plt.yscale("log")
    plt.xlim([df['date'].values[0], df['date'].values[-1]])
    plt.tight_layout()
    
    plt.legend(loc='best', ncols=2, framealpha=0.5)
    plt.savefig(PATH + 'hashtags_log.png', dpi=800)

df = pd.read_csv('daily_sentiment.csv', header=0)
presidents_sent_plot()
countries_sent_plot()

df = pd.read_csv('daily_stats.csv', header=0)
activity_plot()

df = pd.read_csv('daily_hashtags.csv', header=0)
top_hashtags_plot()
