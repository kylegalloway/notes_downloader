from urllib.request import urlopen
from urllib.error import URLError, HTTPError

for i in range(1, 39):
    filename = "G01M01L{0:0=2d}_MC_StudentNotes_4thEd.pdf".format(i)
    url = "https://webassets.zearn.org/lesson_pdfs/G01M01/{}".format(filename)
    print("Opening url: {}".format(url))
    try:
        filedata = urlopen(url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        datatowrite = filedata.read()

        with open("./Notes/{}".format(filename), "wb+") as f:
            f.write(datatowrite)
