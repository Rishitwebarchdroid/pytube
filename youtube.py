from pytube import YouTube
                              
try:
    url = input("Enter url of the youtube video you want to download :")

    yt = YouTube(url)

    print("Title : ", yt.title)                     #give title of youtube video
    print("Views : ", yt.views)                     #give views of youtube video   

    yd = yt.streams.get_highest_resolution()        #give highresolution of video.

    yd.download("")                                 #give folder name where to download the video.
                                                

except Exception as e:
    print("Error occured : ", str(e))