# Webアプリケーションのパフォーマンス改善

## setup
<pre>
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U Flask
$ pip install gunicorn
$ pip freeze
Flask==1.0.2
gunicorn==19.9.0
</pre>
<pre>
$ sudo apt install apache2-utils
$ ab -V
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
</pre>

## start web app
<pre>
$ python norilog.py
</pre>

## os spec
<pre>
Ubuntu 17.10
Intel® Core™ i5-4210M CPU @ 2.60GHz × 4
7.7 GiB
</pre>

## exec apache bench

■トータル1000リクエストを100コネクション並列で送信
<pre>
$ ab -n 1000 -c 100 http://0.0.0.0:8000/
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        Werkzeug/0.14.1
Server Hostname:        0.0.0.0
Server Port:            8000

Document Path:          /
Document Length:        9674 bytes

Concurrency Level:      100
Time taken for tests:   3.310 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      9830000 bytes
HTML transferred:       9674000 bytes
Requests per second:    302.14 [#/sec] (mean)
Time per request:       330.971 [ms] (mean)
Time per request:       3.310 [ms] (mean, across all concurrent requests)
Transfer rate:          2900.44 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.6      0       4
Processing:    46  314  54.2    328     364
Waiting:       15  312  54.4    325     359
Total:         49  315  53.6    328     365

Percentage of the requests served within a certain time (ms)
  50%    328
  66%    334
  75%    337
  80%    339
  90%    344
  95%    348
  98%    352
  99%    355
 100%    365 (longest request)
</pre>

■トータル5000リクエストを500コネクション並列で送信
<pre>
$ ab -n 5000 -c 500 http://0.0.0.0:8000/
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
apr_socket_recv: Connection reset by peer (104)
Total of 4358 requests completed
</pre>

■トータル3000リクエストを200コネクション並列で送信
<pre>
$ ab -n 3000 -c 200 http://0.0.0.0:8000/
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 300 requests
Completed 600 requests
Completed 900 requests
Completed 1200 requests
Completed 1500 requests
Completed 1800 requests
Completed 2100 requests
Completed 2400 requests
Completed 2700 requests
Completed 3000 requests
Finished 3000 requests


Server Software:        Werkzeug/0.14.1
Server Hostname:        0.0.0.0
Server Port:            8000

Document Path:          /
Document Length:        9674 bytes

Concurrency Level:      200
Time taken for tests:   14.480 seconds
Complete requests:      3000
Failed requests:        0
Total transferred:      29490000 bytes
HTML transferred:       29022000 bytes
Requests per second:    207.18 [#/sec] (mean)
Time per request:       965.322 [ms] (mean)
Time per request:       4.827 [ms] (mean, across all concurrent requests)
Transfer rate:          1988.89 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   82 310.2      0    3039
Processing:    31  591 1499.8    415   13454
Waiting:        8  588 1499.8    413   13454
Total:         41  673 1640.2    416   14470

Percentage of the requests served within a certain time (ms)
  50%    416
  66%    421
  75%    424
  80%    426
  90%    435
  95%   1432
  98%   2282
  99%  14378
 100%  14470 (longest request)
</pre>

## use gunicorn

CPUコア数 4 のため、ワーカープロセス（`-w`）も 4 で起動
<pre>
$ gunicorn -w 4 -b 0.0.0.0:8000 norilog
</pre>

## exec apache bench

■トータル5000リクエストを500コネクション並列で送信
<pre>
$ ab -n 5000 -c 500 http://0.0.0.0:8000/
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 500 requests
Completed 1000 requests
Completed 1500 requests
Completed 2000 requests
Completed 2500 requests
Completed 3000 requests
Completed 3500 requests
Completed 4000 requests
Completed 4500 requests
apr_pollset_poll: The timeout specified has expired (70007)
Total of 4777 requests completed
</pre>

■トータル3000リクエストを200コネクション並列で送信
<pre>
$ ab -n 3000 -c 200 http://0.0.0.0:8000/
This is ApacheBench, Version 2.3 <$Revision: 1796539 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 0.0.0.0 (be patient)
Completed 300 requests
Completed 600 requests
Completed 900 requests
Completed 1200 requests
Completed 1500 requests
Completed 1800 requests
Completed 2100 requests
Completed 2400 requests
Completed 2700 requests
Completed 3000 requests
Finished 3000 requests


Server Software:        gunicorn/19.9.0
Server Hostname:        0.0.0.0
Server Port:            8000

Document Path:          /
Document Length:        9674 bytes

Concurrency Level:      200
Time taken for tests:   2.740 seconds
Complete requests:      3000
Failed requests:        0
Total transferred:      29508000 bytes
HTML transferred:       29022000 bytes
Requests per second:    1094.93 [#/sec] (mean)
Time per request:       182.661 [ms] (mean)
Time per request:       0.913 [ms] (mean, across all concurrent requests)
Transfer rate:          10517.29 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   25 157.2      0    1029
Processing:    14  144 220.0    111    1718
Waiting:       14  144 220.0    111    1718
Total:         23  170 369.4    111    2731

Percentage of the requests served within a certain time (ms)
  50%    111
  66%    118
  75%    120
  80%    121
  90%    125
  95%    126
  98%   1970
  99%   2707
 100%   2731 (longest request)
</pre>
