**Create a test** <br />
http://127.0.0.1:5000/tests  POST <br />
sample input:
```json
{
	"subject":"Math",
	"answer_keys":"ABCDEF"
}
```

**View created test** <br />
http://127.0.0.1:5000/tests/1  GET <br />
enter the test id of the test you want to view after /tests/
<img width="972" alt="Screen Shot 2020-04-25 at 4 49 22 PM" src="https://user-images.githubusercontent.com/33642497/80293695-526b1080-8716-11ea-9c59-0b5e9c1fe549.png">

**Upload scantron** <br />
http://127.0.0.1:5000/tests/scantrons  POST <br />
upload scantron in json version
<img width="978" alt="Screen Shot 2020-04-25 at 4 49 34 PM" src="https://user-images.githubusercontent.com/33642497/80293706-7cbcce00-8716-11ea-8d3d-daeb850a971d.png">


**View all submission** <br />
http://127.0.0.1:5000/tests/grades/1 GET <br />
this means to retrieve all the data releated to test id 1 
<img width="971" alt="Screen Shot 2020-04-25 at 4 49 14 PM" src="https://user-images.githubusercontent.com/33642497/80293658-f607f100-8715-11ea-9526-c75692209af7.png">

