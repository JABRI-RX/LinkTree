from django.shortcuts import render,get_object_or_404
from .models import LinkPage,Link
from urllib.parse import unquote
import uuid
 
# Create your views here.
def parse_post_data(request_body):
    # Convert the raw request body to a string
    data_str = request_body 

    # Split the data into key-value pairs based on the '&' separator
    key_value_pairs = data_str.split('&')

    # Create a dictionary to store the form data
    data_dict = {}

    # Iterate through the key-value pairs and populate the dictionary
    for pair in key_value_pairs:
        key, value = pair.split('=')
        data_dict[key] = value

    return data_dict

def browse(request):
    return render(request,"pages/browse.html",{})

def createPage(request):
    if request.method == "POST":
        links_data = parse_post_data(unquote(request.body)) 
        links_data.pop("csrfmiddlewaretoken")
        
        linkPage = LinkPage(title=links_data.get("title"),created_by=request.user,url=uuid.uuid4())
        print(linkPage.created_at)
        links_data.pop("title")

        #keys_list = list(links_data.keys())
        values_list = list(links_data.values())
        type_url = values_list[::2]
        link_url =  values_list[1::2]
        print(type_url)
        print(link_url)
        for i in range(len(type_url)):
            link = Link(type=type_url[i],url=link_url[i],linkPage=linkPage)
            print(type_url[i],link_url[i],linkPage)
        

    return render(request,"pages/create.html",{})

def updatePage(request):
    return render(request,"pages/update.html",{})

def DeletePage(request):
    return render(request,"pages/delete.html",{})

