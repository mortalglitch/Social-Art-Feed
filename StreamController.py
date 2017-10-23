import tweepy, sys, time, shutil
# Switching to NoEncodeBuilder until the encoding errors can be resolved
import NoEncodeBuilder
import FtpPush
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler

# Basic listener the prints tweets to stdout
class StdOutListener(StreamListener):

    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        filter_file = open("filter.txt", "r")
        filter_lines = [x.strip('\n') for x in filter_file.readlines()]
        if any(x in data for x in filter_lines):
            print ("Data failed Check moving to next")
        else:
            print data
            #Editing to dump to text
            if 'media_url' in data:
                text_file = open("Output.txt", "a")
                text_file.write(data)
                text_file.close()
                self.num_tweets = self.num_tweets + 1
        if self.num_tweets < 8:
            return True
        else:
            text_file.close()
            filter_file.close()
            NoEncodeBuilder.build_func()
            #Disabling FTPPush by default.
            #FtpPush.push_data()

            #Commenting out pause to prevent timer

            #print('Starting Timer')
            #time.sleep(300)
            #print('Sleep Complete')
            main()
            return False

    def on_error(self, status):
        print status

def main():
    config_file = open("Config.txt", "r")
    CONSUMER_KEY = config_file.readline()
    CONSUMER_KEY = CONSUMER_KEY.replace("CONSUMER_KEY:", "")
    CONSUMER_KEY = CONSUMER_KEY.rstrip()
    CONSUMER_SECRET = config_file.readline()
    CONSUMER_SECRET = CONSUMER_SECRET.replace("CONSUMER_SECRET:","")
    CONSUMER_SECRET = CONSUMER_SECRET.rstrip()
    ACCESS_KEY = config_file.readline()
    ACCESS_KEY = ACCESS_KEY.replace("ACCESS_KEY:", "")
    ACCESS_KEY = ACCESS_KEY.rstrip()
    ACCESS_SECRET = config_file.readline()
    ACCESS_SECRET = ACCESS_SECRET.replace("ACCESS_SECRET:", "")
    ACCESS_SECRET = ACCESS_SECRET.rstrip()

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    # Generating generic time based string for naming backup
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # Backing up current file
    text_file = open("Output.txt", "a")
    text_file.close()
    shutil.copy2('Output.txt', 'backup/' + timestr + '.txt')
    # Clearing output file.
    text_file = open("Output.txt", "w")
    text_file.close()

    # Handles Twitter Auth and the timeout between post
    l = StdOutListener()
    stream = Stream(auth, l, timeout=10)

    # Filter Data here
    stream.filter(track=['#happy', '#life', '#love'])

if __name__ == '__main__':
    main()
