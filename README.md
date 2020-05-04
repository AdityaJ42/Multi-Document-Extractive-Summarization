# Multi-Document-Extractive-Summarization

The implemented system look to use either sinle or multiple documents uploaded by the user, break down the contents and extract those sentences which are most relevant to the content, thereby generating a summary of the document cluster.

## Environment Setup
### Pre-requisites
```
python >= 3.6
```

### Clone this respository and run these commands in the directory
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver
pip install git+https://github.com/boudinfl/pke.git
```

To view the website visit http://localhost:8000

### Running project
Home Page: Upload the required files here
![image](https://user-images.githubusercontent.com/32266008/80939871-a0a99f00-8dfb-11ea-8a70-6ae053220265.png)

Summary Page: The generated summary is displayed here along with options to
              1. Download the generated summary
              2. Regnerate the summary
              3. Reset the project to load a fresh set of documents

Generated Summary
![image](https://user-images.githubusercontent.com/32266008/80940200-a653b480-8dfc-11ea-8cb6-8ede41da4ecb.png)

Regenerated Summary
![image](https://user-images.githubusercontent.com/32266008/80940243-d00cdb80-8dfc-11ea-80d8-d826cf0b5dc6.png)

Project Whitebook - [PDF](https://drive.google.com/open?id=1njlH25-RpthdMTs8QLQIBKce9GtS2tSR)

Team Members:
  *[Aditya Jeswani](https://github.com/adityaj42)
  *[Shruti More](https://github.com/shrutim24)
  *[Kabir Kapoor](https://github.com/KabirKapoor)
  *[Sifat Sheikh](https://github.com/sifatyk)
