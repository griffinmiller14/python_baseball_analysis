"""
Griffin Miller
CSE 163 AI
This program implements the tests for each mathematic function in
my final project.
"""
import Griffin_Miller_Real
import Griffin_Miller_Fantasy
import pandas as pd

from cse163_utils import assert_equals


def test_era_to_ip_and_l(df):
    """
    This method tests the era_to_ip_and_l function.
    """
    # made a df that era has positve 1 corr with IP and negative 1 corr with L
    assert_equals((1.0, -1.0), Griffin_Miller_Real.era_to_ip_and_l(df))


def test_team_war_to_wins(df, df2):
    """
    This method tests the team_war_to_wins function.
    """
    # made to test csv files, one with win data and one with WAR data.
    # They get merged together and i made win/war have corr of 1
    assert_equals((1.0), Griffin_Miller_Real.team_war_to_wins(df, df2))


def test_average_points(df1, df2):
    """
    This method tests the average_points function.
    """
    # made a test data set of hitters with avg points equal to 200
    assert_equals(200, Griffin_Miller_Fantasy.average_points(df1))
    # made a test data set of pitchers with avg points equal to 75
    assert_equals(75, Griffin_Miller_Fantasy.average_points(df2))


def main():
    test2 = pd.read_csv('test2.csv')
    test3_0 = pd.read_csv('TEAM_WAR_data.csv')
    test3_1 = pd.read_csv('TEAM_data.csv')
    test4 = pd.read_csv('hitter_points.csv')
    test5 = pd.read_csv('pitcher_points.csv')

    test_era_to_ip_and_l(test2)
    test_team_war_to_wins(test3_0, test3_1)
    test_average_points(test4, test5)


if __name__ == '__main__':
    main()
