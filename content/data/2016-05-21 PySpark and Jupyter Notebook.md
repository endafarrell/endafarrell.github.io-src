Title: PySpark and Jupyter Notebook
Date: 2016-05-21 11:11
Modified: 2016-07-02 18:00
Tags: pyspark, jupyter, ipython, notebook, how-to, conda

There's a _lot_ of crap advice about getting jupyter notebooks to play nicely with pyspark. I guess things have changed
a lot over the last couple of years, but here's how I have things.

I use [conda](http://conda.pydata.org/docs/) for my python envs, but I _doubt_ that matters here.
 
```bash
SPARK_HOME=/workspace/pyspark-games/spark-1.5.0-bin-hadoop2.4 \
PATH=$SPARK_HOME/bin:$PATH \
PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip:$PYTHONPATH \
IPYTHON_OPTS="notebook" \
$SPARK_HOME/bin/pyspark
```

With this approach I don't need/want to play with Jupyter profiles and, it may (now) be unsupported with Jupyter. This 
way allows me to have pyspark running when I want it and not when I don't.

You'll need to set your own ```SPARK_HOME``` and check your ```py4j-0.8.2.1-src.zip``` versions ;-)


It'd like to shout out to 
[http://npatta01.github.io/2015/08/01/pyspark_jupyter/](http://npatta01.github.io/2015/08/01/pyspark_jupyter/) for the 
how-to.
