from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items()})

#공백포함    
def blank(request):    
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
            # add to dictionary
            word_dictionary[word]=1
    total = len(words)*2 -1

    return render(request, 'result.html', {'full': text, 'total' : total, 'dictionary' : word_dictionary.items()})
    # 공백 포함 총 단어 수는 그냥 위 단어 수에 공백만큼을 더해주면 된다.
    # 공백의 수는 단어 수 -1 이다