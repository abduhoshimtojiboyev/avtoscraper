# avtoscraper
Intro: this scrapy web scraper is created to scrape data from `avtoelon.uz`

in order to use this code follow the instructions
## Step 1 - Install & activate your python virtual environment
## Step 2 - Install the required python modules
To install the required modules for this python project to run you need to install the required python modules using the following command:

`pip install -r requirements.txt`


## Step 3 - Add your ScrapeOps API key to the settings.py file
You can signup for an ScrapeOps API key at https://scrapeops.io

Then add your API key to the settings.py file.
`SCRAPEOPS_API_KEY = 'YOUR_API_KEY_HERE'` 

## Step 4 - Run the project
Once the required python modules are installed you should be able to view/run the Python Scrapy Spider with the following command (from within the project folder):

Cd into the project spiders: `cd car/car/spiders`

View the project spiders: `scrapy list`

Run the project spider: `scrapy crawl avtospider`
 
