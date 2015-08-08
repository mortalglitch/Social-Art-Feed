import json

def build_func():
    # Begining with reading every line for the generated output file into various
    # strings.
    source_file = open("Output.txt", "r")

    post1 = source_file.readline()
    post2 = source_file.readline()
    post3 = source_file.readline()
    post4 = source_file.readline()
    post5 = source_file.readline()
    post6 = source_file.readline()
    post7 = source_file.readline()
    post8 = source_file.readline()

    parsedPost1 = json.loads(post1)
    parsedPost2 = json.loads(post2)
    parsedPost3 = json.loads(post3)
    parsedPost4 = json.loads(post4)
    parsedPost5 = json.loads(post5)
    parsedPost6 = json.loads(post6)
    parsedPost7 = json.loads(post7)
    parsedPost8 = json.loads(post8)
    print ('Parsing Data Complete')

    source_file.close()

    # Conversion - there is probably a simpler way to do this but I'm doing it this way for now.
    post1_Text = parsedPost1['text'].encode('utf-8')
    post1_Name = parsedPost1['user']['screen_name'].encode('utf-8')
    post1_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post1_Name + '">'
    post1_ImageLink = parsedPost1['entities']['media'][0]['media_url'].encode('utf-8')
    post1_ImageComplete = '<img src="' + post1_ImageLink + '" >'

    post2_Text = parsedPost2['text'].encode('utf-8')
    post2_Name = parsedPost2['user']['screen_name'].encode('utf-8')
    post2_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post2_Name + '">'
    post2_ImageLink = parsedPost2['entities']['media'][0]['media_url'].encode('utf-8')
    post2_ImageComplete = '<img src="' + post2_ImageLink + '" >'

    post3_Text = parsedPost3['text'].encode('utf-8')
    post3_Name = parsedPost3['user']['screen_name'].encode('utf-8')
    post3_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post3_Name + '">'
    post3_ImageLink = parsedPost3['entities']['media'][0]['media_url'].encode('utf-8')
    post3_ImageComplete = '<img src="' + post3_ImageLink + '" >'

    post4_Text = parsedPost4['text'].encode('utf-8')
    post4_Name = parsedPost4['user']['screen_name'].encode('utf-8')
    post4_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post4_Name + '">'
    post4_ImageLink = parsedPost4['entities']['media'][0]['media_url'].encode('utf-8')
    post4_ImageComplete = '<img src="' + post4_ImageLink + '" >'

    post5_Text = parsedPost5['text'].encode('utf-8')
    post5_Name = parsedPost5['user']['screen_name'].encode('utf-8')
    post5_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post5_Name + '">'
    post5_ImageLink = parsedPost5['entities']['media'][0]['media_url'].encode('utf-8')
    post5_ImageComplete = '<img src="' + post5_ImageLink + '" >'

    post6_Text = parsedPost6['text'].encode('utf-8')
    post6_Name = parsedPost6['user']['screen_name'].encode('utf-8')
    post6_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post6_Name + '">'
    post6_ImageLink = parsedPost6['entities']['media'][0]['media_url'].encode('utf-8')
    post6_ImageComplete = '<img src="' + post6_ImageLink + '" >'

    post7_Text = parsedPost7['text'].encode('utf-8')
    post7_Name = parsedPost7['user']['screen_name'].encode('utf-8')
    post7_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post7_Name + '">'
    post7_ImageLink = parsedPost7['entities']['media'][0]['media_url'].encode('utf-8')
    post7_ImageComplete = '<img src="' + post7_ImageLink + '" >'

    post8_Text = parsedPost8['text'].encode('utf-8')
    post8_Name = parsedPost8['user']['screen_name'].encode('utf-8')
    post8_ProfileLink = '<a target="_blank" href="https://twitter.com/'+ post8_Name + '">'
    post8_ImageLink = parsedPost8['entities']['media'][0]['media_url'].encode('utf-8')
    post8_ImageComplete = '<img src="' + post8_ImageLink + '" >'

    print("Data Load Complete")

    # Site Work
    text_file = open("site/example.htm", "w")
    message =  """<html>
    <head><title>Twitter Feed Site</title>
    <link href="style/orpla.css" rel="stylesheet" type="text/css">

    </head>
    <body>
    <div class="contents">
    <div class="wrap">
    """ + post1_ProfileLink + """
    """ + post1_ImageComplete + """
    </a>
    <h3 class="desc">""" + post1_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post2_ProfileLink + """
    """ + post2_ImageComplete + """
    </a>
    <h3 class="desc">""" + post2_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post3_ProfileLink + """
    """ + post3_ImageComplete + """
    </a>
    <h3 class="desc">""" + post3_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post4_ProfileLink + """
    """ + post4_ImageComplete + """
    </a>
    <h3 class="desc">""" + post4_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post5_ProfileLink + """
    """ + post5_ImageComplete + """
    </a>
    <h3 class="desc">""" + post5_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post6_ProfileLink + """
    """ + post6_ImageComplete + """
    </a>
    <h3 class="desc">""" + post6_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post7_ProfileLink + """
    """ + post7_ImageComplete + """
    </a>
    <h3 class="desc">""" + post7_Text + """</h3>
    </div>
    <div class="wrap">
    """ + post8_ProfileLink + """
    """ + post8_ImageComplete + """
    </a>
    <h3 class="desc">""" + post8_Text + """</h3>
    </div>
    </div>
    <div class="footer">Example Twitter Feed Site - Images are not our own</div>
    </body>
    </html>"""

    text_file.write(message)

    text_file.close()

    print('Build Complete')

if __name__ == '__main__':
    # Call build_func to begin process
    build_func()
