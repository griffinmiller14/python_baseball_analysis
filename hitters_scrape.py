"""
Griffin Miller
CSE 163 AI
This program scrapes the fangraphs website to obtain information on the top
500 hitters going into this coming MLB Season.
"""
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def main():
    # initialize lists for all columns of data set
    names, teams, games, plate_aps, at_bats, hits, doubles, triples,\
        home_runs, runs, rbis, walks, strikeouts, hit_by_pitches,\
        stolen_bases, caughts, avg, obp, slg, ops, woba, fld, bsr,\
        war, adp = ([] for i in range(25))

    URL = ('https://www.fangraphs.com/' +
           'projections.aspx?pos=all&stats=bat&type=zips')
    PATH = '/Users/Griffin/chromedriver'

    # navigate to Fangraphs page
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    driver.fullscreen_window()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ProjectionBoard1_dg1_ctl00_ctl0' +
                                 '2_ctl00_PageSizeComboBox"]/span/' +
                                 'button').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ProjectionBoard1_dg1_ctl00_ctl02' +
                                 '_ctl00_PageSizeComboBox_DropDown"]/div/ul' +
                                 '/li[6]').click()
    time.sleep(5)

    # start scraping
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find(id='ProjectionBoard1_dg1')

    players = table.find_all('tr', class_=['rgRow', 'rgAltRow'])

    for p in players:
        data_line = p.find_all('td', class_='grid_line_regular')

        names.append(data_line[0].get_text())
        teams.append(data_line[2].get_text())
        games.append(data_line[3].get_text())
        plate_aps.append(data_line[4].get_text())
        at_bats.append(data_line[5].get_text())
        hits.append(data_line[6].get_text())
        doubles.append(data_line[7].get_text())
        triples.append(data_line[8].get_text())
        home_runs.append(data_line[9].get_text())
        runs.append(data_line[10].get_text())
        rbis.append(data_line[11].get_text())
        walks.append(data_line[12].get_text())
        strikeouts.append(data_line[13].get_text())
        hit_by_pitches.append(data_line[14].get_text())
        stolen_bases.append(data_line[15].get_text())
        caughts.append(data_line[16].get_text())
        avg.append(data_line[17].get_text())
        obp.append(data_line[18].get_text())
        slg.append(data_line[19].get_text())
        ops.append(data_line[20].get_text())
        woba.append(data_line[21].get_text())
        fld.append(data_line[22].get_text())
        bsr.append(data_line[23].get_text())
        war.append(data_line[24].get_text())
        adp.append(data_line[25].get_text())

    driver.quit()

    baseball_data = pd.DataFrame(
        {
            'Name': names,
            'Team_Abr': teams,
            'G': games,
            'PA': plate_aps,
            'AB': at_bats,
            'H': hits,
            '2B': doubles,
            '3B': triples,
            'HR': home_runs,
            'R': runs,
            'RBI': rbis,
            'BB': walks,
            'SO': strikeouts,
            'HBP': hit_by_pitches,
            'SB': stolen_bases,
            'CS': caughts,
            'AVG': avg,
            'OBP': obp,
            'SLG': slg,
            'OPS': ops,
            'wOBA': woba,
            'Fld': fld,
            'BsR': bsr,
            'WAR': war,
            'ADP': adp
        }
    )
    baseball_data.to_csv('hitter_data.csv', index=False)

    print(baseball_data.head())


if __name__ == '__main__':
    main()
