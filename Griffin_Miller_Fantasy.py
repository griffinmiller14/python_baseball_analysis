"""
Griffin Miller
CSE 163 AI
This program implements functions necessary to conduct analysis on baseball
projection data and how it relates to fantasy baseball.
"""
from Griffin_Miller_Real import load_data
from Griffin_Miller_Real import merge_player_and_team
from Griffin_Miller_Real import stat_corr_pitchers_visual
from Griffin_Miller_Real import stat_corr_hitters_visual
from Griffin_Miller_Real import stat_corr_math
from Griffin_Miller_Real import plot_stat_players_by_team


def create_total_points_hitter(df):
    """
    Takes in the hitter data frame and applies the scoring system
    from my fantasy league to calculate a total points column.
    Returns the df with the new column.
    """
    df['tot_points'] = (df['R'] * 3) + \
                       ((df['H'] - df['2B'] - df['3B'] - df['HR']) * 4) +\
                       (df['2B'] * 8) + (df['3B'] * 12) +\
                       (df['HR'] * 16) + (df['RBI'] * 3) +\
                       (df['SB'] * 4) - (df['CS'] * 3) + (df['BB'] * 4) +\
                       (df['HBP'] * 4)

    return df


def create_total_points_pitcher(df):
    """
    Takes in the pitcher data frame and applies the scoring system
    from my fantasy league to calculate a total points column.
    Returns the df with the new column.
    """
    df['tot_points'] = (df['IP'] * 3) + (df['W'] * 3) - (df['ER'] * 3) +\
                       (df['SO'] * 3)

    return df


def average_points(df):
    """
    takes in a postion dataframe (hitters or pitchers) and returns the
    average total points scored.
    """
    return df['tot_points'].mean()


def main():
    # Loading in the data sets and merging them appropriately
    hitter_df, pitcher_df, team_df = load_data()
    master_hitter_df = merge_player_and_team(team_df, hitter_df)
    master_pitchers_df = merge_player_and_team(team_df, pitcher_df)

    # Create points columns
    master_h_points = create_total_points_hitter(master_hitter_df)
    master_p_points = create_total_points_pitcher(master_pitchers_df)

    # Avg points for hitters and pitchers
    avg_hitters = average_points(master_h_points)
    avg_pitchers = average_points(master_p_points)
    print(f'Average points for hitters: {avg_hitters:.2f}')
    print(f'Average points for pitchers: {avg_pitchers:.2f}')

    # Plot correlation of points with various stats
    stat_corr_pitchers_visual(master_p_points, 'tot_points', ['7', '8', '9'],
                              'pitcher_tot_points.png')
    most_corr_points_p, least_corr_points_p = stat_corr_math(master_p_points,
                                                             50, 'tot_points')
    print('Pitcher stats most correlated with fantasy points:')
    print(most_corr_points_p)
    print('Pitcher stats least correlated with fantasy points:')
    print(least_corr_points_p)

    stat_corr_hitters_visual(master_h_points, 'tot_points', ['10', '11', '12'],
                             'hitter_tot_points.png')
    most_corr_points_h, least_corr_points_h = stat_corr_math(master_h_points,
                                                             200, 'tot_points')
    print('Hitter stats most correlated with fantasy points:')
    print(most_corr_points_h)
    print('Hitter stats least correlated with fantasy points:')
    print(least_corr_points_h)

    # plot number of players on each team
    plot_stat_players_by_team(master_h_points, 100, 'team_points_hitters',
                              'tot_points')

    plot_stat_players_by_team(master_p_points, 30, 'team_points_pitchers',
                              'tot_points')


if __name__ == '__main__':
    main()
