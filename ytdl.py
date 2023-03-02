from pytube import YouTube

#ask for the link from user
def yt(link:str)->dict:
    '''
    Pass a youtube link and it'll return a dictonary of streams and video details
    Example: {
        "title":Video title,
        "views":Video views,
        "length":Video length,
        "videos": Progressive mp4 streams,
        "audios": All audio streams 
        
    }
    '''
    youtude = YouTube(link)
    videos=youtude.streams.filter(progressive=True, file_extension="mp4")
    youtubedict={
        "url":link,
        "thumb":youtude.thumbnail_url,
        "title":youtude.title,
        "views":youtude.views,
        "length":youtude.length,
        "videos":videos,
        "audios":youtude.streams.filter(type="audio")
        }
    return youtubedict

# ytdict=yt("https://youtu.be/SXiSVQZLje8")
# for i in ytdict['videos']:
#     print(i.resolution)
# vids = ytdict["videos"]
# bitrates = ["144p","240p","360p","480p","720p","1080p","1440p","2160p"]
# for r in bitrates:
#     s=vids.get_by_resolution(r)
#     if s is not None:
#         print(s.url)