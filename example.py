from inventools import tools

Name_of_file = "language"

header_in_list=['s_no','language','version']

iteratable_object_in_list = [[1,"python",0.1],[2,"java",11],[3,"kotlin",2],[4,"golang",2]]

@tools.write_csv(Name_of_file,header_in_list)
def foo():
    for output_in_list in iteratable_object_in_list:
        yield(output_in_list)
foo()