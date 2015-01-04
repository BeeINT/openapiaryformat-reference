Examples
=========

Simple hive:

.. code-block:: javascript


  {
    "type" : "hive",
    "name" : "My Second Hive",
    "identifier": "a9d19090b1b7f675b50e06652fd0a8b7ff252945",
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
          "type" : "link",
          "identifier": "a9d19090b1b7f675b50e06652fd0a8b7ff252945",
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

