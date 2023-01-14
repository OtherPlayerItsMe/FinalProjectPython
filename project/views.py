from django.shortcuts import render

def index_page(reqest):
    return render(reqest, 'index.html')

def relevance_page(reqest):
    return render(reqest, 'relevance.html')

def geograf_page(reqest):
    return render(reqest, 'geograf.html')

def skill_page(reqest):
    return render(reqest, 'skill.html')

def lastvacans_page(reqest):
    return render(reqest, 'lastvacans.html')

