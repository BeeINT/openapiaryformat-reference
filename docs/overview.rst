openapiaryformat-reference
==========================

The goal of this format is to create a way for different independent projects and data sources to share their data of bees and apiaries. 
The format specifications and reference implementations for an easy start will be public available and open sources




Mission statements
---------------------

* The format can be used in a very lean way but should be powerfull enough to handle all cases.
* The current state of the apiaries and hives is always easy avaialble and does not require computing 
* A journal of the history of an apiary or hive can be added but is optinal.



Examples
------------

Simple hive:

.. code-block:: javascript


  {
    "name" : "My Second Hive"
    "type" : "hive"
    "description" : "Watch your step",
  }





Simple apiary:

.. code-block:: javascript
   


  {
    { 
      "type": "apiary",
      "name": "My Apiary",
      "description" : "this is my apiary",
      "location" : {
        "latitude": 0.023,
        "longitude": 0.123
      },
      "hives":{
        {
          "name" : "My First Hive",
        },
      }
    }
  }






.. code-block:: javascript


  {
    "name" : "My Second Hive"
    "type" : "hive"
    "description" : "Watch your step",
  }

