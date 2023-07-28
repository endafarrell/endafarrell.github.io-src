Valid PostGIS geometries via python
###################################

:summary: PostGIS's `ST_IsValid` is not always straight-forward.


I have a database with 2,746,617,990 different geometries. These ~3 billion
geometries are points, linestrings, polygons and multipolygons and they 
represent the shapes needed to draw maps of the world. They cover roads,
houses, parks, lakes, intersections of all kinds, point addresses right 
through to countries and continents. 

With such a large collection have to deal with all sorts of edge
cases and data problems. The data pipeline that we are running transforms
geometries from protobuf into PostGIS via CSV for fast loading into the 
database. 

Python ETL
----------
Our "Extract, Transform, Load" pipeline is python based. We have a wide range
of sources from which to extract and get get the data in a number of different
formats - protobuf, geojson, not-geo json, some xml and shapefiles.

In our transforms we mostly use `shapely <https://pypi.org/project/Shapely/>`_ to 
handle the geometries. We load/create them and use ``shapely.wkt.dumps`` to write 
WKT representations of the geometries. Given the size of the data, and that I agree with 
`XKCD.2170 <https://xkcd.com/2170/>`_, we limit our precisions (which also greatly 
reduces the physical size on disk of our data) to 8 digits.

Our load for the PostGIS (via AWS's RDS) uses 
``f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, HEADER);"`` as for our setup it
has proven itself to be the fastest way to populate the database.

We have invalid geometries
--------------------------
Recently we have begun to offer more ways of accessing this data and have found 
that some of the geometries are invalid - as far as ``ST_IsValid`` is concerned. 
None of our sources claim to have ``ST_IsValid`` geometries, and in any case, as we
are transforming the data, its our own responsibility to get this right. Here's a 
little of what we have learnt.

Invalid PostGIS geometries can be rendered as geojson
-----------------------------------------------------
Javascript rendering of geojson does not imply that the geometry is valid as
far as PostGIS is concerned. There is a significant up-side to this - your 
PostGIS is able to load and return invalid geometries.

.. figure:: {static}/images/2020/geojson-render.png
   :height: 80pc

This geometry, is invalid as it self-intersects. All of those "internal" lines
make for beautiful images showing something of the internal structure of the
building, but PostGIS does not consider them to be valid:

.. code:: sql

    spatialindex=> SELECT ST_IsValid(geometry), ST_IsValidReason(geometry)
    spatialindex-> FROM BuildingFootprintGeometry
    spatialindex-> WHERE identifier = 'here:ec:building-loc:61561';
    NOTICE:  Self-intersection at or near point -73.988937442643163 40.734395016371103
     st_isvalid |                   st_isvalidreason
    ------------+-------------------------------------------------------
     f          | Self-intersection[-73.9889374426432 40.7343950163711]
    (1 row)

    spatialindex=>

The image above was of a Javascript rendering of the geojson selected from this
``BuildingFootprintGeometry`` row. Clearly PostGIS will import and export these
rows, and that allows us to see our data.

shapely's ``is_valid`` does not guarantee PostGIS's ``ST_IsValid``
------------------------------------------------------------------
Having found the issue above, we refactored a test-set to guarantee that the 
shapely geometries were valid. The first refactor checked the `is_valid` but 
then dumped a WKT with a precision of 8 digits (+- 0.3 mm when dealing with 
country-sized geometries is more than enough precision). We then re-refactored
to first (1) dump at 8 digits, (2) reload the 8-digit WKT and check that _it_
is valid, (3) if #2 is valid, return #1, else use `.buffer(0)` and confirm that
#3 is valid. At this point, we knew our shapely geometries were valid.

.. code:: python


However, PostGIS still found 



