# picymru/exchange

[![Docker Repository on Quay](https://quay.io/repository/picymru/exchange/status "Docker Repository on Quay")](https://quay.io/repository/picymru/exchange) [![GitHub license](https://img.shields.io/github/license/picymru/exchange.svg)]()

We're committed to being open about how we work, so how better than to completely open source our website!

## Building
    docker build -t picymru/exchange .

## Running
### Using docker
    docker run -e HOST=0.0.0.0 -e PORT=80 -p 80:80 quay.io/picymru/exchange
### Using docker-compose
    version: '2'
    services:
      picymru:
        image: quay.io/picymru/exchange
        ports:
          - "80:80"
        environment:
          - APP_MODE = 'prod'
    
## License
    MIT License
    
    Copyright (c) 2016 Matthew Gall
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.