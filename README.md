# Google Search Console -> Google Sheets

This script will import data from your GSC account to a Google Sheet (and worksheet) of your choosing.

## Installation

- Git clone the repository

- Create a new project in [Google Developers Console](https://console.cloud.google.com/apis/dashboard), then enable the APIs for Google Search Console and Google Sheets

- Finally, create your credentials and select OAuth Client ID. Save the json file to the root of your project directory.

## How to Use

- Modify the first three variables in main.py to reflect your info. You'll need your GSC domain, your desired Google Sheet endpoint, and an optional worksheet inside that Google Sheet.

- Modify the "report" variable to set date ranges and filters

- python main.py and profit!