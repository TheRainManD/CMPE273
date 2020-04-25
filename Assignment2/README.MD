**Create a test**
http://127.0.0.1:5000/tests  POST
sample input:
```json
{
	"subject":"Math",
	"answer_keys":"ABCDEF"
}
```

**View created test**
http://127.0.0.1:5000/tests/1  GET
enter the test id of the test you want to view after /tests/

**Upload scantron**
http://127.0.0.1:5000/tests/scantrons  POST
upload scantron in json version



**View all submission**
http://127.0.0.1:5000/tests/grades/1 GET <br />
this means to retrieve all the data releated to test id 1
