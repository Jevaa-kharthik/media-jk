## Project description

### A Simple Wrapper tool for mediainfo

### Prerequisites
- This tool needs mediainfo to be installed to work properly
-  On Ubuntu/Debian :
```Sudo apt install media_jk ```
 OR
``` apt install media_jk ```
- On Mac :
``` brew install media_jk ```

### Usage :
- To get all avaible information about the video, Audio and Image file.
- It works will all media type 
``` media_jk --file= --type=<General,Audio,Video> --list-Keys ```
- If it is a Video file :
``` --type=<General,Audio,Video> ```
- If it is a Audio file :
``` --type=<General,Audio> ```
- If it is a Image file :
``` --type= ''' To get a particular key about the file ''' media_jk --file= --type=<General,Audio,Video> --keys="list name" ```
