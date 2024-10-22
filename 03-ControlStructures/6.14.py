# An influencer is a person who can influence other people's behaviour. 
# An influencer communicates with other people using social networking sites. 
# Write a program that checks whether a given person is a good influencer,
# that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. 
# Use logical type variables: facebook, twitter, instagram,
# the value of which indicates whether the person has an account on the social networking site.
# Sample result:
# facebook = True
# twitter = False
# instagram = True
# You are a good influencer!

facebook = bool(input("Do you have an account on facebook (if yes type: True otherwise type False)"))
twitter = bool(input("Do you have an account on twitter (if yes type: True otherwise type False)"))
instagram = bool(input("Do you have an account on instagram (if yes type: True otherwise type False)"))
account = [facebook, twitter, instagram]
yes = account.count(False)
print(yes)
if yes <=1 :
    print("You are a good influencer!")
else:
    print("You are a bad influencer!")