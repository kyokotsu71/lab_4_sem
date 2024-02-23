import requests

request_string = ('https://belarusbank.by/api/atm')
my_params = {
    'city': 'Яя',
    'ATM_currency': 'USD,BYN'
}
response = requests.get(request_string, params=my_params)

if response:
    s = str(response.content, "utf-8")
    print(s)
    '''
    A = response.json()  # statham
    B = A[3]
    C = B['EURCARD_out']
    print(C)
    '''
    # print(response.content)

    # print(A)
else:
    print('Что-то пошло не так.')
    print(f'Код ответа: {response.status_code}')
    print(f'Причина: {response.reason}')
