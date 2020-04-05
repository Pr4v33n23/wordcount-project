from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
    
def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()
    
    word_count_dictionary = {}
    
    for word in word_list:
        if word in word_count_dictionary:
            #Increase the count
            word_count_dictionary[word] += 1
        else:
            #add the word to dictonary
            word_count_dictionary[word] = 1
         
    sorted_words = sorted(word_count_dictionary.items(), key= operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'full_text': full_text, 'count': len(word_list), 'word_count_dictionary': sorted_words })   

def about(request):
    
    return render(request, 'about.html')