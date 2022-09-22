import searchconsole
import gspread

# Your domain inside of GSC
domain = "sc-domain:yourdomain.com"
# The name of your Google Sheets file
sheet = "MySheet"
# The name of the worksheet you want to import data into (or as default)
worksheet = "Sheet1"

# Get GSC data
account = searchconsole.authenticate(client_config='config.json', credentials='credentials.json')
webproperty = account[domain]

# Adjust the query range to suit your needs
report = webproperty.query.range('today', days=-30).dimension('query').get().to_dataframe()

# Import into Google Sheets
gc = gspread.service_account()

report = report.values.tolist()

# Preserve the headers on the first row, add data below
wks = gc.open(sheet).worksheet(worksheet)
wks.update("A2", report)