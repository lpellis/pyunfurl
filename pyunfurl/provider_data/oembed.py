OEMBED_PROVIDER_LIST = [
    [
        "https://(\\S*\\.)?youtu(\\.be/|be\\.com/watch)\\S+",
        "http://www.youtube.com/oembed?scheme=https&",
    ],
    [
        "http://(\\S*\\.)?youtu(\\.be/|be\\.com/watch)\\S+",
        "http://www.youtube.com/oembed",
    ],
    ["https?://wordpress\\.tv/\\S+", "http://wordpress.tv/oembed/"],
    ["http://\\S+\\.wordpress\\.com/\\S+", "http://public-api.wordpress.com/oembed/"],
    ["https://vimeo\\.com/\\S+", "https://vimeo.com/api/oembed.json"],
    ["http://vimeo\\.com/\\S+", "http://vimeo.com/api/oembed.json"],
    [
        "https?://(www\\.)?twitter\\.com/\\S+/status(es)?/\\S+",
        "https://api.twitter.com/1/statuses/oembed.json",
    ],
    ["https?://(?:www\\.)?scribd\\.com/\\S*", "http://www.scribd.com/services/oembed"],
    ["https?://speakerdeck\\.com/\\S*", "https://speakerdeck.com/oembed.json"],
    ["https://\\S*?soundcloud\\.com/\\S+", "http://soundcloud.com/oembed"],
    ["http://\\S*\\.smugmug\\.com/\\S*", "http://api.smugmug.com/services/oembed/"],
    ["https?://slidesha\\.re/\\S*", "http://www.slideshare.net/api/oembed/2"],
    [
        "https?://(?:www\\.)?slideshare\\.net/[^\\/]+/\\S+",
        "http://www.slideshare.net/api/oembed/2",
    ],
    ["https?://(.+\\.)?polldaddy\\.com/\\S*", "http://polldaddy.com/oembed/"],
    [
        "http://www\\.polleverywhere\\.com/(polls|multiple_choice_polls|free_text_polls)/\\S+",
        "http://www.polleverywhere.com/services/oembed/",
    ],
    ["http://gi\\S*\\.photobucket\\.com/groups/\\S+", "http://photobucket.com/oembed"],
    ["http://i\\S*\\.photobucket\\.com/albums/\\S+", "http://photobucket.com/oembed"],
    ["http://moby\\.to/\\S*", "http://api.mobypicture.com/oEmbed"],
    [
        "http://www\\.mobypicture\\.com/user/\\S*?/view/\\S*",
        "http://api.mobypicture.com/oEmbed",
    ],
    [
        "https?://(www\\.)?instagr(\\.am|am\\.com)/p/\\S+",
        "http://api.instagram.com/oembed",
    ],
    ["https?://\\S*imgur\\.com/\\S+", "https://api.imgur.com/oembed"],
    ["http://(?:www\\.)hulu\\.com/watch/\\S+", "http://www.hulu.com/api/oembed.json"],
    ["https?://gist\\.github\\.com/\\S*", "https://github.com/api/oembed"],
    [
        "https?://(?:www\\.)?funnyordie\\.com/videos/\\S+",
        "http://www.funnyordie.com/oembed",
    ],
    ["https?://flic\\.kr/\\S*", "https://www.flickr.com/services/oembed/"],
    ["https?://\\S*?flickr\\.com/\\S+", "https://www.flickr.com/services/oembed/"],
    [
        "https?://(?:www\\.)?dailymotion\\.com/\\S+",
        "http://www.dailymotion.com/services/oembed",
    ],
    [
        "https?://www\\.circuitlab\\.com/circuit/\\S+",
        "https://www.circuitlab.com/circuit/oembed",
    ],
    ["http://chirb\\.it/\\S+", "http://chirb.it/oembed.json"],
    [
        "https://(\\S*\\.)?youtu(\\.be/|be\\.com/watch)\\S+",
        "http://www.youtube.com/oembed?scheme=https&",
    ],
    [
        "http://(\\S*\\.)?youtu(\\.be/|be\\.com/watch)\\S+",
        "http://www.youtube.com/oembed",
    ],
    [
        "https://reports.zoho.com/ZDBDataSheetView.cc\\?OBJID=1432535000000003002&STANDALONE=true&INTERVAL=120&DATATYPESYMBOL=false&REMTOOLBAR=false&SEARCHBOX=true&INCLUDETITLE=true&INCLUDEDESC=true&SHOWHIDEOPT=true",
        "http://api.provider.com/oembed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.znipe.tv/[^\\/\\s\\?&]+?",
        "https://api.znipe.tv/v3/oembed/",
    ],
    ["https://youtu.be/[^\\/\\s\\?&]+?", "https://www.youtube.com/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.youtube.com/v/[^\\/\\s\\?&]+?",
        "https://www.youtube.com/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.youtube.com/watch[^\\/\\s\\?&]+?",
        "https://www.youtube.com/oembed",
    ],
    ["http://yfrog.us/[^\\/\\s\\?&]+?", "http://www.yfrog.com/api/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.yfrog.com/[^\\/\\s\\?&]+?",
        "http://www.yfrog.com/api/oembed",
    ],
    ["http://www.yesik.it/[^\\/\\s\\?&]+?", "http://yesik.it/s/oembed"],
    ["http://yesik.it/[^\\/\\s\\?&]+?", "http://yesik.it/s/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.wizer.me/preview/[^\\/\\s\\?&]+?",
        "http://app.wizer.me/api/oembed.json",
    ],
    [
        "http://[^\\/\\s\\?&]+?.wizer.me/preview/[^\\/\\s\\?&]+?",
        "http://app.wizer.me/api/oembed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.wizer.me/learn/[^\\/\\s\\?&]+?",
        "http://app.wizer.me/api/oembed.json",
    ],
    [
        "http://[^\\/\\s\\?&]+?.wizer.me/learn/[^\\/\\s\\?&]+?",
        "http://app.wizer.me/api/oembed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.wistia.com/medias/[^\\/\\s\\?&]+?",
        "https://fast.wistia.com/oembed.json",
    ],
    [
        "https://fast.wistia.com/embed/playlists/[^\\/\\s\\?&]+?",
        "https://fast.wistia.com/oembed.json",
    ],
    [
        "https://fast.wistia.com/embed/iframe/[^\\/\\s\\?&]+?",
        "https://fast.wistia.com/oembed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.wiredrive.com/[^\\/\\s\\?&]+?",
        "http://*.wiredrive.com/present-oembed/",
    ],
    [
        "https://article.voxsnap.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://data.voxsnap.com/oembed",
    ],
    ["https://vlurb.co/video/[^\\/\\s\\?&]+?", "https://vlurb.co/oembed.json"],
    ["http://vlurb.co/video/[^\\/\\s\\?&]+?", "https://vlurb.co/oembed.json"],
    ["https://www.vlive.tv/video/[^\\/\\s\\?&]+?", "https://www.vlive.tv/oembed"],
    ["https://vlipsy.com/[^\\/\\s\\?&]+?", "https://vlipsy.com/oembed"],
    [
        "http://viziosphere.com/3dphoto[^\\/\\s\\?&]+?",
        "http://viziosphere.com/services/oembed/",
    ],
    [
        "https://player.vimeo.com/video/[^\\/\\s\\?&]+?",
        "https://vimeo.com/api/oembed.json",
    ],
    [
        "https://vimeo.com/ondemand/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://vimeo.com/api/oembed.json",
    ],
    [
        "https://vimeo.com/groups/[^\\/\\s\\?&]+?/videos/[^\\/\\s\\?&]+?",
        "https://vimeo.com/api/oembed.json",
    ],
    [
        "https://vimeo.com/channels/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://vimeo.com/api/oembed.json",
    ],
    [
        "https://vimeo.com/album/[^\\/\\s\\?&]+?/video/[^\\/\\s\\?&]+?",
        "https://vimeo.com/api/oembed.json",
    ],
    ["https://vimeo.com/[^\\/\\s\\?&]+?", "https://vimeo.com/api/oembed.json"],
    [
        "http://[^\\/\\s\\?&]+?.hubs.vidyard.com/[^\\/\\s\\?&]+?",
        "https://api.vidyard.com/dashboard/v1.1/oembed",
    ],
    [
        "http://share.vidyard.com/[^\\/\\s\\?&]+?",
        "https://api.vidyard.com/dashboard/v1.1/oembed",
    ],
    [
        "http://play.vidyard.com/[^\\/\\s\\?&]+?",
        "https://api.vidyard.com/dashboard/v1.1/oembed",
    ],
    [
        "http://embed.vidyard.com/[^\\/\\s\\?&]+?",
        "https://api.vidyard.com/dashboard/v1.1/oembed",
    ],
    [
        "https://players.vidmizer.com/[^\\/\\s\\?&]+?",
        "https://app-v2.vidmizer.com/api/oembed",
    ],
    ["https://vidl.it/[^\\/\\s\\?&]+?", "https://api.vidl.it/oembed"],
    [
        "http://www.videojug.com/interview/[^\\/\\s\\?&]+?",
        "http://www.videojug.com/oembed.json",
    ],
    [
        "http://www.videojug.com/film/[^\\/\\s\\?&]+?",
        "http://www.videojug.com/oembed.json",
    ],
    ["https://www.vevo.com/[^\\/\\s\\?&]+?", "https://www.vevo.com/oembed"],
    ["http://www.vevo.com/[^\\/\\s\\?&]+?", "https://www.vevo.com/oembed"],
    ["http://veervr.tv/videos/[^\\/\\s\\?&]+?", "https://api.veervr.tv/oembed"],
    ["http://veer.tv/videos/[^\\/\\s\\?&]+?", "https://api.veer.tv/oembed"],
    ["http://uttles.com/uttle/[^\\/\\s\\?&]+?", "http://uttles.com/api/reply/oembed"],
    [
        "http://utposts.com/products/[^\\/\\s\\?&]+?",
        "https://www.utposts.com/api/oembed",
    ],
    [
        "https://utposts.com/products/[^\\/\\s\\?&]+?",
        "https://www.utposts.com/api/oembed",
    ],
    [
        "http://www.utposts.com/products/[^\\/\\s\\?&]+?",
        "https://www.utposts.com/api/oembed",
    ],
    [
        "https://www.utposts.com/products/[^\\/\\s\\?&]+?",
        "https://www.utposts.com/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.ustream.com/[^\\/\\s\\?&]+?",
        "http://www.ustream.tv/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.ustream.tv/[^\\/\\s\\?&]+?",
        "http://www.ustream.tv/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.uol.com.br/video/[^\\/\\s\\?&]+?",
        "https://mais.uol.com.br/apiuol/v3/oembed/view",
    ],
    [
        "https://[^\\/\\s\\?&]+?.uol.com.br/view/[^\\/\\s\\?&]+?",
        "https://mais.uol.com.br/apiuol/v3/oembed/view",
    ],
    ["https://map.cam.ac.uk/[^\\/\\s\\?&]+?", "https://map.cam.ac.uk/oembed/"],
    [
        "https://player.ubideo.com/[^\\/\\s\\?&]+?",
        "https://player.ubideo.com/api/oembed.json",
    ],
    ["https://play.typecast.ai/[^\\/\\s\\?&]+?", "https://play.typecast.ai/oembed"],
    ["https://play.typecast.ai/e/[^\\/\\s\\?&]+?", "https://play.typecast.ai/oembed"],
    ["https://play.typecast.ai/s/[^\\/\\s\\?&]+?", "https://play.typecast.ai/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.twitter.com/[^\\/\\s\\?&]+?/status/[^\\/\\s\\?&]+?",
        "https://publish.twitter.com/oembed",
    ],
    [
        "https://twitter.com/[^\\/\\s\\?&]+?/status/[^\\/\\s\\?&]+?",
        "https://publish.twitter.com/oembed",
    ],
    ["https://twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    ["http://twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    ["https://www.twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    ["http://www.twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    ["https://clips.twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    ["http://clips.twitch.tv/[^\\/\\s\\?&]+?", "https://api.twitch.tv/v4/oembed"],
    [
        "http://www.tvcf.co.kr/v/[^\\/\\s\\?&]+?",
        "http://www.tvcf.co.kr/services/oembed",
    ],
    ["https://www.tuxx.be/[^\\/\\s\\?&]+?", "https://www.tuxx.be/services/oembed"],
    ["http://www.topy.se/image/[^\\/\\s\\?&]+?", "http://www.topy.se/oembed/"],
    [
        "https://www.toornament.com/tournaments/[^\\/\\s\\?&]+?/stages/[^\\/\\s\\?&]+?/",
        "https://widget.toornament.com/oembed",
    ],
    [
        "https://www.toornament.com/tournaments/[^\\/\\s\\?&]+?/matches/schedule",
        "https://widget.toornament.com/oembed",
    ],
    [
        "https://www.toornament.com/tournaments/[^\\/\\s\\?&]+?/registration/",
        "https://widget.toornament.com/oembed",
    ],
    [
        "https://www.toornament.com/tournaments/[^\\/\\s\\?&]+?/information",
        "https://widget.toornament.com/oembed",
    ],
    [
        "https://www.tickcounter.com/worldclock/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "https://www.tickcounter.com/ticker/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "https://www.tickcounter.com/countup/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "https://www.tickcounter.com/countdown/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "http://www.tickcounter.com/worldclock/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "http://www.tickcounter.com/ticker/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "http://www.tickcounter.com/countup/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "http://www.tickcounter.com/countdown/[^\\/\\s\\?&]+?",
        "https://www.tickcounter.com/oembed",
    ],
    [
        "https://theysaidso.com/image/[^\\/\\s\\?&]+?",
        "https://theysaidso.com/extensions/oembed/",
    ],
    [
        "https://[^\\/\\s\\?&]+?.nytimes.com/[^\\/\\s\\?&]+?",
        "https://www.nytimes.com/svc/oembed/json/",
    ],
    ["https://nytimes.com/[^\\/\\s\\?&]+?", "https://www.nytimes.com/svc/oembed/json/"],
    ["https://www.nytimes.com/svc/oembed", "https://www.nytimes.com/svc/oembed/json/"],
    [
        "https://www.ted.com/talks/[^\\/\\s\\?&]+?",
        "https://www.ted.com/talks/oembed.json",
    ],
    ["https://ted.com/talks/[^\\/\\s\\?&]+?", "https://www.ted.com/talks/oembed.json"],
    ["http://ted.com/talks/[^\\/\\s\\?&]+?", "https://www.ted.com/talks/oembed.json"],
    ["https://www.sway.com/[^\\/\\s\\?&]+?", "https://sway.com/api/v1.0/oembed"],
    ["https://sway.com/[^\\/\\s\\?&]+?", "https://sway.com/api/v1.0/oembed"],
    [
        "https://www.sutori.com/story/[^\\/\\s\\?&]+?",
        "https://www.sutori.com/api/oembed",
    ],
    [
        "https://content.streamonecloud.net/embed/[^\\/\\s\\?&]+?",
        "https://content.streamonecloud.net/oembed",
    ],
    [
        "https://streamable.com/[^\\/\\s\\?&]+?",
        "https://api.streamable.com/oembed.json",
    ],
    ["http://streamable.com/[^\\/\\s\\?&]+?", "https://api.streamable.com/oembed.json"],
    [
        "https://purl.stanford.edu/[^\\/\\s\\?&]+?",
        "https://purl.stanford.edu/embed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.spreaker.com/[^\\/\\s\\?&]+?",
        "https://api.spreaker.com/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.spreaker.com/[^\\/\\s\\?&]+?",
        "https://api.spreaker.com/oembed",
    ],
    ["spotify:[^\\/\\s\\?&]+?", "https://embed.spotify.com/oembed/"],
    [
        "https://[^\\/\\s\\?&]+?.spotify.com/[^\\/\\s\\?&]+?",
        "https://embed.spotify.com/oembed/",
    ],
    ["http://play.bespotful.com/[^\\/\\s\\?&]+?", "https://api.bespotful.com/oembed"],
    [
        "https://speakerdeck.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://speakerdeck.com/oembed.json",
    ],
    [
        "http://speakerdeck.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://speakerdeck.com/oembed.json",
    ],
    [
        "https://soundsgood.co/playlist/[^\\/\\s\\?&]+?",
        "https://play.soundsgood.co/oembed",
    ],
    [
        "https://play.soundsgood.co/playlist/[^\\/\\s\\?&]+?",
        "https://play.soundsgood.co/oembed",
    ],
    ["https://soundcloud.com/[^\\/\\s\\?&]+?", "https://soundcloud.com/oembed"],
    ["http://soundcloud.com/[^\\/\\s\\?&]+?", "https://soundcloud.com/oembed"],
    ["https://song.link/[^\\/\\s\\?&]+?", "https://song.link/oembed"],
    [
        "https://www.socialexplorer.com/[^\\/\\s\\?&]+?/embed",
        "https://www.socialexplorer.com/services/oembed/",
    ],
    [
        "https://www.socialexplorer.com/[^\\/\\s\\?&]+?/edit",
        "https://www.socialexplorer.com/services/oembed/",
    ],
    [
        "https://www.socialexplorer.com/[^\\/\\s\\?&]+?/view",
        "https://www.socialexplorer.com/services/oembed/",
    ],
    [
        "https://www.socialexplorer.com/[^\\/\\s\\?&]+?/explore",
        "https://www.socialexplorer.com/services/oembed/",
    ],
    [
        "http://[^\\/\\s\\?&]+?.smugmug.com/[^\\/\\s\\?&]+?",
        "http://api.smugmug.com/services/oembed/",
    ],
    [
        "https://smashnotes.com/p/[^\\/\\s\\?&]+?/e/[^\\/\\s\\?&]+? - https://smashnotes.com/p/[^\\/\\s\\?&]+?/e/[^\\/\\s\\?&]+?/s/[^\\/\\s\\?&]+?",
        "https://smashnotes.com/services/oembed",
    ],
    [
        "https://smashnotes.com/p/[^\\/\\s\\?&]+?",
        "https://smashnotes.com/services/oembed",
    ],
    [
        "http://pt.slideshare.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://www.slideshare.net/api/oembed/2",
    ],
    [
        "http://es.slideshare.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://www.slideshare.net/api/oembed/2",
    ],
    [
        "http://de.slideshare.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://www.slideshare.net/api/oembed/2",
    ],
    [
        "http://fr.slideshare.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://www.slideshare.net/api/oembed/2",
    ],
    [
        "http://www.slideshare.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://www.slideshare.net/api/oembed/2",
    ],
    [
        "https://sketchfab.com/[^\\/\\s\\?&]+?/folders/[^\\/\\s\\?&]+?",
        "http://sketchfab.com/oembed",
    ],
    ["https://sketchfab.com/models/[^\\/\\s\\?&]+?", "http://sketchfab.com/oembed"],
    ["http://sketchfab.com/models/[^\\/\\s\\?&]+?", "http://sketchfab.com/oembed"],
    ["https://onsizzle.com/i/[^\\/\\s\\?&]+?", "https://onsizzle.com/oembed"],
    ["https://simplecast.com/s/[^\\/\\s\\?&]+?", "https://simplecast.com/oembed"],
    ["https://showtheway.io/to/[^\\/\\s\\?&]+?", "https://showtheway.io/oembed"],
    ["http://shoud.io/[^\\/\\s\\?&]+?", "http://shoudio.com/api/oembed"],
    ["http://shoudio.com/[^\\/\\s\\?&]+?", "http://shoudio.com/api/oembed"],
    [
        "https://www.shortnote.jp/view/notes/[^\\/\\s\\?&]+?",
        "https://www.shortnote.jp/oembed/",
    ],
    [
        "https://embed.sendtonews.com/oembed/[^\\/\\s\\?&]+?",
        "https://embed.sendtonews.com/services/oembed",
    ],
    [
        "http://www.scribd.com/doc/[^\\/\\s\\?&]+?",
        "http://www.scribd.com/services/oembed/",
    ],
    [
        "https://scribblemaps.com/maps/view/[^\\/\\s\\?&]+?",
        "https://scribblemaps.com/api/services/oembed.json",
    ],
    [
        "http://scribblemaps.com/maps/view/[^\\/\\s\\?&]+?",
        "https://scribblemaps.com/api/services/oembed.json",
    ],
    [
        "https://www.scribblemaps.com/maps/view/[^\\/\\s\\?&]+?",
        "https://scribblemaps.com/api/services/oembed.json",
    ],
    [
        "http://www.scribblemaps.com/maps/view/[^\\/\\s\\?&]+?",
        "https://scribblemaps.com/api/services/oembed.json",
    ],
    [
        "http://www.screenr.com/[^\\/\\s\\?&]+?/",
        "http://www.screenr.com/api/oembed.json",
    ],
    [
        "https://[^\\/\\s\\?&]+?.screen9.tv/[^\\/\\s\\?&]+?",
        "https://api.screen9.com/oembed",
    ],
    ["https://console.screen9.com/[^\\/\\s\\?&]+?", "https://api.screen9.com/oembed"],
    ["http://videos.sapo.pt/[^\\/\\s\\?&]+?", "http://videos.sapo.pt/oembed"],
    ["https://roosterteeth.com/[^\\/\\s\\?&]+?", "https://roosterteeth.com/oembed"],
    [
        "http://roomshare.jp/en/post/[^\\/\\s\\?&]+?",
        "http://roomshare.jp/en/oembed.json",
    ],
    ["http://roomshare.jp/post/[^\\/\\s\\?&]+?", "http://roomshare.jp/en/oembed.json"],
    [
        "https://www.reverbnation.com/[^\\/\\s\\?&]+?/songs/[^\\/\\s\\?&]+?",
        "https://www.reverbnation.com/oembed",
    ],
    [
        "https://www.reverbnation.com/[^\\/\\s\\?&]+?",
        "https://www.reverbnation.com/oembed",
    ],
    [
        "http://repubhub.icopyright.net/freePost.act\\?[^\\/\\s\\?&]+?",
        "http://repubhub.icopyright.net/oembed.act",
    ],
    ["https://repl.it/@[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?", "https://repl.it/data/oembed"],
    ["http://rwire.com/[^\\/\\s\\?&]+?", "http://publisher.releasewire.com/oembed/"],
    [
        "https://www.reddit.com/r/[^\\/\\s\\?&]+?/comments/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://www.reddit.com/oembed",
    ],
    [
        "https://reddit.com/r/[^\\/\\s\\?&]+?/comments/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://www.reddit.com/oembed",
    ],
    ["https://rapidengage.com/s/[^\\/\\s\\?&]+?", "https://rapidengage.com/api/oembed"],
    [
        "http://www.quizz.biz/quizz-[^\\/\\s\\?&]+?.html",
        "http://www.quizz.biz/api/oembed",
    ],
    [
        "http://www.quiz.biz/quizz-[^\\/\\s\\?&]+?.html",
        "http://www.quiz.biz/api/oembed",
    ],
    [
        "https://posixion.com/[^\\/\\s\\?&]+?/question/[^\\/\\s\\?&]+?",
        "http://posixion.com/services/oembed/",
    ],
    [
        "https://posixion.com/question/[^\\/\\s\\?&]+?",
        "http://posixion.com/services/oembed/",
    ],
    [
        "https://portfolium.com/entry/[^\\/\\s\\?&]+?",
        "https://api.portfolium.com/oembed",
    ],
    [
        "https://app.sellwithport.com/#/buyer/[^\\/\\s\\?&]+?",
        "https://api.sellwithport.com/v1.0/buyer/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.polldaddy.com/ratings/[^\\/\\s\\?&]+?",
        "http://polldaddy.com/oembed/",
    ],
    [
        "http://[^\\/\\s\\?&]+?.polldaddy.com/poll/[^\\/\\s\\?&]+?",
        "http://polldaddy.com/oembed/",
    ],
    [
        "http://[^\\/\\s\\?&]+?.polldaddy.com/s/[^\\/\\s\\?&]+?",
        "http://polldaddy.com/oembed/",
    ],
    [
        "http://[^\\/\\s\\?&]+?.podbean.com/e/[^\\/\\s\\?&]+?",
        "https://api.podbean.com/v1/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.podbean.com/e/[^\\/\\s\\?&]+?",
        "https://api.podbean.com/v1/oembed",
    ],
    [
        "https://store.pixdor.com/map/[^\\/\\s\\?&]+?/show",
        "https://store.pixdor.com/oembed",
    ],
    [
        "https://store.pixdor.com/place-marker-widget/[^\\/\\s\\?&]+?/show",
        "https://store.pixdor.com/oembed",
    ],
    ["https://www.pastery.net/[^\\/\\s\\?&]+?", "https://www.pastery.net/oembed"],
    ["http://www.pastery.net/[^\\/\\s\\?&]+?", "https://www.pastery.net/oembed"],
    ["https://pastery.net/[^\\/\\s\\?&]+?", "https://www.pastery.net/oembed"],
    ["http://pastery.net/[^\\/\\s\\?&]+?", "https://www.pastery.net/oembed"],
    [
        "https://overflow.io/embed/[^\\/\\s\\?&]+?",
        "https://overflow.io/services/oembed",
    ],
    ["https://overflow.io/s/[^\\/\\s\\?&]+?", "https://overflow.io/services/oembed"],
    ["https://outplayed.tv/media/[^\\/\\s\\?&]+?", "https://outplayed.tv/oembed"],
    ["https://www.oumy.com/v/[^\\/\\s\\?&]+?", "https://www.oumy.com/oembed"],
    [
        "http://orbitvu.co/001/[^\\/\\s\\?&]+?/1/2/orbittour/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "http://orbitvu.co/001/[^\\/\\s\\?&]+?/2/orbittour/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "http://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3602/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "http://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3601/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "http://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3601/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "https://orbitvu.co/001/[^\\/\\s\\?&]+?/1/2/orbittour/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "https://orbitvu.co/001/[^\\/\\s\\?&]+?/2/orbittour/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "https://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3602/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "https://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3601/[^\\/\\s\\?&]+?/view",
        "http://orbitvu.co/service/oembed",
    ],
    [
        "https://orbitvu.co/001/[^\\/\\s\\?&]+?/ov3601/view",
        "http://orbitvu.co/service/oembed",
    ],
    ["http://on.aol.com/video/[^\\/\\s\\?&]+?", "http://on.aol.com/api"],
    [
        "https://omniscope.me/[^\\/\\s\\?&]+?",
        "https://omniscope.me/_global_/oembed/json",
    ],
    [
        "http://official.fm/playlists/[^\\/\\s\\?&]+?",
        "http://official.fm/services/oembed.json",
    ],
    [
        "http://official.fm/tracks/[^\\/\\s\\?&]+?",
        "http://official.fm/services/oembed.json",
    ],
    ["https://odds.com.au/[^\\/\\s\\?&]+?", "https://www.odds.com.au/api/oembed/"],
    ["https://www.odds.com.au/[^\\/\\s\\?&]+?", "https://www.odds.com.au/api/oembed/"],
    [
        "http://[^\\/\\s\\?&]+?.nfb.ca/film/[^\\/\\s\\?&]+?",
        "http://www.nfb.ca/remote/services/oembed/",
    ],
    [
        "https://naturalatlas.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://naturalatlas.com/oembed.json",
    ],
    [
        "https://naturalatlas.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://naturalatlas.com/oembed.json",
    ],
    [
        "https://naturalatlas.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://naturalatlas.com/oembed.json",
    ],
    [
        "https://naturalatlas.com/[^\\/\\s\\?&]+?",
        "https://naturalatlas.com/oembed.json",
    ],
    ["https://www.nb.no/items/[^\\/\\s\\?&]+?", "https://api.nb.no/catalog/v1/oembed"],
    [
        "https://new.media.zhdk.ch/signatur/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    [
        "https://media.zhdk.ch/signatur/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    [
        "http://new.media.zhdk.ch/signatur/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    [
        "http://media.zhdk.ch/signatur/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    ["https://nanoo.pro/link/[^\\/\\s\\?&]+?", "https://www.nanoo.tv/services/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.nanoo.pro/link/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    ["https://nanoo.tv/link/[^\\/\\s\\?&]+?", "https://www.nanoo.tv/services/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.nanoo.tv/link/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    ["http://nanoo.pro/link/[^\\/\\s\\?&]+?", "https://www.nanoo.tv/services/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.nanoo.pro/link/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    ["http://nanoo.tv/link/[^\\/\\s\\?&]+?", "https://www.nanoo.tv/services/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.nanoo.tv/link/[^\\/\\s\\?&]+?",
        "https://www.nanoo.tv/services/oembed",
    ],
    ["https://namchey.com/embeds/[^\\/\\s\\?&]+?", "https://namchey.com/api/oembed"],
    ["https://mybeweeg.com/w/[^\\/\\s\\?&]+?", "https://mybeweeg.com/services/oembed"],
    [
        "https://musicboxmaniacs.com/explore/melody/[^\\/\\s\\?&]+?",
        "https://musicboxmaniacs.com/embed/",
    ],
    [
        "https://m-roll.morphcast.com/mroll/[^\\/\\s\\?&]+?",
        "https://m-roll.morphcast.com/service/oembed",
    ],
    [
        "https://beta.modelo.io/embedded/[^\\/\\s\\?&]+?",
        "https://portal.modelo.io/oembed",
    ],
    ["http://moby.to/[^\\/\\s\\?&]+?", "http://api.mobypicture.com/oEmbed"],
    [
        "http://www.mobypicture.com/user/[^\\/\\s\\?&]+?/view/[^\\/\\s\\?&]+?",
        "http://api.mobypicture.com/oEmbed",
    ],
    [
        "https://www.mixcloud.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/",
        "https://www.mixcloud.com/oembed/",
    ],
    [
        "http://www.mixcloud.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/",
        "https://www.mixcloud.com/oembed/",
    ],
    ["http://meetu.ps/[^\\/\\s\\?&]+?", "https://api.meetup.com/oembed"],
    ["https://meetup.com/[^\\/\\s\\?&]+?", "https://api.meetup.com/oembed"],
    ["https://www.meetup.com/[^\\/\\s\\?&]+?", "https://api.meetup.com/oembed"],
    ["http://meetup.com/[^\\/\\s\\?&]+?", "https://api.meetup.com/oembed"],
    [
        "https://medienarchiv.zhdk.ch/entries/[^\\/\\s\\?&]+?",
        "https://medienarchiv.zhdk.ch/oembed.json",
    ],
    ["https://me.me/i/[^\\/\\s\\?&]+?", "https://me.me/oembed"],
    [
        "http://mathembed.com/latex\\?inputText=[^\\/\\s\\?&]+?",
        "http://mathembed.com/oembed",
    ],
    ["https://app.ludus.one/[^\\/\\s\\?&]+?", "https://app.ludus.one/oembed"],
    [
        "https://livestream.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/videos/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://livestream.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://livestream.com/[^\\/\\s\\?&]+?/events/[^\\/\\s\\?&]+?/videos/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://livestream.com/[^\\/\\s\\?&]+?/events/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://livestream.com/accounts/[^\\/\\s\\?&]+?/events/[^\\/\\s\\?&]+?/videos/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://livestream.com/accounts/[^\\/\\s\\?&]+?/events/[^\\/\\s\\?&]+?",
        "https://livestream.com/oembed",
    ],
    [
        "https://pod.univ-lille.fr/video/[^\\/\\s\\?&]+?",
        "https://pod.univ-lille.fr/oembed",
    ],
    ["http://learningapps.org/[^\\/\\s\\?&]+?", "http://learningapps.org/oembed.php"],
    ["https://jdr.knacki.info/meuh/[^\\/\\s\\?&]+?", "https://jdr.knacki.info/oembed"],
    ["http://jdr.knacki.info/meuh/[^\\/\\s\\?&]+?", "https://jdr.knacki.info/oembed"],
    [
        "http://www.kitchenbowl.com/recipe/[^\\/\\s\\?&]+?",
        "http://www.kitchenbowl.com/oembed",
    ],
    ["https://kit.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?", "https://embed.kit.com/oembed"],
    ["http://kit.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?", "https://embed.kit.com/oembed"],
    [
        "https://www.kidoju.com/fr/x/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://www.kidoju.com/api/oembed",
    ],
    [
        "https://www.kidoju.com/en/x/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://www.kidoju.com/api/oembed",
    ],
    [
        "http://www.kickstarter.com/projects/[^\\/\\s\\?&]+?",
        "http://www.kickstarter.com/services/oembed",
    ],
    ["https://tv.kakao.com/channel/l/[^\\/\\s\\?&]+?", "https://tv.kakao.com/oembed"],
    [
        "https://tv.kakao.com/channel/[^\\/\\s\\?&]+?/livelink/[^\\/\\s\\?&]+?",
        "https://tv.kakao.com/oembed",
    ],
    ["https://tv.kakao.com/channel/v/[^\\/\\s\\?&]+?", "https://tv.kakao.com/oembed"],
    [
        "https://tv.kakao.com/channel/[^\\/\\s\\?&]+?/cliplink/[^\\/\\s\\?&]+?",
        "https://tv.kakao.com/oembed",
    ],
    [
        "https://issuu.com/[^\\/\\s\\?&]+?/docs/[^\\/\\s\\?&]+?",
        "https://issuu.com/oembed",
    ],
    ["https://www.isnare.com/[^\\/\\s\\?&]+?", "https://www.isnare.com/oembed/"],
    ["https://www.instagr.am/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["https://www.instagram.com/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["https://instagr.am/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["https://instagram.com/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["http://www.instagr.am/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["http://www.instagram.com/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["http://instagr.am/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    ["http://instagram.com/p/[^\\/\\s\\?&]+?", "https://api.instagram.com/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.inphood.com/[^\\/\\s\\?&]+?",
        "http://api.inphood.com/oembed",
    ],
    ["https://www.inoreader.com/oembed/", "https://www.inoreader.com/oembed/api/"],
    [
        "https://www.injurymap.com/exercises/[^\\/\\s\\?&]+?",
        "https://www.injurymap.com/services/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.infoveave.net/P/[^\\/\\s\\?&]+?",
        "https://infoveave.net/services/oembed/",
    ],
    [
        "https://[^\\/\\s\\?&]+?.infoveave.net/E/[^\\/\\s\\?&]+?",
        "https://infoveave.net/services/oembed/",
    ],
    ["https://infogr.am/[^\\/\\s\\?&]+?", "https://infogr.am/oembed"],
    [
        "https://player.indacolive.com/player/jwp/clients/[^\\/\\s\\?&]+?",
        "https://player.indacolive.com/services/oembed",
    ],
    ["http://ifttt.com/recipes/[^\\/\\s\\?&]+?", "http://www.ifttt.com/oembed/"],
    ["http://www.ifixit.com/Guide/View/[^\\/\\s\\?&]+?", "http://www.ifixit.com/Embed"],
    [
        "http://www.hulu.com/watch/[^\\/\\s\\?&]+?",
        "http://www.hulu.com/api/oembed.json",
    ],
    [
        "http://huffduffer.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://huffduffer.com/oembed",
    ],
    [
        "https://hearthis.at/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/",
        "https://hearthis.at/oembed/",
    ],
    ["https://gyazo.com/[^\\/\\s\\?&]+?", "https://api.gyazo.com/api/oembed"],
    ["https://gtchannel.com/watch/[^\\/\\s\\?&]+?", "https://api.luminery.com/oembed"],
    [
        "https://media.giphy.com/media/[^\\/\\s\\?&]+?/giphy.gif",
        "https://giphy.com/services/oembed",
    ],
    ["http://gph.is/[^\\/\\s\\?&]+?", "https://giphy.com/services/oembed"],
    ["https://giphy.com/gifs/[^\\/\\s\\?&]+?", "https://giphy.com/services/oembed"],
    [
        "https://www.gifnote.com/play/[^\\/\\s\\?&]+?",
        "https://www.gifnote.com/services/oembed",
    ],
    ["https://www.gfycat.com/[^\\/\\s\\?&]+?", "https://api.gfycat.com/v1/oembed"],
    ["https://gfycat.com/[^\\/\\s\\?&]+?", "https://api.gfycat.com/v1/oembed"],
    ["http://www.gfycat.com/[^\\/\\s\\?&]+?", "https://api.gfycat.com/v1/oembed"],
    ["http://gfycat.com/[^\\/\\s\\?&]+?", "https://api.gfycat.com/v1/oembed"],
    ["http://gty.im/[^\\/\\s\\?&]+?", "http://embed.gettyimages.com/oembed"],
    [
        "http://germany.geograph.org/[^\\/\\s\\?&]+?",
        "http://geo.hlipp.de/restapi.php/api/oembed",
    ],
    [
        "http://geo.hlipp.de/[^\\/\\s\\?&]+?",
        "http://geo.hlipp.de/restapi.php/api/oembed",
    ],
    [
        "http://geo-en.hlipp.de/[^\\/\\s\\?&]+?",
        "http://geo.hlipp.de/restapi.php/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.channel.geographs.org/[^\\/\\s\\?&]+?",
        "http://www.geograph.org.gg/api/oembed",
    ],
    [
        "http://channel-islands.geographs.org/[^\\/\\s\\?&]+?",
        "http://www.geograph.org.gg/api/oembed",
    ],
    [
        "http://channel-islands.geograph.org/[^\\/\\s\\?&]+?",
        "http://www.geograph.org.gg/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.geograph.org.je/[^\\/\\s\\?&]+?",
        "http://www.geograph.org.gg/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.geograph.org.gg/[^\\/\\s\\?&]+?",
        "http://www.geograph.org.gg/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.wikimedia.org/[^\\/\\s\\?&]+?_geograph.org.uk_[^\\/\\s\\?&]+?",
        "http://api.geograph.org.uk/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.geograph.ie/[^\\/\\s\\?&]+?",
        "http://api.geograph.org.uk/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.geograph.co.uk/[^\\/\\s\\?&]+?",
        "http://api.geograph.org.uk/api/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.geograph.org.uk/[^\\/\\s\\?&]+?",
        "http://api.geograph.org.uk/api/oembed",
    ],
    [
        "http://www.funnyordie.com/videos/[^\\/\\s\\?&]+?",
        "http://www.funnyordie.com/oembed.json",
    ],
    ["https://framebuzz.com/v/[^\\/\\s\\?&]+?", "https://framebuzz.com/oembed/"],
    ["http://framebuzz.com/v/[^\\/\\s\\?&]+?", "https://framebuzz.com/oembed/"],
    [
        "https://fiso.foxsports.com.au/isomorphic-widget/[^\\/\\s\\?&]+?",
        "https://fiso.foxsports.com.au/oembed",
    ],
    [
        "http://fiso.foxsports.com.au/isomorphic-widget/[^\\/\\s\\?&]+?",
        "https://fiso.foxsports.com.au/oembed",
    ],
    ["https://catapult.fontself.com/[^\\/\\s\\?&]+?", "https://oembed.fontself.com/"],
    [
        "https://public.flourish.studio/story/[^\\/\\s\\?&]+?",
        "https://app.flourish.studio/api/v1/oembed",
    ],
    [
        "https://public.flourish.studio/visualisation/[^\\/\\s\\?&]+?",
        "https://app.flourish.studio/api/v1/oembed",
    ],
    ["https://flic.kr/p/[^\\/\\s\\?&]+?", "https://www.flickr.com/services/oembed/"],
    [
        "https://[^\\/\\s\\?&]+?.flickr.com/photos/[^\\/\\s\\?&]+?",
        "https://www.flickr.com/services/oembed/",
    ],
    ["http://flic.kr/p/[^\\/\\s\\?&]+?", "https://www.flickr.com/services/oembed/"],
    [
        "http://[^\\/\\s\\?&]+?.flickr.com/photos/[^\\/\\s\\?&]+?",
        "https://www.flickr.com/services/oembed/",
    ],
    [
        "https://[^\\/\\s\\?&]+?.flat.io/score/[^\\/\\s\\?&]+?",
        "https://flat.io/services/oembed",
    ],
    ["https://flat.io/score/[^\\/\\s\\?&]+?", "https://flat.io/services/oembed"],
    ["https://www.fite.tv/watch/[^\\/\\s\\?&]+?", "https://www.fite.tv/oembed"],
    [
        "https://faithlifetv.com/media/resource/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://faithlifetv.com/api/oembed",
    ],
    [
        "https://faithlifetv.com/media/assets/[^\\/\\s\\?&]+?",
        "https://faithlifetv.com/api/oembed",
    ],
    [
        "https://faithlifetv.com/media/[^\\/\\s\\?&]+?",
        "https://faithlifetv.com/api/oembed",
    ],
    [
        "https://faithlifetv.com/items/resource/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://faithlifetv.com/api/oembed",
    ],
    [
        "https://faithlifetv.com/items/[^\\/\\s\\?&]+?",
        "https://faithlifetv.com/api/oembed",
    ],
    [
        "https://app.getfader.com/projects/[^\\/\\s\\?&]+?/publish",
        "https://app.getfader.com/api/oembed",
    ],
    [
        "https://www.facebook.com/video.php",
        "https://www.facebook.com/plugins/video/oembed.json",
    ],
    [
        "https://www.facebook.com/[^\\/\\s\\?&]+?/videos/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/video/oembed.json",
    ],
    [
        "https://www.facebook.com/notes/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/questions/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/media/set\\?set=[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/permalink.php",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/[^\\/\\s\\?&]+?/activity/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/photo.php",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/photo.php[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/[^\\/\\s\\?&]+?/photos/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/photos/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    [
        "https://www.facebook.com/[^\\/\\s\\?&]+?/posts/[^\\/\\s\\?&]+?",
        "https://www.facebook.com/plugins/post/oembed.json",
    ],
    ["https://eyrie.io/sparkfun/[^\\/\\s\\?&]+?", "https://eyrie.io/v1/oembed"],
    ["https://eyrie.io/board/[^\\/\\s\\?&]+?", "https://eyrie.io/v1/oembed"],
    ["https://ethfiddle.com/[^\\/\\s\\?&]+?", "https://ethfiddle.com/services/oembed/"],
    ["http://embedarticles.com/[^\\/\\s\\?&]+?", "http://embedarticles.com/oembed/"],
    [
        "http://egliseinfo.catholique.fr/[^\\/\\s\\?&]+?",
        "http://egliseinfo.catholique.fr/api/oembed",
    ],
    ["http://edocr.com/docs/[^\\/\\s\\?&]+?", "http://edocr.com/api/oembed"],
    ["https://d.tube/v/[^\\/\\s\\?&]+?", "https://api.d.tube/oembed"],
    ["http://dotsub.com/view/[^\\/\\s\\?&]+?", "http://dotsub.com/services/oembed"],
    ["http://docdro.id/[^\\/\\s\\?&]+?", "https://www.docdroid.net/api/oembed"],
    ["https://docdro.id/[^\\/\\s\\?&]+?", "https://www.docdroid.net/api/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.docdroid.net/[^\\/\\s\\?&]+?",
        "https://www.docdroid.net/api/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.docdroid.net/[^\\/\\s\\?&]+?",
        "https://www.docdroid.net/api/oembed",
    ],
    [
        "http://www.dipity.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/",
        "http://www.dipity.com/oembed/timeline/",
    ],
    [
        "https://www.ultimedia.com/default/index/videogeneric/id/[^\\/\\s\\?&]+?",
        "https://www.ultimedia.com/api/search/oembed",
    ],
    [
        "https://www.ultimedia.com/default/index/videogeneric/id/[^\\/\\s\\?&]+?/showtitle/1/viewnc/1",
        "https://www.ultimedia.com/api/search/oembed",
    ],
    [
        "https://www.ultimedia.com/central/video/edit/id/[^\\/\\s\\?&]+?/topic_id/[^\\/\\s\\?&]+?/",
        "https://www.ultimedia.com/api/search/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.didacte.com/a/course/[^\\/\\s\\?&]+?",
        "https://*.didacte.com/cards/oembed'",
    ],
    [
        'https://[^\\/\\s\\?&]+?.deviantart.com/[^\\/\\s\\?&]+?#/d[^\\/\\s\\?&]+?"',
        "http://backend.deviantart.com/oembed",
    ],
    ['https://sta.sh/[^\\/\\s\\?&]+?",', "http://backend.deviantart.com/oembed"],
    [
        "https://[^\\/\\s\\?&]+?.deviantart.com/[^\\/\\s\\?&]+?/art/[^\\/\\s\\?&]+?",
        "http://backend.deviantart.com/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.deviantart.com/art/[^\\/\\s\\?&]+?",
        "http://backend.deviantart.com/oembed",
    ],
    ["http://sta.sh/[^\\/\\s\\?&]+?", "http://backend.deviantart.com/oembed"],
    ["http://fav.me/[^\\/\\s\\?&]+?", "http://backend.deviantart.com/oembed"],
    [
        "http://[^\\/\\s\\?&]+?.deviantart.com/[^\\/\\s\\?&]+?#/d[^\\/\\s\\?&]+?",
        "http://backend.deviantart.com/oembed",
    ],
    [
        "http://[^\\/\\s\\?&]+?.deviantart.com/art/[^\\/\\s\\?&]+?",
        "http://backend.deviantart.com/oembed",
    ],
    [
        "https://[^\\/\\s\\?&]+?.deseretnews.com/[^\\/\\s\\?&]+?",
        "https://embed.deseretnews.com/",
    ],
    [
        "https://www.dailymotion.com/video/[^\\/\\s\\?&]+?",
        "https://www.dailymotion.com/services/oembed",
    ],
    [
        "http://www.dailymile.com/people/[^\\/\\s\\?&]+?/entries/[^\\/\\s\\?&]+?",
        "http://api.dailymile.com/oembed?format=json",
    ],
    [
        "https://app.cyranosystems.com/msg/[^\\/\\s\\?&]+?",
        "https://staging.cyranosystems.com/oembed",
    ],
    [
        "https://staging.cyranosystems.com/msg/[^\\/\\s\\?&]+?",
        "https://staging.cyranosystems.com/oembed",
    ],
    [
        "http://crowdranking.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "http://crowdranking.com/api/oembed.json",
    ],
    ["http://coub.com/embed/[^\\/\\s\\?&]+?", "http://coub.com/api/oembed.json"],
    ["http://coub.com/view/[^\\/\\s\\?&]+?", "http://coub.com/api/oembed.json"],
    ["https://commaful.com/play/[^\\/\\s\\?&]+?", "https://commaful.com/api/oembed/"],
    [
        "http://www.collegehumor.com/video/[^\\/\\s\\?&]+?",
        "http://www.collegehumor.com/oembed.json",
    ],
    ["https://codesandbox.io/embed/[^\\/\\s\\?&]+?", "https://codesandbox.io/oembed"],
    ["https://codesandbox.io/s/[^\\/\\s\\?&]+?", "https://codesandbox.io/oembed"],
    [
        "https://www.codepoints.net/[^\\/\\s\\?&]+?",
        "https://codepoints.net/api/v1/oembed",
    ],
    [
        "http://www.codepoints.net/[^\\/\\s\\?&]+?",
        "https://codepoints.net/api/v1/oembed",
    ],
    ["https://codepoints.net/[^\\/\\s\\?&]+?", "https://codepoints.net/api/v1/oembed"],
    ["http://codepoints.net/[^\\/\\s\\?&]+?", "https://codepoints.net/api/v1/oembed"],
    ["https://codepen.io/[^\\/\\s\\?&]+?", "http://codepen.io/api/oembed"],
    ["http://codepen.io/[^\\/\\s\\?&]+?", "http://codepen.io/api/oembed"],
    [
        "https://codehs.com/editor/share_abacus/[^\\/\\s\\?&]+?",
        "https://codehs.com/api/sharedprogram/*/oembed/",
    ],
    ["http://clyp.it/playlist/[^\\/\\s\\?&]+?", "http://api.clyp.it/oembed/"],
    ["http://clyp.it/[^\\/\\s\\?&]+?", "http://api.clyp.it/oembed/"],
    [
        "https://www.clipland.com/v/[^\\/\\s\\?&]+?",
        "https://www.clipland.com/api/oembed",
    ],
    [
        "http://www.clipland.com/v/[^\\/\\s\\?&]+?",
        "https://www.clipland.com/api/oembed",
    ],
    [
        "https://www.circuitlab.com/circuit/[^\\/\\s\\?&]+?",
        "https://www.circuitlab.com/circuit/oembed/",
    ],
    ["http://chirb.it/[^\\/\\s\\?&]+?", "http://chirb.it/oembed.json"],
    [
        "http://public.chartblocks.com/c/[^\\/\\s\\?&]+?",
        "http://embed.chartblocks.com/1.0/oembed",
    ],
    ["http://view.ceros.com/[^\\/\\s\\?&]+?", "http://view.ceros.com/oembed"],
    ["http://img.catbo.at/[^\\/\\s\\?&]+?", "http://img.catbo.at/oembed.json"],
    [
        "https://carbonhealth.com/practice/[^\\/\\s\\?&]+?",
        "http://carbonhealth.com/oembed",
    ],
    ["https://cacoo.com/diagrams/[^\\/\\s\\?&]+?", "http://cacoo.com/oembed.json"],
    ["https://cmc.byzart.eu/files/[^\\/\\s\\?&]+?", "https://cmc.byzart.eu/oembed/"],
    ["https://buttondown.email/[^\\/\\s\\?&]+?", "https://buttondown.email/embed"],
    [
        "https://view.briovr.com/api/v1/worlds/oembed/[^\\/\\s\\?&]+?",
        "https://view.briovr.com/api/v1/worlds/oembed/",
    ],
    [
        "https://blackfire.io/profiles/compare/[^\\/\\s\\?&]+?/graph",
        "https://blackfire.io/oembed",
    ],
    [
        "https://blackfire.io/profiles/[^\\/\\s\\?&]+?/graph",
        "https://blackfire.io/oembed",
    ],
    ["http://backtracks.fm/[^\\/\\s\\?&]+?", "https://backtracks.fm/oembed"],
    ["https://backtracks.fm/[^\\/\\s\\?&]+?", "https://backtracks.fm/oembed"],
    [
        "https://backtracks.fm/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?/e/[^\\/\\s\\?&]+?",
        "https://backtracks.fm/oembed",
    ],
    ["http://audiosnaps.com/k/[^\\/\\s\\?&]+?", "http://audiosnaps.com/service/oembed"],
    [
        "https://www.audiomack.com/playlist/[^\\/\\s\\?&]+?",
        "https://www.audiomack.com/oembed",
    ],
    [
        "https://www.audiomack.com/album/[^\\/\\s\\?&]+?",
        "https://www.audiomack.com/oembed",
    ],
    [
        "https://www.audiomack.com/song/[^\\/\\s\\?&]+?",
        "https://www.audiomack.com/oembed",
    ],
    [
        "https://audioclip.naver.com/audiobooks/[^\\/\\s\\?&]+?",
        "https://audioclip.naver.com/oembed",
    ],
    [
        "https://audioclip.naver.com/channels/[^\\/\\s\\?&]+?/clips/[^\\/\\s\\?&]+?",
        "https://audioclip.naver.com/oembed",
    ],
    [
        "https://app.archivos.digital/app/view/[^\\/\\s\\?&]+?",
        "https://app.archivos.digital/oembed/",
    ],
    [
        "https://renderer.apester.com/v2/[^\\/\\s\\?&]+?\\?preview=true&iframe_preview=true",
        "https://display.apester.com/oembed",
    ],
    ["http://animoto.com/play/[^\\/\\s\\?&]+?", "http://animoto.com/oembeds/create"],
    [
        "https://animatron.com/project/[^\\/\\s\\?&]+?",
        "https://animatron.com/oembed/json",
    ],
    [
        "https://www.animatron.com/project/[^\\/\\s\\?&]+?",
        "https://animatron.com/oembed/json",
    ],
    ["https://live.amcharts.com/[^\\/\\s\\?&]+?", "https://live.amcharts.com/oembed"],
    ["http://live.amcharts.com/[^\\/\\s\\?&]+?", "https://live.amcharts.com/oembed"],
    [
        "https://app.altrulabs.com/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?\\?answer_id=[^\\/\\s\\?&]+?",
        "https://api.altrulabs.com/social/oembed",
    ],
    [
        "https://photos.app.net/[^\\/\\s\\?&]+?/[^\\/\\s\\?&]+?",
        "https://alpha-api.app.net/oembed",
    ],
    [
        "https://alpha.app.net/[^\\/\\s\\?&]+?/post/[^\\/\\s\\?&]+?",
        "https://alpha-api.app.net/oembed",
    ],
    [
        "http://play.adpaths.com/experience/[^\\/\\s\\?&]+?",
        "http://play.adpaths.com/oembed/*",
    ],
    [
        "http://www.23hq.com/[^\\/\\s\\?&]+?/photo/[^\\/\\s\\?&]+?",
        "http://www.23hq.com/23/oembed",
    ],
]
