import random
lower_case="qwertyuiopasdfghjklzxcvbnm"
upper_case="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
symbol="!@#$%^&*()_+~"

use_for=lower_case+upper_case+number+symbol
length=8
pswd="".join(random.sample(use_for,length))
print("enter the passwoed:",pswd)

