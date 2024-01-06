from urllib.parse import urlparse, unquote
import base64


def instagram_url_type(url):
    try:
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.split('/')
        if path_segments[1] == 'p':
            url_type = 'post'
            data = path_segments[2]
        elif path_segments[1] == 'stories':
            url_type = 'stories'
            data = path_segments[2]
        elif path_segments[1] == 'reel':
            url_type = 'reel'
            data = path_segments[2]
        else:
            url_type = 'username'
            data = path_segments[1]
        return url_type, data
    except Exception as e:
        raise Exception(f'can\'t determine url type')
