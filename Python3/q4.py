string="My linkedIn profile url is https://www.linkedin.com/in/mohammad-muazam-129838190/"
start=string.find("https://")
end=string.find(" ",start)
print(string[start:end])