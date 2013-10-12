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
    """Uploads `blog_text` to our shared class tumblr blog http://llcpythonyvr.tumblr.com/

    hello_llc(blog_text) :: string -> None. Side-effect of creating a tumblr post.
    """
    result = client.create_text(hostname, body=blog_text)
    return HTML(
       '''<div style="padding: 15px">Uploading now.
       Click <a href="http://llcpythonyvr.tumblr.com/"
       target="new">here</a> to see your post!
       Tubmlr replied with some gobbledygook "%s" and an astro cat.</div>
       <img
       src="http://24.media.tumblr.com/b350f252a9460c6f9f3bb4af7702a566/tumblr_mllsjv1Qo01rmn2exo1_500.gif"
       />'''
       % result)

def mind_blown():
    return HTML('<img src="http://i.imgur.com/UmpOi.gif" />')
