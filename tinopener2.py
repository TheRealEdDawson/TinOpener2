import requests
import sys
import logging
import datetime


# Set connecting site details
siteURL = sys.argv[1]
siteUserName = sys.argv[2]
sitePassWord = sys.argv[3]
securePage = sys.argv[4]

# Checking that all the arguments were entered on the command line, exiting with a message if not.
if len(sys.argv) < 5:
    argumentsnotset = '\nError: one or more arguments were not passed. \n\nUsage is like so: \n\nPython tinopener.py SITE-URL USERNAME PASSWORD SECUREPAGE-URL'
    print argumentsnotset
    sys.exit(1)	

# Set up logging
loggydatestamp = datetime.date.today().strftime("%Y-%m-%d %H:%M")
logfilename = str(datetime.date.today()) + '-TinOpener' + '.log'
print 'Logging to ' + logfilename
logging.basicConfig(filename=logfilename,filemode='w',level=logging.INFO,format='%(asctime)s %(message)s')
initialloggystring = 'New connection started at ' + loggydatestamp
print initialloggystring
logging.info(initialloggystring)

def main():
    #Start a session so we can have persistent cookies
    session = requests.session(config={'verbose': sys.stderr})
    #This is the form data that the page sends when logging in
    login_data = {
        'session[username]': siteUserName,
        'session[password]': sitePassWord,
        'commit': 'Login',
        'utf8': True,
    }

# Authenticate
    r = session.post(siteURL, data=login_data)
    print r.status_code
    logging.info(r.status_code)
    logging.info(r.headers)
    print r.encoding
    logging.info(r.encoding)
    logging.info(r.text)
    logging.info(r.json)
    # Try accessing a page that requires you to be logged in
    logging.info("Now trying to access a page that requires the user to be logged in:")
    r = session.get(securePage) #2.0
    print r.status_code
    logging.info(r.status_code)
    logging.info(r.headers)
    print r.encoding
    logging.info(r.encoding)
    logging.info(r.text)
    logging.info(r.json)

if __name__ == '__main__':
    main()

endloggystring = "\n*** END PROCESS ***\n"
logging.info(endloggystring)
