import eyed3

#enter the actual file name of the mp3 file here
audiofile = eyed3.load("name_of.mp3")

#name of the artist
audiofile.tag.artist = u"Artist Name"

#name of the album, be creative for singles
audiofile.tag.album = u"Album Name"

# tbh I'm not sure what the difference is between "Artist" and "Artist Album"
audiofile.tag.album_artist = u"Artist Album"

#name of the track, this may differ from the actual file name
audiofile.tag.title = u"Papercut ft. Troye Sivan (Grey Remix)"

#number of the track on the overall album
audiofile.tag.track_num = 1

# read image into memory
imagedata = open("zedd_papercut_grey_remix.jpg","rb").read()

# append image to tags
audiofile.tag.images.set(3,imagedata,"image/jpg",u"Zedd Papercut Grey Remix Cover")

audiofile.tag.save()
