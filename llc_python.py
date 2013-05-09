import pytumblr
from IPython.core.display import HTML

## misc people off the internet seeing this stuff, please behave!
hostname = 'llcpythonyvr.tumblr.com'
consumer_key = 'hS4941NymGq8rSNlli6j5HnvQj7cXPnXHljEOzr7A6PDJW5Bpb'
consumer_secret = 'jyKtPAeXjF1kCiNnBYZdQVWN1gMZlZ7zsRqCYva1SB5EpHXuhX'
access_token_secret, access_token_key = (
  'SFSz9f6Cp9iRWPUV1uZfZmhMF7wCAIibQG5oROZmjs3qfCgQ1b',
  'uZeAZYkh6GpAGKHTTCGLDNcJmmEn5Ki3VXUqV7q4X6pElDZZOb')
##

client = pytumblr.TumblrRestClient(
    consumer_key, consumer_secret,
    access_token_key, access_token_secret)

def hello_llc(blog_text):
    """hello_llc(blog_text) :: string -> None. Side-effect of creating a tumblr post.

    Upload `blog_text` to our shared class tumblr blog http://llcpythonyvr.tumblr.com/
    """
    result = client.create_text(hostname, body=blog_text)
    return HTML(
       '''Uploading now.
       Click <a href="http://llcpythonyvr.tumblr.com/" target="new">here</a> for the post.
       Tubmlr replied "%s".'''
       % result)
