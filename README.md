# What is it

Average color detecting plugin for thumbor [https://github.com/thumbor/thumbor](https://github.com/thumbor/thumbor)

Allows detecting average color and returning value in response headers of the image

### Example:
Request:

`curl 'http://localhost:8888/unsafe/300x210/filters:avg_color()/https://url/to/image.jpg'`

Response Headers contain header `x-avg-color` with the value of the average color:

```
HTTP/1.1 200 OK
...
X-Avg-Color: d5d4d4
...
```


# How to

1. Install the plugin: `pip install thumbor_avg_color`

2. Modify `thumbor.conf` to enable average color detecting:

Add avg_color to filters list
```
FILTERS = [
        # // your filters here
        'thumbor_avg_color.filters.avg_color',
    ]
```

Change app class of the ThumborServiceApp by replacing line with line:
```
APP_CLASS = 'thumbor_avg_color.app.App'
```

3. Run with new config

`thumbor -c ./thumbor.conf`
