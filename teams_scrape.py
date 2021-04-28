"""
Griffin Miller
CSE 163 AI
This program scrapes the fangraphs website to obtain information related
to each MLB team.
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    # initialize lists for all columns of data set
    team, games, wins, losses, w_l_ratio, run_dif, \
        rs_game, ra_game = ([] for i in range(8))

    # start scraping
    page = requests.get('https://www.fangraphs.com/depthcharts' +
                        '.aspx?position=Standings')

    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("div", {"class": 'depth-charts-aspx_table'})

    teams = table.find_all('tr', class_=['depth_team'])

    for t in teams[0:30]:
        text = t.get_text(',')
        data_line = text.split(',')

        team.append(data_line[0])
        games.append(data_line[8])
        wins.append(data_line[9])
        losses.append(data_line[10])
        w_l_ratio.append(data_line[11])
        run_dif.append(data_line[12])
        rs_game.append(data_line[13])
        ra_game.append(data_line[14])

    baseball_data = pd.DataFrame(
        {
            'Team': team,
            'Games': games,
            'Wins': wins,
            'Losses': losses,
            'W%': w_l_ratio,
            'RDif': run_dif,
            'RS/G': rs_game,
            'RA/G': ra_game
        }
    )
    baseball_data.to_csv('teams_data.csv', index=False)

    print(baseball_data)


if __name__ == '__main__':
    main()
