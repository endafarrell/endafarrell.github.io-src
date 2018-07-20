Title: Parsing dates in Java
Date: 2018-03-04
Category: Java
Tags: java, how-to, code

![calendar image]({filename}/images/calendar_date_parsing.jpg){:style="float: left; margin-right: 7px;"} Clearly, the ``correct`` way to deal with dates in Java is with Joda, but I've been looking at a project which
doesn't have Joda installed already, and I haven't earned the right to rearrange that project's dependencies and
build patterns. It's also a project that needs to run on lower-specced machines (I'm used to writing server code,
but this is destined for things like watches), so there are likely to be reasons I don't understand why external
modules will not be welcome.

Here's my current thinking:

```java

import javafx.util.Pair;  // <<<- this woould be replaced with the Pair in the Android SDK

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;


public class DateUtils {
    private final static Locale EN = Locale.ENGLISH;
    private final static TimeZone UTC = TimeZone.getTimeZone("UTC");

    private final static SimpleDateFormat hms_tz = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssZ");
    private final static SimpleDateFormat hm_tz = new SimpleDateFormat("yyyy-MM-dd'T'HH:mmZ");
    private final static SimpleDateFormat hms_X = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssX");
    private final static SimpleDateFormat hm_X = new SimpleDateFormat("yyyy-MM-dd'T'HH:mmX");
    private final static SimpleDateFormat no_T_hms_X = new SimpleDateFormat("yyyy-MM-dd HH:mm:ssX");
    private final static SimpleDateFormat no_T_hms_no_tz = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    private static final List<SimpleDateFormat> formats =
            Collections.unmodifiableList(Arrays.asList(
                    hms_X, hm_X, hms_tz, hm_tz,
                    no_T_hms_X, no_T_hms_no_tz));


    public static void main(String[] args) {
        // Having parsed strings, we'll want to print them out in a very specific format later
        SimpleDateFormat dateUTC = new SimpleDateFormat("yyyy-MM-dd HH:mm:ssZ", EN);
        dateUTC.setTimeZone(UTC);

        Date parsed;
        String parsedPrinted;
        boolean formatFound = false;
        List<Pair<String, Integer>> dateStrings = Arrays.asList(
                new Pair<>("2018-03-03T11:38:54+01:00", 10),
                new Pair<>("2018-03-03T11:38:54Z", 11),
                new Pair<>("2018-03-03T11:38 UTC", 11),
                new Pair<>("2018-03-03 11:38:54", 10)); // only true as my Timezone is UTC+1 right now.
        for (Pair<String, Integer> dateStringUTCHour : dateStrings) {
            System.out.println(String.format(
                    "\"%s\" is (with expected UTC hour %d):",
                    dateStringUTCHour.getKey(),
                    dateStringUTCHour.getValue()));

            formatFound = false;
            // Note: Your IDE will say "for loop replaceable with foreach" - don't do it!
            // Note: The SimpleDateFormat is not thread-safe, and so we need to synchronise on it, but not on the local
            // Note: variable that a foreach loop would give. Hence `noinspection ForLoopReplaceableByForEach`
            //noinspection ForLoopReplaceableByForEach
            for (int f = 0; f < formats.size(); f++) {
                try {
                    synchronized (formats.get(f)) {
                        parsed = formats.get(f).parse(dateStringUTCHour.getKey());
                    }
                    parsedPrinted = dateUTC.format(parsed);

                    System.out.println(String.format(
                            "* in format \"%s\" and is %s",
                            formats.get(f).toPattern(), parsedPrinted));
                    formatFound = true;
                } catch (ParseException e) {
                    System.out.println(String.format(
                            "* not in format \"%s\"",
                            formats.get(f).toPattern()));
                    System.out.flush();
                }
            }
            if (!formatFound) {
                System.err.println(String.format("\"%s\" has an unhandled format", dateStringUTCHour.getKey()));
            }
            System.out.println();
        }
    }
}
```

running it gives:

```
"2018-03-03T11:38:54+01:00" is (with expected UTC hour 10):
* in format "yyyy-MM-dd'T'HH:mm:ssX" and is 2018-03-03 10:38:54+0000
* not in format "yyyy-MM-dd'T'HH:mmX"
* not in format "yyyy-MM-dd'T'HH:mm:ssZ"
* not in format "yyyy-MM-dd'T'HH:mmZ"
* not in format "yyyy-MM-dd HH:mm:ssX"
* not in format "yyyy-MM-dd HH:mm:ss"

"2018-03-03T11:38:54Z" is (with expected UTC hour 11):
* in format "yyyy-MM-dd'T'HH:mm:ssX" and is 2018-03-03 11:38:54+0000
* not in format "yyyy-MM-dd'T'HH:mmX"
* not in format "yyyy-MM-dd'T'HH:mm:ssZ"
* not in format "yyyy-MM-dd'T'HH:mmZ"
* not in format "yyyy-MM-dd HH:mm:ssX"
* not in format "yyyy-MM-dd HH:mm:ss"

"2018-03-03T11:38 UTC" is (with expected UTC hour 11):
* not in format "yyyy-MM-dd'T'HH:mm:ssX"
* not in format "yyyy-MM-dd'T'HH:mmX"
* not in format "yyyy-MM-dd'T'HH:mm:ssZ"
* in format "yyyy-MM-dd'T'HH:mmZ" and is 2018-03-03 11:38:00+0000
* not in format "yyyy-MM-dd HH:mm:ssX"
* not in format "yyyy-MM-dd HH:mm:ss"

"2018-03-03 11:38:54" is (with expected UTC hour 10):
* not in format "yyyy-MM-dd'T'HH:mm:ssX"
* not in format "yyyy-MM-dd'T'HH:mmX"
* not in format "yyyy-MM-dd'T'HH:mm:ssZ"
* not in format "yyyy-MM-dd'T'HH:mmZ"
* not in format "yyyy-MM-dd HH:mm:ssX"
* in format "yyyy-MM-dd HH:mm:ss" and is 2018-03-03 10:38:54+0000


Process finished with exit code 0
```

I've seen other code that asks the caller to a ``DateUtil`` to already know the format - that might be prone
to error - I'm hoping this framework would be easier to extend without needing to interfere with the calling
code at all.

Clearly, if this wasn't a poor-man's-unit-test there'd be a break in the ``for`` loop once a suitable date
had been found.