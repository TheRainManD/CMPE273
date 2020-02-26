from ariadne import QueryType, graphql_sync, make_executable_schema, MutationType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify

student_id = 0
class_id = 1000

students = []
classes = []

type_defs = """
    type Query {
        hello: String!
        students: [Student]
        find_student(sid: Int): Student
        classes: [Class]
        class_student(cid: Int): Class
    }

    type Mutation {
        create_student(name: String!): Boolean!
        create_class(cid: Int!, name: String!): Boolean!
        add_students(cid: Int!, sid: Int!): Boolean!
    }

    type Student {
        sid: Int
        name: String
    }

    type Class {
        cid: Int
        name: String
        students: [Student]
    }
 
"""

mutation = MutationType()
query = QueryType()

@mutation.field("create_student")
def resolve_create_student(_, info, name):
    global student_id
    student_id += 1
    students.append({'sid': student_id, 'name': name})
    return True

@query.field("find_student")
def resolve_find_student(_, info, sid):
    #return next(item["name"] for item in students if item["sid"] == sid)
    return next(item for item in students if item["sid"] == sid)

@mutation.field("create_class")
def resolve_create_class(_, info, cid, name):
    classes.append({'cid': cid, 'name': name, 'students': []})
    return True

@query.field("students")
def resolve_get_student(_, info):
    return students

@query.field("classes")
def resolve_get_classes(_, info):
    return classes

@mutation.field("add_students")
def resolve_add_students(_, info, sid, cid):
    s_name = next(s["name"] for s in students if s["sid"] == sid)
    for c in classes:
        if c["cid"] == cid:
            #has to append {"name":s_name}, due to Type Student
            c["students"].append({"name":s_name})
    return True

@query.field("class_student")
def resolve_class_student(_, info, cid):
    print(classes)
    return next(item for item in classes if item["cid"] == cid)

@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    return "Hello, %s!" % user_agent


schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)