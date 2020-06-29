# Notes Downloader

## Run

```
docker build -t notes_image . && docker run --rm -it -v "$PWD":/src -u `id -u`:`id -g` notes_image /bin/bash -c "python ./download_notes.py"
```