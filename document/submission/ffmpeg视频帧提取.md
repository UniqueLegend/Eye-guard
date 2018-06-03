ffmpeg是一套可以用来记录、转换音频、视频格式，并可以将其转换成流的开源计算机程序，采用GPL许可证。它的[官网](http://ffmpeg.org/about.html),wiki百科[地址](https://en.wikipedia.org/wiki/FFmpeg),github项目[地址](https://github.com/FFmpeg/FFmpeg)。ffmpeg是提供了视音频录制、格式转换、采集以及流化的全套功能。ffmpeg提供编译好的程序包使用命令行参数进行交互。视频采集需要用到的命令行参数如下：
* -t 指定采集时长
* -s 指定采集帧的大小
* -i 指定源文件
* -f 指定文件格式
* -r 指定每秒采集帧的数目
* -vcodec 指定视屏编码格式
 通过上述参数调用ffmeg即可以快速的使用ffmpeg实现简单的视屏摘要提取。