# soni.lite

A simple audio player based on sqlite database.

Works only on Windows, however if you are a Linux user you are able to make it work on your os.

Features:
- Only black theme
- Store audio data in your library
- Combine your audios into playlists
- Play playlists in audio player
- The player has random and loop playback functions

![image](https://github.com/FSK-idk/soni-lite/assets/81324348/117f64f9-bb3d-4718-96b4-76d853e0e23a)


## installation

Clone repository to your local folder

```
git clone git@github.com:FSK-idk/soni-lite.git
```

Download required packages from requirements.txt

```
pip install -r requirements.txt
```

Compile `soni/resources/resources.qrc` file

```
pyside6-rcc soni/resources/resources.qrc -o soni/resources/resources_rc.py
```

Launch program
```
python soni/main.py
```

## about

It is a project for my subject at university.

It is only a light version of the application. Using PySide doesn't seem to be a very good option. The project may be continued with a different gui framework.
