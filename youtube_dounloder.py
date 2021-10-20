from pytube import  YouTube as yt
url=input("ENTER THE URL OF YOUTUBE VIDEO")
data=yt(url)
data.streams.first().download()
print("Download sucessfull")