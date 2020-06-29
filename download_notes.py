from urllib.request import urlopen
from urllib.error import URLError, HTTPError

lessons = []

for mod in [3, 4]:
    for lesson_num in range(1, 30):
        lessons.append(tuple((mod, lesson_num)))

for tup in lessons:
    module = tup[0]
    lesson = tup[1]

    filename = "G01M{0:0=2d}L{1:0=2d}_MC_StudentNotes_4thEd.pdf".format(
        module, lesson
    )
    url = "https://webassets.zearn.org/lesson_pdfs/G01M{0:0=2d}/{1}".format(
        module, filename
    )
    print("Opening url: {}".format(url))
    try:
        filedata = urlopen(url)
    except HTTPError as e:
        print("The server couldn't fulfill the request.")
        print("Error code: ", e.code)
    except URLError as e:
        print("We failed to reach a server.")
        print("Reason: ", e.reason)
    else:
        datatowrite = filedata.read()

        with open("./Notes/{}".format(filename), "wb+") as f:
            f.write(datatowrite)
