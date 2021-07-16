import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Search
BASE_CRAIGLIST_URL='https://losangeles.craigslist.org/search/bbb?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
def home(request):
    return render(request,'base.html',{})
def new_search(request):
    search_dict=request.POST['search']
    Search.objects.create(search=search_dict)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search_dict))
    data = requests.get(final_url).text
    soup = BeautifulSoup(data,features='html.parser')
    post_listings = soup.find_all('li',{'class':'result-row'})

    final_post_list=[]
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url= post.find('a').get('href')

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'https://kiyanfox.com/wp-content/uploads/2019/03/Image-not-found-300x300.gif'
        final_post_list.append((post_title,post_url,post_image_url))

        front_dic={
        'search_dict':search_dict,
        'final_post_list':final_post_list,

        }



    return render(request,'my_app/index.html',front_dic)
