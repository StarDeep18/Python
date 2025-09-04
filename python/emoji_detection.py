import emoji #importing emoji library
emojis = []
text = input("\nEnter the text with emojis: ") #getting input
for i in text:
    if emoji.is_emoji(i): #checking if its emoji
        emojis.append(i) #appending the emoji to list
if emojis:
    print("✅ Emojis found:", emojis) 
    for j in emojis:
        print(f"{j} --> {emoji.demojize(j)}") #demojizing the emoji