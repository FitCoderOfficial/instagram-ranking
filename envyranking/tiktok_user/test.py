from TikTokApi import TikTokApi
api = TikTokApi()

#print(api.getUser('woori88')) 

scraper_list = api.getUserObject('just_grace')
 
scraper_list2 = api.getUser('just_grace')


for e in scraper_list2:
    print(e)

print(scraper_list2['userInfo']['stats'])

