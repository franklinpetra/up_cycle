from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

    #functions to allow users to request to see data from a list (materials) placed on a map 
    # 
    # function to show the routing options if they were to request the materials 

    # funtion to add materials from them to the map and then we should be able to serve them companies that could use those



    