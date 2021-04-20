# inventools

### Inventools helps to covert yield value to Json or csv output


## Example to user yeild value to csv

.. code-block:: python

    from inventools import tools

    Name_of_file = "language"

    header_in_list=['s_no','language','version']

    output_in_list = ["1","python","0.1"]

    @tools.write_csv(Name_of_file,header_in_list)
    def foo():
        yield(output_in_list)
    foo()


#### output location in relative path 

    └───output_csv
            language.csv


## Example to user yeild value to json

.. code-block:: python

    from inventools import tools

    Name_of_file = "language"

    header_in_list=['s_no','language','version']

    output_in_list = ["1","python","0.1"]

    @tools.write_json(Name_of_file,header_in_list)
    def foo():
        yield(output_in_list)
    foo()


#### output location in relative path 
    └───output_json
            language.json


#####  Iteratable example 


.. code-block:: python

    from inventools import tools

    Name_of_file = "language"

    header_in_list=['s_no','language','version']

    iteratable_object_in_list = [[1,"python",0.1],[2,"java",11],[3,"kotlin",2],[4,"golang",2]]

    @tools.write_csv(Name_of_file,header_in_list)
    def foo():
        for output_in_list in iteratable_object_in_list:
            yield(output_in_list)
    foo()
