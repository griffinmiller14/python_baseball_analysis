Veiw the written report in the attached PDF file.


To run this project, begin with the following steps:
1) Install the necessary libraries
    - BeautifulSoup4
        ~ In your terminal, type 'pip install beautifulsoup4'
    - requests
        ~ In your terminal, type 'pip install requests'
    - selenium
        ~ In your terminal, type 'pip install selenium'

2) You will need to have Google Chrome browser on your computer. If you don't
    have Chrome, install it by going to: https://www.google.com/chrome/

3) You will need to install the Chrome WebDriver
    - Open Google Chrome
        ~ click the 3 dots in the upper right corner
            > hover over 'Help' and then click on 'About Google Chrome'
                - You should be able to see your version of chrome (i.e., 88.0.4324)
                    ~ Go to https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnVIOGdobXNia2p4N0FtWE5HUmU4cXVoQkdYQXxBQ3Jtc0tuODJuQlhRdUxVWFMtNVZwNS12U3dQbFBiQ0s5b3dTM3FPZzlTTkJlNUx1Z0J2LXhkd0w4VG4xUThVVDlCbWJaNDJDT0lNQmxvTzdLWHpCS0R0ZVYwN0pod0h3QVFCN09wdHIxdjIwdm1wWWRrLTRkMA&q=https%3A%2F%2Fsites.google.com%2Fa%2Fchromium.org%2Fchromedriver%2Fdownloads
                        > select your version of Chrome
                            - Download the appropriate WebDriver dependent upon your operating system
                                ~ *Change the PATH variable in hitters_scrape.py and pitchers_scrape.py to the absolute path of your newly installed chromedriver*
                                    > This YouTube Video is what I used for reference: https://www.youtube.com/watch?v=Xjv1sY630Uc&t=296s

4) Open all of the python modules in your IDE
    - hitters_scrape.py
    - pitchers_scrape.py
    - teams_scrape.py
    - Griffin_Miller_Real.py
    - Griffin_Miller_Fantasy.py
    - Griffin_Miller_test.py
    - cse163_utils.py

5) Run the following modules in order:
    1) hitters_scrape.py
    2) pitchers_scrape.py
    3) teams_scrape.py

  These modules will save 3 seperate files to your working directory. These files will be used in the other modules. *See Notes at bottom of this file if you are unable to scrape the data with selenium*

6) Run the Griffin_Miller_Real.py module. This will save several plots to your working directory (I have included them in my submission)

7) Run the Griffin_Miller_Fantasy.py module. This will save several plots to your working directory (I have included them in my submission)

8) Griffin_Miller_test.py can be run to test the mathematical functions of this project.
    - The following CSV files in the will need to be placed in your working directory in order to run the test
        > test2.csv
        > TEAM_WAR_data.csv
        > TEAM_data.csv
        > hitter_points.csv
        > pitcher_points.csv

Notes:

- *If you have trouble scraping the data with selenium, I have included the scraped data in the submission (hitter_data.csv, pitchers_data.csv, and teams_data.csv*

- *Your results may differ slighty from mine as the projected stats I am scraping from FanGraphs are adjusted ever so slightly each week leading up until the start of the season*

- *Plots are included in the submission*
