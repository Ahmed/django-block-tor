==================
BlockTorMiddleware
==================

BlockTorMiddleware is a middleware to automatically block users from Tor network.
If user enter from Tor network, 404 page will be returned. I urge you to not use this middleware unless you have too.
I wrote this middleware due to lot of spamming from Tor network on my website.

Quick start
-----------

1. Go to the root of your django project and download this package::

    git clone git@github.com:Ahmed/django-block-tor.git


2. Install the missing requirement::

    pip install -r requirements.txt

3. Add "BlockTorMiddleware" *at the end of* MIDDLEWARE_CLASSES setting like this::

    MIDDLEWARE_CLASSES = (
        ...
        'django-block-tor.blocktor.BlockTorMiddleware'
    )


4. That's it ;)