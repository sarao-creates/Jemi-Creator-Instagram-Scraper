from instaloader import Instaloader, Hashtag, Profile
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
# How to link to a spreadsheet: https://www.youtube.com/watch?v=cnPlKLEGR7E&ab_channel=TechWithTim
scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("./creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Jemi Hashtag Scraper").sheet1

# How to use InstaLoader: https://instaloader.github.io/module/structures.html
loader = Instaloader()
loader.load_session_from_file("sameer__rao") # You'll need to put your instagram username here.
users = []
count = 600
hashtag = Hashtag.from_name(loader.context, 'Patreon')


for post in hashtag.get_posts():
    try:
        if post.owner_profile.followers > 20000:
            link = 'https://instagram.com/' + post.owner_profile.username + '/'
            count += 1
            print(post.owner_profile.username)
            sheet.insert_row([post.owner_profile.full_name, post.owner_profile.followers, post.owner_profile.biography, post.owner_profile.external_url, link], count)
    except:
        print('sleeping')
        time.sleep(3600) # I usually had the scraper sleep for 60 mins on any error thrown. this only kinda worked
print('done')