import phonenumbers

from phonenumbers import geocoder

phone = input("Digite um telefone +551174589680 como no padrão impresso: ")

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))