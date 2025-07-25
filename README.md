# Parse the folder/file name and extract relevant information

### Example Usage

```bash
python3 src/rename_media.py "/path/to/folder" --pattern "{title} ({year}) - S{season:02}E{episode:02}"
```

For a file like: 

```
Game.of.Thrones.S01E01.720p.HDTV.x264.mkv
```

It would rename it to: 
```
Game of Thrones (2011) - S01E01.mkv
```


