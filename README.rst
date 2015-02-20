==================
BlockTorMiddleware
==================

BlockTorMiddleware is a middleware to automatically block users from Tor network.
If user enter from Tor network, 404 page will be returned. If you need

I urge you to not use this middleware unless you have too. I wrote this middleware due to
 a lot of spamming from Tor network on my website.

Quick start
-----------


1. Install the missing requirement::

    pip install -r requirements.txt

2. Add "BlockTorMiddleware" to your MIDDLEWARE_CLASSES setting like this::

    MIDDLEWARE_CLASSES = (
        ...
        'django-block-tor.blocktor.BlockTorMiddleware'
    )


3. That's it ;)