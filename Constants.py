from datetime import date

# Getting holidays from https://www.nyse.com/markets/hours-calendars

TRADING_HOLIDAYS = [
    date(2021, 12, 24),
    date(2022, 12, 31),
    date(2022, 1, 17),
    date(2022, 2, 21),
    date(2022, 4, 15),
    date(2022, 5, 30),
    date(2022, 7, 4),
    date(2022, 9, 5),
    date(2022, 11, 24),
    date(2022, 12, 25)
]

FILTER_DEFAULTS = {
    'VOLUME_MIN': 400000,
    'MIN_STOCK_VALUE': 1,
    'MARKET_CAP_MIN': 1000000000,
    'PE_MIN': 0,
    'PE_MAX': 50
}

MIN_DATA_LEN = 104

TICKERS_FOLDER = 'tickers'

API_URL = 'http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange={}&render=download'

EXCHANGES = ('nasdaq', 'nyse', 'amex')

COMMASPACE = ', '

DAILY_REPORTS_FOLDER = 'daily_reports'

DAILY_REPORTS_ENDING = '_report.txt'

CLIENT_SECRET_FILE = 'json/client_secret.json'

APPLICATION_NAME = 'ichimokuemaillist'

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

FILES = ["amex.txt", "nasdaq.txt", "nyse.txt"]

SPECIFIC_PATH = 'tickers/all_tickers.txt'

IGNORED_STRINGS = ('SYMBOL', )

FTP_ADDRESS = 'ftp.nasdaqtrader.com'

FTP_CWD = 'SymbolDirectory'

NASDAQ_FILE = 'nasdaqlisted.txt'

OTHER_FILE = 'otherlisted.txt'

FTP_DELIMITER = '|'

FILTERED_SYMBOLS = ('^', '.', '$')
