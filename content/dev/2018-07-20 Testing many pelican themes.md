Title: Testing many pelican themes
Date: 2018-07-20
Tags: Python, Pelican

![calendar image]({filename}/images/2018/testing-many-pelican-themes.png){:style="float: left; margin-right: 7px;"} I've been looking at how Pelican works, and was working with many different themes,
and of course, after a while, it became annoying to have to make repeated calls to
see what the content looks like in different themes. So I put this together:

```bash
for theme in $(
    find themes/pelican-themes \
        -type d \
        -not -empty \
        -depth 1 \
    | grep -v ".git/" \
    | cut -f3 -d/ \
    | sort
)
do 
    printf "${theme}: "
    pelican content \
        -o output/${theme} \
        -s pelicanconf.py \
        -t themes/pelican-themes/${theme}
done 2>&1 | tee log
```