import tweepy


API_KEY = "YOUR API KEY"
API_SECRET_KEY = "YOUR API SECRET KEY"
BEARER_TOKEN = "YOUR BEARER TOKEN"
ACCESS_TOKEN = "YOUR ACCESS TOKEN"
ACCESS_TOKEN_SECRET = "YOUR ACCESS TOKEN SECRET"
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

friends = []

print("\n=========\n")

user_id = input("フォロー・フォロワー欄を取得したいID\n>> ")

check = True
while check:
	follow_or_follower = input("\n選択してください\n1. フォロー\n2. フォロワー\n>> ")
	if follow_or_follower == "1" or follow_or_follower == "2":
		check = False
	else:
		print("1か2を半角で入力してください")

if follow_or_follower == "1":
	for account in tweepy.Cursor(api.get_friends, screen_name=user_id).items():
		print(account.screen_name)

elif follow_or_follower == "2":
	for account in tweepy.Cursor(api.get_followers, screen_name=user_id).items():
		print(account.screen_name)

print("\n=========\n")
