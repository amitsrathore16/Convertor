from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        num = int(request.POST.get('number'))
        word = int_to_en(num)
        return render(request, 'home.html', {'word': word})
    return render(request, 'home.html', {})


def int_to_en(num):
    d = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
         11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
         15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
         19: 'Nineteen', 20: 'Twenty',
         30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
         70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
    k = 1000
    m = k * 100

    if num < 1 or num > 1000000:
        return 'Please enter a number between 1 and 1000000'

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + ' ' + d[num % 10]

    if num < k:
        if num % 100 == 0:
            return d[num // 100] + ' Hundred'
        else:
            return d[num // 100] + ' Hundred and ' + int_to_en(num % 100)

    if num < m:
        if num % k == 0:
            return int_to_en(num // k) + ' Thousand'
        else:
            return int_to_en(num // k) + ' Thousand ' + int_to_en(num % k)

    if num >= m:
        if num % m == 0:
            return int_to_en(num//m) + ' Lakh '
        else:
            return  int_to_en(num//m) + ' Lakh ' + int_to_en(num % m)
