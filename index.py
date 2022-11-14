from pytube import YouTube
import requests
import shutil

def dowload_thumbnail(url, file_name):
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ' + file_name)
    else:
        print('Image Couldn\'t be retrieved')


def download(link):
    youtube_object = YouTube(link)
    thumbnail = youtube_object.thumbnail_url
    youtube_object = youtube_object.streams.get_highest_resolution()

    dowload_thumbnail(thumbnail, youtube_object.title + '.jpg')

    try:
        youtube_object.download()
    except:
        print('An error has occured')
    print('Download is completed successfully')

link = input('Enter the Yotube video URL: ')
download(link)
