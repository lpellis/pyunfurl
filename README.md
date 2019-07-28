# PyUnfurl

PyUnfurl is a Python library for embedding ('unfurling') content from other sites into your own site, similar to the way slack expands links.  
Useful for easily embedding tweets, YouTube videos, StackOverflow posts or content from any other site.

### Features
* Supports all oEmbed providers from [https://oembed.com/](https://oembed.com/) and [https://noembed.com/](https://noembed.com/) by default.
* Supports the [autodiscovery](https://oembed.com/#section4) part of the oEmbed spec.
* Support for [Open Graph](https://ogp.me/) protocol.
* Support for [Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards.html)
* Falls back to Meta tags and the site favicon/title if all else fails.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyunfurl.

```bash
pip install pyunfurl
```

## Usage

```python
import pyunfurl
pyunfurl.unfurl('https://www.youtube.com/watch?v=aBr2kKAHN6M') 
```
This will return a dict similar to the oembed spec:
```
{
	'method': 'oembed', # one of 'oembed', 'twitter_card', 'open_graph', 'meta_tags', 'custom'
	'site': 'YouTube', 
	'domain': 'youtube.com', 
	'title': 'Live Views of Starman', 
	'description': '', 
	'image': '', 
	'favicon': '',  # only included if no image was found 
	'url': 'https://www.youtube.com/watch?v=aBr2kKAHN6M', 
	'type': 'rich', 
	'html': '\n<iframe width=" 480" height="270" src="https://www.youtube.com/embed/aBr2kKAHN6M?feature=oembed" frameborder="0" allowfullscreen="allowfullscreen"></iframe>\n'
}
```
You can use the `html` entry to directly include the content on your site.

## Styling
For non oembed content (eg OpenGraph entries such as StackOverflow) PyUnfurl returns a html structure like the following:
```
pyunfurl.unfurl('https://stackoverflow.com/questions/509211/understanding-slice-notation')['html']
```
```
<div class="unfurl unfurl-image">
    <a rel="noopener nofollow" target="_blank" href="https://stackoverflow.com/questions/509211/understanding-slice-notation">
        <img src="https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon@2.png?v=73d79a89bded">
    </a>
    <div class="unfurl-content">
        <a class="unfurl-title" href="https://stackoverflow.com/questions/509211/understanding-slice-notation">Understanding slice notation</a>
        <div>I need a good explanation (references are a plus) on Python's slice notation. 
To me, this notation needs a bit of picking up. 
It looks extremely powerful, but I haven't quite got my head around...</div>
        <a class="unfurl-domain" href="https://stackoverflow.com/questions/509211/understanding-slice-notation">stackoverflow.com</a>
    </div>
</div>

```
You can style this any way you want, a good starting point is to include the following css on your site:
```
 div.unfurl{
        font-family: helvetica, arial, sans-serif;
        font-size:15px;
        border:1px solid #ebebeb;
        border-radius: 8px;
        display:flex;
        align-items: center;
        text-align: left;
    }
    div.unfurl img {
        width: 120px;
        background-color: #ebebeb;
     }
    div.unfurl-favicon img {
        width: 80px;
        padding:20px;
        background-color: #ebebeb;
    }
    div.unfurl-content a{
        color:black;
        display: inline-block;
        font-weight: bold;
        text-decoration: none;
        line-height:30px;
        text-overflow: ellipsis;
        overflow: hidden;
        min-width: 10px;
        white-space: nowrap;
        width:100%;
    }
    div.unfurl-content a.unfurl-domain{
        color:gray;
        font-weight: normal;
    }
    div.unfurl-content{
        flex:1;
        margin-left:10px;
        margin-right:10px;
        min-width: 10px;
        width:100%;
    }
    div.unfurl-content div{
        line-height:18px;
        max-height:54px;
        overflow:hidden;
    }
```
This will generate a card looking like:

![img](https://i.imgur.com/1CMJjJq.png)

## Contributing
Pull requests are welcome. PyUnfurl supports some custom integrations for sites that doesnt return any meta tags, if you want to improve the integration for a specific site you can look at the hackernews example.

## License
[MIT](https://choosealicense.com/licenses/mit/)
