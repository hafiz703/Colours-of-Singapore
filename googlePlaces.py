from googleplaces import GooglePlaces, types, lang
from PIL import Image
import rawpy
import imageio
import urllib
import os

YOUR_API_KEY = 'AIzaSyBdJIjNif2GrjJNoLm3XHztebChSFd6KxI'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
def getPhotos(lat,lng):
    directory = "./GooglePhotos/%s-%s"%(lat,lng)
    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    query_result = google_places.nearby_search(
            lat_lng = {'lat':lat,'lng':lng},
            # location='Singapore', keyword='Bishan',
            # types = [types.TYPE_PARK,types.TYPE_NEIGHBORHOOD,types.TYPE_NATURAL_FEATURE,types.TYPE_LOCALITY],
            radius=560)
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:
    # http://googlegeodevelopers.blogspot.com.au/2016/02/changes-and-quality-improvements-in_16.html

    if query_result.has_attributions:
        print(query_result.html_attributions)

    x = 0
    for place in query_result.places:
        # Returned places from a query are place summaries.
        # print(place.name)
        # print place.geo_location
        # print place.place_id

        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print place.details # A dict matching the JSON response from Google.
        # print place.local_phone_number
        # print place.international_phone_number
        # print place.website
        # print place.url

        # Getting place photos
        
        for photo in place.photos:
           
            
            # 'maxheight' or 'maxwidth' is required
            photo.get(maxheight=500, maxwidth=500)
            # MIME-type, e.g. 'image/jpeg'
            photo.mimetype
            # Image URL
            # print photo.filename
            print photo.url
            urllib.urlretrieve(photo.url, "./GooglePhotos/%s-%s/photo%d.jpg"%(lat,lng,x))         
            x+=1


    # Are there any additional pages of results?
    if query_result.has_next_page_token:
        query_result_next_page = google_places.nearby_search(
                pagetoken=query_result.next_page_token)


 