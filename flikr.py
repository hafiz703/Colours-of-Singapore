import flickrapi
import json
 
api_key = u'1bba8d5e7c3b54769a93e24cf36e4f45'
api_secret = u'e62fc108ca0687e0'

def getflickrPhotos(lt,lng):
	directory = "./flickrPhotos/%s-%s"%(lt,lng)
	flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')	 
	data = flickr.photos.search(lat = lt,lon = lng,radius = 0.56)	 
	data = json.loads(data)
	 
	ls = data['photos']['photo']
	res = []
	x=0
	for i in ls:	 
		url = 'https://farm'+str(i['farm'])+'.staticflickr.com/'+str(i['server'])+'/'+str(i['id'])+'_'+str(i['secret'])+'_m.jpg'		 
		res.append(url)

	for j in res:
		print (j)
		urllib.urlretrieve(j, "./flickrPhotos/%s-%s/photo%d.jpg"%(lt,lng,x))
		x+=1
		 

	 

 