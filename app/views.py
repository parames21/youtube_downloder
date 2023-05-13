from django.shortcuts import render
from pytube import YouTube

def index(request):
    if request.method == 'POST':
        url = request.POST.get('video_url')
        resolution = request.POST.get('resolution')
        try:
            yt = YouTube(url)
            video = yt.streams.filter(res=resolution).first()
            video.download()
            message = "Video downloaded successfully!"
        except Exception as e:
            message = "Error: " + str(e)

        return render(request, 'index.html', {'message': message})

    return render(request, 'index.html')