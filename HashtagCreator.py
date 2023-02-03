import random

hashtags = ["#love","#extreme","#reeloftheday","#beautiful","#trick","#videooftheday","#happy","#follow","#nature","#instagram","#travel","#like4like","#style","#repost","#summer","#instadaily","#beauty","#friends","#instalike","#me","#smile","#family","#video","#life","#likeforlike","#music","#follow4follow","#amazing","#igers","#nofilter","#sunset","#beach","#motivation","#instamood","#lifestyle","#followforfollow","#sky","#l4l","#f4f","#likeforlikes"]
print(len(hashtags))

def generate_hashtag():
  hasthag_for_post = []
  for i in range(30):
    hastag = hashtags[random.randint(0,39)]
    if(hastag not in hasthag_for_post):
      hasthag_for_post.append(hastag)
  
  print(len(hasthag_for_post))
  return hasthag_for_post

with open("hastags.txt","w") as f:
  for hastag in generate_hashtag():
    f.write(f"{hastag} ")
