"""
Griffin Miller
CSE 163 AI
This program scrapes the fangraphs website to obtain information on the top
100 pitchers going into this coming MLB Season.
"""
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def main():
    # initialize lists for all columns of data set
    names, teams, wins, losses, era, starts, ip, hits_given, earned_runs, \
        home_runs, strikeouts, walks, whip, k_by_9, bb_by_9, fip, war, \
        adp = ([] for i in range(18))

    URL = 'https://www.fangraphs.com/projections.aspx?pos=all&stats' + \
        '=pit&type=zips&team=0&lg=all&players=0'
    PATH = '/Users/Griffin/chromedriver'

    # navigate to Fangraphs page
    driver = webdriver.Chrome(PATH)
    driver.get(URL)
    driver.fullscreen_window()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ProjectionBoard1_dg1_ctl00_ctl02' +
                                 '_ctl00_PageSizeComboBox_Arrow"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ProjectionBoard1_dg1_ctl00_ctl02_' +
                                 'ctl00_PageSizeComboBox_DropDown"]' +
                                 '/div/ul/li[5]').click()
    time.sleep(5)

    # start scraping
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find(id='ProjectionBoard1_dg1')

    players = table.find_all('tr', class_=['rgRow', 'rgAltRow'])

    for p in players:
        data_line = p.find_all('td', class_='grid_line_regular')

        names.append(data_line[0].get_text())
        teams.append(data_line[2].get_text())
        wins.append(data_line[3].get_text())
        losses.append(data_line[4].get_text())
        era.append(data_line[5].get_text())
        starts.append(data_line[6].get_text())
        ip.append(data_line[8].get_text())
        hits_given.append(data_line[9].get_text())
        earned_runs.append(data_line[10].get_text())
        home_runs.append(data_line[11].get_text())
        strikeouts.append(data_line[12].get_text())
        walks.append(data_line[13].get_text())
        whip.append(data_line[14].get_text())
        k_by_9.append(data_line[15].get_text())
        bb_by_9.append(data_line[16].get_text())
        fip.append(data_line[17].get_text())
        war.append(data_line[18].get_text())
        adp.append(data_line[19].get_text())

    driver.quit()

    baseball_data = pd.DataFrame(
        {
            'Name': names,
            'Team_Abr': teams,
            'W': wins,
            'L': losses,
            'ERA': era,
            'GS': starts,
            'IP': ip,
            'H': hits_given,
            'ER': earned_runs,
            'HR': home_runs,
            'SO': strikeouts,
            'BB': walks,
            'WHIP': whip,
            'K/9': k_by_9,
            'BB/9': bb_by_9,
            'FIP': fip,
            'WAR': war,
            'ADP': adp,
        }
    )
    baseball_data.to_csv('pitchers_data.csv', index=False)

    print(baseball_data.head())


if __name__ == '__main__':
    main()
