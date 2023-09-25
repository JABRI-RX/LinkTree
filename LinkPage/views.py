from django.shortcuts import render,get_object_or_404
from .models import LinkPage,Link
from urllib.parse import unquote
from django.template import RequestContext
 
def parse_post_data(request_body):
# Create your views here.
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

def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def browse(request):
    
    return render(request,"pages/browse.html",{})

def linkpage_details(request,uuid):
    linkpage = get_object_or_404(LinkPage,uuid=uuid)
    links = Link.objects.filter(linkPage=linkpage)
    print(links)
    return render(request,"pages/linkpage_details.html",{"linkpage":linkpage,"links":links})

def createPage(request):
    mode =None
    if request.method == "POST":
        links_data = parse_post_data(unquote(request.body)) 
        links_data.pop("csrfmiddlewaretoken")
         
        title = links_data.get("title")
        print(title)
        created_by = request.user
        linkPage = LinkPage(title=title,created_by=created_by)
        linkPage.save()
        print(linkPage.id is None)

        links_data.pop("title")

        #keys_list = list(links_data.keys())
        values_list = list(links_data.values())
        type_url = values_list[::2]
        link_url =  values_list[1::2]
        print(type_url)
        print(link_url)
        
        for i in range(len(type_url)):
            link =  Link(type=type_url[i],url=link_url[i],linkPage=linkPage)
            link.save()
            print(link)
            print(f"type={type_url[i]},url={link_url[i]},linkPage={linkPage.created_by}")
        mode = 1
                
    return render(request,"pages/create.html", {"mode":mode})

def updatePage(request):
    mode = None
    linkPage = LinkPage.objects.filter(created_by=request.user)
    links = Link.objects.filter(linkPage__in=linkPage)
    title = linkPage[0].title
    print(linkPage)
    
    #to be implmeneted I dont have time
    # if request.method == "POST":
        
    #      = request.POST.get("title")

    return render(request,"pages/update.html",{"links":links,"title":title})

def DeletePage(request):
    if request.method == "POST":
        data = request.POST.getlist("selectedPageId")
        print(data)
        pageid = int([i for i in data if i ][0])
        linkpage = LinkPage.objects.get(id=pageid)
        linkpage.delete()

    linkPages = LinkPage.objects.filter(created_by=request.user)
    linksLengthInPages = []
    for page in linkPages:
        link = Link.objects.filter(linkPage=page)
        linksLengthInPages.append(len(link))

    return render(request,"pages/delete.html",{
    "linkPages":linkPages,
    "Pageslength":len(linkPages),
    "linksLength":linksLengthInPages
    })
