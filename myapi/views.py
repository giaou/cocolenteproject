# from django.http import HttpResponse
import json

import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_world(request):
    return Response({'message': getAPokemon()})
    # return HttpResponse("Hello, world")


def getAPokemon():
    url = "https://pokeapi.co/api/v2/pokemon/ditto"

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # poke_type = data.get("types")
        name = data.get("name")
        image = data.get("sprites").get("front_shiny")
        pokemon={
            "name":name,
            "image":image
        }

        json_pokemon = json.dumps(pokemon)
        return(json_pokemon)

    else:
        return(f"Failed to retrieve data: {response.status_code}")