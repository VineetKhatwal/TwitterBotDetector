import BotoMeter
import credentials

# **********************************************************************************
# *                                                                                *
# *                                     RAPID API KEY                              *
# *                                                                                *
# **********************************************************************************
rapidapi_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


twitter_app_auth = {
    'consumer_key': credentials.CONSUMER_API_KEY,
    'consumer_secret': credentials.CONSUMER_API_SECRET,
    'access_token': credentials.ACCESS_TOKEN,
    'access_token_secret': credentials.ACCESS_TOKEN_SECRET,
}
bom = BotoMeter.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
#result = bom.check_account('@CMPE_295_FakeNews')

# Check a single account by id
#result = bom.check_account(1548959833)

# Check a sequence of accounts
accounts = ['@realdonaldtrump']
for screen_name, result in bom.check_accounts_in(accounts):
    # Do stuff with `screen_name` and `result`
    print(screen_name, result)
