"""
Griffin Miller
CSE 163 AI
This program implements functions necessary to conduct analysis on baseball
projection data and how it can be used to identify the best players and
most important stats.
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_data():
    '''
    This method is repsonsible for loading in the data frames needed
    for the following analysis. Returns each of data frames.
    '''
    hitter = pd.read_csv('hitter_data.csv')
    hitter = hitter.replace(' ', np.nan)
    pitcher = pd.read_csv('pitchers_data.csv')
    pitcher = pitcher.replace(' ', np.nan)
    team = create_team_key()

    return hitter, pitcher, team


def create_team_key():
    '''
    Loads in the team related data. Creates a data frame that maps team
    abbreviation to team name. By merging these two data frames together,
    it allows for the addition of the team name column to the original
    team data set that only contained the abbreviation. Returns the new
    data frame.
    '''
    teams_df = pd.read_csv('teams_data.csv')
    data = [
        ['LAA', 'Angels'],
        ['LAD', 'Dodgers'],
        ['NYY', 'Yankees'],
        ['SDP', 'Padres'],
        ['NYM', 'Mets'],
        ['ATL', 'Braves'],
        ['HOU', 'Astros'],
        ['TOR', 'Blue Jays'],
        ['CHW', 'White Sox'],
        ['MIN', 'Twins'],
        ['BOS', 'Red Sox'],
        ['TBR', 'Rays'],
        ['OAK', 'Athletics'],
        ['WSN',  'Nationals'],
        ['PHI', 'Phillies'],
        ['CLE', 'Cleveland'],
        ['STL', 'Cardinals'],
        ['MIL', 'Brewers'],
        ['CHC', 'Cubs'],
        ['KCR', 'Royals'],
        ['CIN', 'Reds'],
        ['SFG', 'Giants'],
        ['SEA', 'Mariners'],
        ['ARI', 'Diamondbacks'],
        ['MIA', 'Marlins'],
        ['DET', 'Tigers'],
        ['TEX', 'Rangers'],
        ['BAL', 'Orioles'],
        ['COL', 'Rockies'],
        ['PIT', 'Pirates'],
        ]

    key_df = pd.DataFrame(data, columns=['Abr', 'Name'])

    merged_df = teams_df.merge(key_df, left_on='Team', right_on='Name',
                               how='left')

    team_with_abr = merged_df.drop(columns=['Name'])

    return team_with_abr


def merge_player_and_team(team, player):
    """
    Takes in a team data frame and a player related data frame.
    This method merges the given player related data frame
    (hitters or pitchers) with the team data frame. This results
    in each player row also containing their respective teams stats.
    Returns the merged data frame.
    """
    merged = player.merge(team, left_on='Team_Abr', right_on='Abr',
                          how='left')

    return merged


def stat_corr_hitters_visual(hitter, stat, file_range, export):
    """
    Takes in the hitter df, a string representing the stat we wish to
    measure correlation with, a list of strings that assist in naming
    output files, and a string representing the exported plot file name.
    This method plots the given stat's correlation with a wide range
    of hitter related stats.
    """
    df = hitter.head(200)
    sns.pairplot(df, x_vars=['G', 'PA', 'AB', '2B', '3B', 'HR', 'H'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[0] + '.png', dpi=300)
    plt.clf()

    sns.pairplot(df, x_vars=['R', 'RBI', 'BB', 'SO', 'HBP', 'SB', 'CS'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[1] + '.png', dpi=300)
    plt.clf()

    sns.pairplot(df, x_vars=['AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'Fld', 'BsR'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[2] + '.png', dpi=300)
    plt.clf()

    fig, ax = plt.subplots(3, 1, figsize=(30, 30))

    ax[0].imshow(mpimg.imread('plot' + file_range[0] + '.png'))
    ax[1].imshow(mpimg.imread('plot' + file_range[1] + '.png'))
    ax[2].imshow(mpimg.imread('plot' + file_range[2] + '.png'))
    fig.suptitle(stat + ' Correlation Matrix', fontsize=120)
    fig.tight_layout()
    plt.savefig(export)
    plt.clf()


def stat_corr_pitchers_visual(pitcher, stat, file_range, export):
    """
    Takes in the pitcher df, a string representing the stat we wish to
    measure correlation with, a list of strings that assist in naming
    output files, and a string representing the exported plot file name.
    This method plots the given stat's correlation with a wide range
    of pitcher related stats.
    """
    df = pitcher.head(50)
    sns.pairplot(df, x_vars=['ERA', 'GS', 'IP', 'H'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[0] + '.png')
    plt.clf()

    sns.pairplot(df, x_vars=['ER', 'HR', 'SO', 'BB'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[1] + '.png')
    plt.clf()

    sns.pairplot(df, x_vars=['WHIP', 'K/9', 'BB/9', 'FIP'],
                 y_vars=[stat], diag_kind=None)
    plt.savefig('plot' + file_range[2] + '.png')
    plt.clf()

    fig, ax = plt.subplots(3, 1, figsize=(30, 30))

    ax[0].imshow(mpimg.imread('plot' + file_range[0] + '.png'))
    ax[1].imshow(mpimg.imread('plot' + file_range[1] + '.png'))
    ax[2].imshow(mpimg.imread('plot' + file_range[2] + '.png'))
    fig.tight_layout()
    fig.suptitle(stat + ' Correlation Matrix', fontsize=80)
    plt.savefig(export)
    plt.clf()


def stat_corr_math(data, num, stat):
    """
    Takes in a position df (hitters or pitchers), a number (num) of how many
    players to include in the analysis, and a string of the stat to be used in
    the analyis. Returns a df of the stats most correlated with the given
    stat and a df of the stats least correlated with the given stat.
    """
    df = data.head(num)
    corr_matrix = df.corr()

    return corr_matrix[stat].nlargest(10), corr_matrix[stat].nsmallest(10)


def era_to_ip_and_l(df):
    """
    Takes in pitcher df. Plots the relationship between ERA and IP,
    highlighting losses with the hue of the points. Plots the
    relationship between ERA and Losses. Also returns the
    correlation coeffecient of ERAxIP and ERAxLosses.
    """
    sns.relplot(data=df, x='ERA', y='IP', hue='L')
    plt.title('ERA & IP Correlation')
    plt.savefig('ERAxIP.png', bbox_inches='tight')
    plt.clf()

    sns.relplot(data=df, x='ERA', y='L')
    plt.title('ERA & Losses Correlation')
    plt.savefig('ERAxL.png', bbox_inches='tight')
    plt.clf()
    return df['ERA'].corr(df['IP']), df['ERA'].corr(df['L'])


def team_war_position(data, num, file_name):
    """
    This method takes in a player-team combined df, the count of how many
    players to be included in the analysis, and the name of the file to be
    saved to. It graphs the total WAR of each team in a bar chart.
    """
    data = data.head(num)
    df = data.groupby('Team')['WAR'].sum().reset_index()
    sns.catplot(data=df, x='Team', y='WAR', kind='bar', ci=None, color='g')
    plt.xticks(rotation=90)
    plt.title(file_name[13:] + ' WAR by Team')

    plt.savefig((file_name + '.png'), bbox_inches='tight')
    plt.clf()


def team_war_total(hitter, pitcher, team):
    """
    Takes in the hitter and pitcher data frames, as well as the team
    data frame. Returns a data frame containing each team, its hitter WAR,
    pitcher WAR, and total WAR based off the the top 300 hitters and 100
    pitchers. Also plots a bar chart showing total WAR for each team.
    """
    hitter_df = hitter.head(300)
    hitter_df = hitter_df.groupby('Team')['WAR'].sum().reset_index()

    pitcher_df = pitcher.groupby('Team')['WAR'].sum().reset_index()

    merged_df = hitter_df.merge(pitcher_df, left_on='Team', right_on='Team',
                                how='left')

    total_war_df = merged_df.copy()
    total_war_df['Total_WAR'] = merged_df['WAR_x'] + merged_df['WAR_y']

    sns.catplot(data=total_war_df, x='Team', y='Total_WAR', kind='bar',
                ci=None, color='g')
    plt.xticks(rotation=90)
    plt.title('Total Team WAR')

    plt.savefig('total_team_war.png', bbox_inches='tight')
    plt.clf()

    return total_war_df


def team_wins_plot(teams):
    """
    Takes in the team data frame and simply plots a bar chart displaying
    the total amount of wins by each team.
    """
    sns.catplot(data=teams, x='Team', y='Wins', kind='bar',
                ci=None, color='g')
    plt.xticks(rotation=90)
    plt.title('Wins by Team')

    plt.savefig('total_team_wins.png', bbox_inches='tight')
    plt.clf()


def team_war_to_wins(team_war, team):
    """
    Takes in the team data set containing total war as well as the
    team data set containing team record. Merges these data sets and
    plots the correlation between total team war and wins.
    Returns the correlation coeffecient.
    """
    merged_df = team.merge(team_war, left_on='Team', right_on='Team',
                           how='inner')

    sns.relplot(data=merged_df, x='Wins', y='Total_WAR')
    plt.title('Total Team WAR & Wins Correlation')
    plt.savefig('team_war_to_wins.png', bbox_inches='tight')
    plt.clf()

    return merged_df['Wins'].corr(merged_df['Total_WAR'])


def plot_stat_players_by_team(df, num, file_name, stat):
    """
    Takes in a postion data frame (hitters or pitchers), a number (num) of
    players to include in the analysis, an export file name, and the stat to
    use in analysis. Takes the top (num) of players from the given data set and
    plots a bar graph depciting how many players in the top (num) are on
    each team.
    """
    sorted_df = df.sort_values(by=[stat], ascending=False)
    final_df = sorted_df.head(num)

    sns.countplot(data=final_df, x='Team', color='g')
    plt.ylim(top=10)
    plt.xticks(rotation=90)
    plt.title('Count of Top Players by Team')

    plt.savefig(file_name + '.png', bbox_inches='tight')
    plt.clf()


def main():
    # Loading in the data sets and merging them appropriately
    hitter_df, pitcher_df, team_df = load_data()
    master_hitter_df = merge_player_and_team(team_df, hitter_df)
    master_pitchers_df = merge_player_and_team(team_df, pitcher_df)

    # Hitter stats correlated with WAR
    stat_corr_hitters_visual(hitter_df, 'WAR', ['1', '2', '3'],
                             'hitter_WAR.png')
    most_corr_war_h, least_corr_war_h = stat_corr_math(hitter_df, 200, 'WAR')
    print('Hitter stats most correlated with WAR:')
    print(most_corr_war_h)
    print('Hitter stats least correlated with WAR:')
    print(least_corr_war_h)
    # Pitcher stats correlated with WAR
    stat_corr_pitchers_visual(pitcher_df, 'WAR', ['4', '5', '6'],
                              'pitcher_WAR.png')
    most_corr_war_p, least_corr_war_p = stat_corr_math(pitcher_df, 50, 'WAR')
    print('Pitcher stats most correlated with WAR:')
    print(most_corr_war_p)
    print('Pitcher stats least correlated with WAR:')
    print(least_corr_war_p)

    # IP and Losses vs ERA
    era_ip_corr, era_l_corr = era_to_ip_and_l(pitcher_df)
    print(f'ERA and IP Corr: {era_ip_corr:3f}')
    print(f'ERA and Losses Corr: {era_l_corr}')

    # Team WAR plots
    # hitters
    team_war_position(master_hitter_df, 300, 'tot_team_war_hitters')
    # pitchers
    team_war_position(master_pitchers_df, 100, 'tot_team_war_pitchers')
    # combined
    team_w_war = team_war_total(master_hitter_df, master_pitchers_df, team_df)

    # Team Wins plot
    team_wins_plot(team_df)

    # Team performance correlated with WAR (visual and math)
    tot_war_to_wins = team_war_to_wins(team_w_war, team_df)
    print(f'Team WAR and Wins Corr: {tot_war_to_wins:.3f}')

    # Number of top WAR players on each team
    plot_stat_players_by_team(master_hitter_df, 100, 'team_war_hitter_count',
                              'WAR')
    plot_stat_players_by_team(master_pitchers_df, 30, 'team_war_pitcher_count',
                              'WAR')


if __name__ == '__main__':
    main()
