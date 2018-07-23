title: Runtime disabling of TestNG groups
date: 2010-06-03
tags: code, java, testng

We have recently started to use TestNG and I like it. One thing that is needed is runtime control over whether or not to 
run a group of tests.

We have both unit tests and integration tests to assure ourselves of the system’s health. Running the integration tests 
requires running databases (CouchDB in this case) but we don’t - by policy - have databases running on the continuous 
integration Hudson server. There are of course other approaches to dealing with this, but we have found this works well 
for us.

Oh - and we need to have just one POM. So no

    <disabledGroups>system</disabledGroups>

for us.
We only want the “integration” group of tests to run when the local environment variable “SERVER_ENV” has the value of 
dev. The following code causes these to be skipped (at least as of 5.12.1):

    @BeforeGroups(groups = {"integration"})
    public void checkEnvIsDev() throws Exception {
        boolean isDev = ("dev".equals(System.getenv("SERVER_ENV")));
        if (!isDev) throw new SkipException("Skip the \"integration\" group as $SERVER_ENV is not \"dev\".");
    }
This may be a new feature, but it seems that as the SkipException is thrown, the entire group is skipped.

Nice.
