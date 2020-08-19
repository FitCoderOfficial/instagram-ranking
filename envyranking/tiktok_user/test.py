from TikTokApi import TikTokApi
api = TikTokApi()

#print(api.getUser('woori88')) 

#scraper_list = api.getUserObject('coco_ysr')
 
scraper_list = api.getUser('just_grace')
xxx = api.byUsername('coco_ysr')
print(xxx)
print(scraper_list)



print(scraper_list['userInfo']['user']['id'])
print(scraper_list['userInfo']['user']['nickname'])
print(scraper_list['userInfo']['stats'])

