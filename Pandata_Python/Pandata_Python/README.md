Pandata_Python is the crawling part of the Pandata project. It's written in Python and requires a MongoDB database to store the data. 

## Version

1.0.0

## Prerequisites
Make sure you have installed all these prerequisites on your development machine.
* MongoDB - [Download & Install MongoDB](http://www.mongodb.org/downloads), and make sure it's running on the default port (27017).
* Python - You're going to use [Python](https://www.python.org/) to crawl data from Twitter. In order to install Python dependencies, make sure you've installed [pip](https://pypi.python.org/pypi/pip). Then you can install Twython, Pymongo, Oauth & Oauthlib:

```
$ pip install twython
```
```
$ pip install pymongo
```
```
$ pip install oauth
```
```
$ pip install oauthlib
```

## How to use
Make sure MongoDB is running on the default port (27017). In order to start it, just go to 'C:\Program Files\MongoDB 2.6 Standard\bin' and run 'mongod'. 
Once it's done, you can open the solution Pandata_Python and edit the Variables.py file. Fill the fields you want to modify and run.
You'll see the data coming ('Tweets inserted' will be printed in the console each time).

## License
(The MIT License)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
