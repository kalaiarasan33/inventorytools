from distutils.core import setup
    
setup(
  name = 'inventools',         # How you named your package folder (MyLib)
  packages = ['inventools'],   # Chose the same as "name"
  version = '2.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Inventory tools helps to convert yeild return value to Json or CSV',   # Give a short description about your library
  author = 'Kalaiarasan',                   # Type in your name
  author_email = 'kalaiarsanbalaraman@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kalaiarasan33/inventools',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kalaiarasan33/inventools/archive/refs/heads/main.zip',    # I explain this later on
  keywords = ['inventools','inventools package''pip install inventools''json', 'csv', 'yield','yeild output to json', 'yeild output to csv'],   # Keywords that define your package best
  # install_requires=[            # I get to this in a second
  #         'json',
  #         'itertools',
  #         'functools'

  #     ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8', 
    'Programming Language :: Python :: 3.9'#Specify which pyhton versions that you want to support
  ],
)