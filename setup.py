from distutils.core import setup
setup(
  name = 'semilimes',         
  packages = ['semilimes'],   
  version = '0.1.1',      
  license='gpl-3.0',        
  description = 'semilimes connector library',   
  author = 'Flavio Ansovini',                   
  author_email = 'flavioansovini@gmail.com',     
  url = 'https://github.com/pernicious-flier/semilimes_python_library',   
  download_url = 'https://github.com/pernicious-flier/semilimes_python_library    
  keywords = ['semilimes', 'messenger', 'IOT', 'connector'],  
  install_requires=[            
          'websocket_client',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: gpl-3.0', 
    'Programming Language :: Python ',  
    'Programming Language :: Python :: 2',  
    'Programming Language :: Python :: 2.6',  
    'Programming Language :: Python :: 2.7',  
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)