favorite_languages ={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
print(f"Jen's favorite language is {favorite_languages['jen'].title()}.")

print(favorite_languages.get('rich','not found'))