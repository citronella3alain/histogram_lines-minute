# histogram_lines-minute
Google Code-In 2017:
This program takes a subtitle file (srt) and outputs the number of subtitles created per minute and a histogram that reflects this data. The number of subtitles per minute is based on the starting time of the subtitle.
## Usage
```
python histogram_lines-minute.py <file.srt>
```
## Example
**Input**
```
python histogram_lines-minute.py 04-BBC4.srt
```
**Output**
```
04-BBC4.srt
Minute	Frames
0	9 +++++++++
1	9 +++++++++
2	1 +
Total: 19
```
## Built With
* [Python](https://www.python.org/) - A general purpose programming language.
* [pysrt](https://pypi.python.org/pypi/pysrt) - Used to parse srt files.
## Author
* Allen Mao
