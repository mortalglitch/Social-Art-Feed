import ftplib

def push_data():
    session = ftplib.FTP('ftp.yoursite.com','user@yoursite.com','password')
    file = open('site/example.htm','rb')            # file to send
    session.storbinary('STOR example.htm', file)    # send the file
    file.close()                                    # close file and FTP
    session.quit()
    print('FTP Push Done')

if __name__ == '__main__':
    push_data()
