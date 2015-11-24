import eyed3

audiofile = eyed3.load("zedd_papercut_grey_remix.mp3")
audiofile.tag.artist = u"Zedd"
audiofile.tag.album = u"True Colors Remixes"
audiofile.tag.album_artist = u"Zedd"
audiofile.tag.title = u"Papercut ft. Troye Sivan (Grey Remix)"
audiofile.tag.track_num = 1

# read image into memory
imagedata = open("zedd_papercut_grey_remix.jpg","rb").read()

# append image to tags
audiofile.tag.images.set(3,imagedata,"image/jpg",u"Zedd Papercut Grey Remix Cover")

audiofile.tag.save()
