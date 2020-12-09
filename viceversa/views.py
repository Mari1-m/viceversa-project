from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def reverse(request):
    test_get_text = request.GET['usertext']
    print(test_get_text)
    reversed_text =test_get_text[::-1]
    return render(request, 'reverse.html', {'usertext':test_get_text, 'reversedtext': reversed_text})
