import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your no. :")
phone = phonenumbers.parse(number)#this function give us all information
time = timezone.time_zones_for_number(phone, "en")
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(car)
print(reg)