from populate import base
from home.models import User

def populate():
    print('Creating user accounts')
    User.objects.all().delete()
    for i in range(10):
        account_number='B00'+str(i)
        password = '1234abcd'
        name = 'user'+str(i)
        User.objects.create(account_number=account_number,password=password,name=name,email='1234@test.com')
    print('done')

if __name__=='__main__':
    populate()