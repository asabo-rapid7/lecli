TEST_OWNER_APIKEY = 'test_owner_apikey'
TEST_OWNER_APIKEY_ID = 'test_owner_apikey_id'
TEST_ACCOUNT_RESOURCE_ID = 'test_account_resource_id'
TEST_MANAGEMENT_URL = 'https://rest.logentries.com/management'

TEST_USER_KEY = "test_user_key"
DUMMY_USER_CONTENT = {"user": {"first_name": "",
                               "last_name": "",
                               "login_name": "",
                               "email": "",
                               "id": ""}}

TEST_APIKEY_WITH_VALID_LENGTH = '123456789012345678901234567890123456'
TEST_APIKEY_WITH_INVALID_LENGTH = '123456789012345678901234567890123456_invalid'

TEST_QUERY = 'where(logID) calculate(count) sort(desc) limit(3)'

TEST_LOG_KEY = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
TEST_LOG_GROUP = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX\n' \
                 'YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY'

TEST_LOG_RESOURCE_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

TIME_FROM = '1465370400'
TIME_TO = '1465370500'

DATE_FROM = '2016-05-18 11:04:00'
DATE_TO = '2016-05-18 11:09:59'

RELATIVE_TIME = 'last 2 days'

MOCK_QUERYAPI_URL = 'http://mydummylink.com/query/'

MOCK_USERAPI_URL = 'http://mydummylink.com/user'

MOCK_TEAMSAPI_URL = 'http://mydummyurl.com/teams'

MOCK_USAGE_URL = 'https://mydummyurl.com/usage'

MOCK_SAVED_QUERY_URL = 'https://mydummyurl.com/saved_queries'

MOCK_LOGAPI_URL = 'https://mydummyurl.com/management/logs'

TEST_TEAM_ID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

USAGE_DATE_FROM = '2016-03-01'

USAGE_DATE_TO = '2016-10-01'
