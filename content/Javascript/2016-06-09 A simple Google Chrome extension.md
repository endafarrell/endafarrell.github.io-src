Title: A Simple Chrome extension
Date: 2016-06-09 21:40
Category: Javascript
Tags: "Google Chrome extension", javascript, HTML, Facebook

I had an itch to be able to easily find the Facebook ID for Place pages that I was visiting. You can - usually - find 
the ID that the Facebook Graph API uses for a Place page by looking into the HTML source of the Facebook Place page and 
recognising some patterns. It was a slow business, so I wrote this instead.

Due to my not really knowing how to set things up properly, the installation says that:

> _It can:_
>
>    * Read and change all your data on all facebook.com site
>    * Read your browsing history
>

And I guess it _could_, based on the permissions that I didn't properly set up, but version 1.0.4 doesn't. Except "Read 
... data on ... facebook.com." of course. It does not need to read your browsing history, and it doesn't re-write nor 
edit nor modify nor hide nor touch the Facebook HTML at all. And it most certainly does not in any way "change all your 
data" on Facebook. I'll see about fixing these in a later version.

So: if ever getting the ID of a Facebook Place was something you wanted to do, then 
<a href="https://chrome.google.com/webstore/detail/get-facebook-id/fakbnhhfckloijmnbpdanjeniajgjgcn?hl=en" 
   target="_blank" title="Get Facebook ID in the Chrome Store">Get Facebook ID</a> might be useful..