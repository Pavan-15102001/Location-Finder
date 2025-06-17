
import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919382922826")
phone_number2 = phonenumbers.parse("+918317513598")
phone_number3 = phonenumbers.parse("+917382922826")

print("\n Phone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));

