# MedcostGuider
a tool to compare medical procedures costs in geographic location

#  Motivation
   

#  Pipeline
   ![alt text](https://github.com/parimalak/MedcostGuider/blob/master/img/pipeline.PNG "Data Pipeline")
#  Github Repo structure
   The directory structure of repo look like this:

    ├── README.md 
    ├── flask
        └── app
            |── static
            |   |   └── css
            |   |   └── js
            |   |   └── fonts
            |── templates
            |   |   └── index.html
            |── views.py      
    │   └── run.py
    │   └── tornadoapp.py
    ├── generate_dta
    │   └── procedure_code.py
    ├── redshift_queries
    |   └── copy_s3_redshift.sql
    |   └── procedure_city.txt
    |   └── table_creation.sql
    
#  Prerequisites
#  Resources
   ### Presentation : Medicost Guider (https://www.slideshare.net/parimalakillada/medicost-guider)
   ### Website      : Demo (www.parimala.killada.site)
